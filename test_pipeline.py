import networkx as nx
import yaml
from collections import OrderedDict

# Topology generation
erdos_renyi_1 = nx.erdos_renyi_graph(5, 1)
erdos_renyi_1 = nx.erdos_renyi_graph(5, 0.2)

barabasi_albert_1 = nx.barabasi_albert_graph(3, 2)
barabasi_albert_2 = nx.barabasi_albert_graph(5, 4)

# Parse to YML
def parse_to_yml(graph: nx.Graph):
    # Define output file name
    output_file = "output_topology.yaml"

    # Define topology as an OrderedDict
    topology = OrderedDict({
        "name": "output_topology",
        "topology": OrderedDict({
            "nodes": OrderedDict(),
            "links": []
        })
    })

    # Adding definitions to each node in topology
    for node in graph.nodes:
        topology["topology"]["nodes"][node] = {
            "kind": "srl",
            "image": "ghcr.io/nokia/srlinux",
        }

    # Creating links between the nodes
    for edge in graph.edges:
        topology["topology"]["links"].append({
            "endpoints": [f"{edge[0]}:eth1", f"{edge[1]}:eth1"]
        })

    # Convert OrderedDict to a regular dict before dumping to YAML
    topology_dict = dict(topology)
    topology_dict["topology"] = dict(topology["topology"])
    
    # Parse topology to YAML file
    with open(output_file, 'w') as file:
        yaml.dump(topology_dict, file, default_flow_style=False)

    print("YAML file created successfully!")

parse_to_yml(barabasi_albert_1)