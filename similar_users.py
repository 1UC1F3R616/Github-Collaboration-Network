## Finds similarity Index based on repositories in common between 2 users
## Function to find common repositories between 2 users --> shared_partition_nodes
# Tasks
## Construct a bipartite graph G
### Users and Projects
#### Extract All users
#### Extract all repos of those users
##### Now construct the bipartite graph

import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms import bipartite

from github_scrape import followers, following, get_repos

G = nx.Graph()

username = 'IMRO832000'

users = set()
users.update(user for user in followers(username, page='1', followers_list=[]))
users.update(user for user in following(username, page='1', following_list=[]))

users = list(users)

repos = set()
user2repo = []
for user in users:
    user_repos = get_repos(user, url='', repo_list=[])
    repos.update(repo+'_repo' for repo in user_repos)
    user2repo += [(user, repo+'_repo') for repo in user_repos]
repos = list(repos)
# print(repos)

G.add_nodes_from(users, bipartite='users')
G.add_nodes_from(repos, bipartite='repos')

# print(G.nodes(data=True))

G.add_edges_from(user2repo)

print(nx.is_bipartite(G))
# nx.draw_networkx(G) 
# plt.show()

def shared_partition_nodes(G, node1, node2):
    """
    :return: common repos
    """
    # Check that the nodes belong to the same partition
    assert G.nodes[node1]['bipartite'] == G.nodes[node2]['bipartite']

    # Get neighbors of node 1: nbrs1
    nbrs1 = G.neighbors(node1)
    # Get neighbors of node 2: nbrs2
    nbrs2 = G.neighbors(node2)

    # Compute the overlap using set intersections
    overlap = set(nbrs1).intersection(nbrs2)
    return overlap

# Print the number of shared repositories between users
# print((shared_partition_nodes(G, '1UC1F3R616', 'Defcon27')))

# Define get_nodes_from_partition()
def get_nodes_from_partition(G, partition):
    # Initialize an empty list for nodes to be returned
    nodes = []
    # Iterate over each node in the graph G
    for n in G.nodes():
        # Check that the node belongs to the particular partition
        if G.nodes[n]['bipartite'] == partition:
            # If so, append it to the list of nodes
            nodes.append(n)
    return nodes

# Print the number of nodes in the 'projects' partition
print(len(get_nodes_from_partition(G, 'projects')))

# Print the number of nodes in the 'users' partition
print(len(get_nodes_from_partition(G, 'users')))


def user_similarity(G, user1, user2, proj_nodes):
    # Check that the nodes belong to the 'users' partition
    assert G.nodes[user1]['bipartite'] == 'users'
    assert G.nodes[user2]['bipartite'] == 'users'

    # Get the set of nodes shared between the two users
    shared_nodes = shared_partition_nodes(G, user1, user2)

    # Return the fraction of nodes in the projects partition
    return len(shared_nodes) / len(proj_nodes)

# Compute the similarity score between users 
# repo_nodes = get_nodes_from_partition(G, 'repos')
# similarity_score = user_similarity(G, '1UC1F3R616', 'Defcon27', repo_nodes)
# print(similarity_score)

repo_nodes = get_nodes_from_partition(G, 'repos')

compare_done = dict()
similarity_score_matrix = []
for user1 in users:
    for user2 in users:
        if (user1 != user2) and (user2 not in compare_done):
            similarity_score = user_similarity(G, user1, user2, repo_nodes)
            similarity_score_matrix.append([similarity_score, user1, user2])
            compare_done[user1] = True
similarity_score_matrix.sort(key=lambda x: x[0], reverse=True)
print(similarity_score_matrix[:5])
