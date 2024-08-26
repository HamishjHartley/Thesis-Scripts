import gym
import networkx as nx
import numpy as np
from gym import spaces
from stable_baselines3 import PPO

class NetworkTopologyEnv(gym.Env):
    def __init__(self, target_graphs):
        super(NetworkTopologyEnv, self).__init__()
        self.target_graphs = target_graphs
        self.current_graph = nx.Graph()

        # Define action space: 0 = add node, 1 = add edge
        self.action_space = spaces.Discrete(2)

        # Define observation space: number of nodes and edges in the graph
        self.observation_space = spaces.Box(low=0, high=100, shape=(2,), dtype=np.float32)

    def reset(self):
        self.current_graph = nx.Graph()
        return self._get_observation()

    def step(self, action):
        if action == 0:  # Add a node
            self.current_graph.add_node(len(self.current_graph.nodes))
        elif action == 1:  # Add an edge between two random nodes
            if len(self.current_graph.nodes) > 1:
                node1, node2 = np.random.choice(self.current_graph.nodes, 2, replace=False)
                self.current_graph.add_edge(node1, node2)

        reward = self._compute_reward()
        done = len(self.current_graph.nodes) >= 10  # Example stopping condition
        return self._get_observation(), reward, done, {}

    def _get_observation(self):
        return np.array([len(self.current_graph.nodes), len(self.current_graph.edges)])

    def _compute_reward(self):
        # Compute a reward based on similarity to target graphs
        reward = -1  # Default penalty
        for target in self.target_graphs:
            reward = max(reward, self._graph_similarity(self.current_graph, target))
        return reward

    def _graph_similarity(self, G1, G2):
        # Simplified example: compare number of nodes and edges
        nodes_diff = abs(len(G1.nodes) - len(G2.nodes))
        edges_diff = abs(len(G1.edges) - len(G2.edges))
        return -(nodes_diff + edges_diff)  # Negative reward for difference

# Generate a new topology using the trained model
state = env.reset()
done = False

while not done:
    action, _ = model.predict(state)
    state, reward, done, _ = env.step(action)

# The generated topology is stored in env.current_graph
generated_topology = env.current_graph

# Visualize the generated topology
import matplotlib.pyplot as plt

nx.draw(generated_topology, with_labels=True)
plt.show()


