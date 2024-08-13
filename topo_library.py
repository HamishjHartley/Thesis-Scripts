import random 

# Individual topology variants
ring = [ring_1, ring_2, ring_3]
bus = [bus_1, bus_2, bus_3]
star = [star_1, star_2, star_3]
mesh = [mesh_1, mesh_2, mesh_3]

# Main topology set
topology_set = [ring, bus, star, mesh]

# Generated topology
generated_topo = []

# Parameter definition
n = 3 # Number of topologies to be selected

for i in range(n):
    # topologies which are to be selected at random from the topology_set, [j,k]
    j = random.randint(len(topology_set)-1)
    k = random.randint(len(topology_set[j])-1)

    # Append to generated topology 
    generated_topo.append(topology_set[j][k])



