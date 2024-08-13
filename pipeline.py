import networkx as nx
import yaml
import matplotlib.pyplot as plt
from collections import OrderedDict

#Topology generation
erdos_renyi_1 = nx.erdos_renyi_graph(5,1)
erdos_renyi_1 = nx.erdos_renyi_graph(5,0.2)

barabasi_albert_1 = nx.barabasi_albert_graph(4,2)
barabasi_albert_2 = nx.barabasi_albert_graph(5,4)

# https://stackoverflow.com/questions/45253643/order-preservation-in-yaml-via-python-script
def ordered_dict_representer(self, value):  
    return self.represent_mapping('tag:yaml.org,2002:map', value.items())
yaml.add_representer(OrderedDict, ordered_dict_representer)


#Parse to YML 
def parse_to_yml(graph : nx.graph, image, kind):

    #Define output file name
    output_file = "output_topology.yaml"

    #Define topology as a dictionary
    # Define topology as an OrderedDict
    topology = OrderedDict({
        "name": "output_topology",
        "topology": OrderedDict({
            "nodes": OrderedDict(),
            "links": []
        })
    })

    #Adding definitions to each node in topology
    for node,i in enumerate(graph.nodes):
        topology["topology"]["nodes"][f"node{node}"] = {
            "kind" : kind,
            "image" : image,
        } 

        #Creating links between the nodes
    for edge in graph.edges:
        topology["topology"]["links"].append({
            "endpoints" : [f"node{edge[0]}:eth1", f"node{edge[1]}:eth1"]
        })

    #Parse topology to YAML file
    with open(output_file, 'w') as yaml_file:
        yaml.dump(topology, yaml_file, default_flow_style=False)



    plt.figure(figsize=(3,3))
    nx.draw(graph, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")

    plt.show()

parse_to_yml(barabasi_albert_1, "ghcr.io/nokia/srlinux","srl")

# Deployment of containerlab environment


