import json


def to_graphviz(traceroute, no_rtt=False):
    '''
    Convert a traceroute to a graphviz object.

    This method creates a GraphViz object from the output of
    DublinTraceroute.traceroute(), suitable for plotting.

    Example:
    >>> dub = DublinTraceroute(12345, 33434, "8.8.8.8")
    >>> results = dub.traceroute()
    >>> graph = to_graphviz(results)
    >>> graph.draw('traceroute.png')
    >>> graph.write('traceroute.dot')
    '''
    # importing here, so if pygraphviz is not installed it will not fail at
    # import time
    import pygraphviz

    graph = pygraphviz.AGraph(strict=False, directed=True)
    graph.node_attr['shape'] = 'ellipse'
    graph.graph_attr['rankdir'] = 'BT'

    # create a dummy first node to add the source host to the graph
    # FIXME this approach sucks
    for flow, hops in traceroute['flows'].items():
        src_ip = hops[0]['sent']['ip']['src']
        firsthop = {}
        hops = [firsthop] + hops
        color = random.randrange(0, 0xffffff)

        previous_nat_id = 0
        for index, hop in enumerate(hops):

            # add node
            if index == 0:
                # first hop, the source host
                nodename = src_ip
                graph.add_node(nodename, shape='rectangle')
            else:
                # all the other hops
                received = hop.get('received', None)
                nodeattrs = {}
                if received is None:
                    nodename = 'NULL{idx}'.format(idx=index)
                    nodeattrs['label'] = '*'
                else:
                    nodename = received['ip']['src']
                    if hop['name'] != nodename:
                        hostname = '\n{h}'.format(h=hop['name'])
                    else:
                        hostname = ''

                    # MPLS labels
                    try:
                        labels = received['icmp']['mpls_labels']
                    except KeyError:
                        labels = []
                    if labels:
                        mpls = 'MPLS labels: \n'
                        for label in labels:
                            mpls += '- {l}, ttl: {t}\n'.format(
                                l=label['label'],
                                t=label['ttl'],
                            )
                    else:
                        mpls = ''
                    nodeattrs['label'] = '{ip}{name}\n{icmp}\n{mpls}'.format(
                        ip=nodename,
                        name=hostname,
                        icmp=received['icmp']['description'],
                        mpls=mpls,
                    )
                if index == 0 or hop['is_last']:
                    nodeattrs['shape'] = 'rectangle'
                graph.add_node(nodename)
                graph.get_node(nodename).attr.update(nodeattrs)

            # add edge
            try:
                nexthop = hops[index + 1]
            except IndexError:
                # This means that we are at the last hop, no further edge
                continue

            next_received = nexthop.get('received', None)
            edgeattrs = {'color': '#{c:x}'.format(c=color), 'label': ''}
            if next_received is None:
                next_nodename = 'NULL{idx}'.format(idx=index + 1)
            else:
                next_nodename = next_received['ip']['src']
            if index == 0:
                u = nexthop['sent']['udp']
                edgeattrs['label'] = 'srcport {sp}\ndstport {dp}'.format(sp=u['sport'], dp=u['dport'])
            rtt = nexthop['rtt_usec']
            try:
                if previous_nat_id != nexthop['nat_id']:
                    edgeattrs['label'] += '\nNAT detected'
                previous_nat_id = hop['nat_id']
            except KeyError:
                pass
            if not no_rtt:
                if rtt is not None:
                    edgeattrs['label'] += '\n{sec}.{usec} ms'.format(
                        sec=rtt // 1000, usec=rtt % 1000)
            graph.add_edge(nodename, next_nodename)
            graph.get_edge(nodename, next_nodename).attr.update(edgeattrs)

    graph.layout()
    return graph

to_graphviz(json.load("trace.json"))