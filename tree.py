# Returns a tree topology expressed as an array
def create_tree(d, G):
    tree = []
    N = int((d^(G+1)-1)/(d-1)) # Total number of nodes
    N_d = d^G # Total number of peripheral nodes
    
    for i in range(N):
        tree.append([i])
        for j in range(N_d):
            tree[i].append(j)
    
    print(tree)

create_tree(2,4)

