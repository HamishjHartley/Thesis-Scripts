import networkx as nx
import yaml

def generate_containerlab_topology(graph, output_file="topology.yaml"):
    topology = {
        "name": "barabasi-albert-topology",
        "nodes": {},
        "links": []
    }

    # Create nodes for the topology
    for node in graph.nodes:
        topology["nodes"][f"node{node}"] = {
            "kind": "srl",  # Example node kind, can be changed as needed
            "image": "ghcr.io/nokia/srlinux",  # Example image, can be customized
            "mgmt_ipv4": f"192.168.1.{node + 2}/24"  # Example IP, modify IP scheme as needed
        }

    # Create links between nodes
    for edge in graph.edges:
        topology["links"].append({
            "endpoints": [f"node{edge[0]}:eth1", f"node{edge[1]}:eth1"]  # Example interface, modify as needed
        })

    # Write the topology to a YAML file
    with open(output_file, 'w') as file:
        yaml.dump(topology, file, default_flow_style=False)

    print(f"Topology file '{output_file}' generated successfully.")

# Example usage:
# Generate a Barabási-Albert graph
G = nx.barabasi_albert_graph(10, 2)

# Convert the graph into a Containerlab YAML topology file
generate_containerlab_topology(G, "ba_topology.yaml")
