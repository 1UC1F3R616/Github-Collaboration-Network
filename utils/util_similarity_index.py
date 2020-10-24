import networkx as nx
from networkx.algorithms import bipartite

from .github_scrape import followers, following, get_repos


def shared_partition_nodes(G, node1, node2):
    """
    :return: common repos
    """
   
    assert G.nodes[node1]["bipartite"] == G.nodes[node2]["bipartite"]

    
    nbrs1 = G.neighbors(node1)
    nbrs2 = G.neighbors(node2)

    overlap = set(nbrs1).intersection(nbrs2)
    return overlap



def get_nodes_from_partition(G, partition):

    nodes = []

    for n in G.nodes():

        if G.nodes[n]["bipartite"] == partition:

            nodes.append(n)
    return nodes



def user_similarity(G, user1, user2, proj_nodes):

    assert G.nodes[user1]["bipartite"] == "users"
    assert G.nodes[user2]["bipartite"] == "users"

    shared_nodes = shared_partition_nodes(G, user1, user2)
    return len(shared_nodes) / len(proj_nodes)


def similarity_index(username):

    G = nx.Graph()

    users = set()
    users.update(user for user in followers(username, page="1", followers_list=[]))
    users.update(user for user in following(username, page="1", following_list=[]))

    users = list(users)

    repos = set()
    user2repo = []
    for user in users:
        user_repos = get_repos(user, url="", repo_list=[])
        repos.update(repo + "_repo" for repo in user_repos)
        user2repo += [(user, repo + "_repo") for repo in user_repos]
    repos = list(repos)


    G.add_nodes_from(users, bipartite="users")
    G.add_nodes_from(repos, bipartite="repos")

    G.add_edges_from(user2repo)



    repo_nodes = get_nodes_from_partition(G, "repos")

    compare_done = dict()
    similarity_score_matrix = []
    for user1 in users:
        for user2 in users:
            if (user1 != user2) and (user2 not in compare_done):
                similarity_score = user_similarity(G, user1, user2, repo_nodes)
                similarity_score_matrix.append([similarity_score, user1, user2])
                compare_done[user1] = True
    similarity_score_matrix.sort(key=lambda x: x[0], reverse=True)
    return similarity_score_matrix[:5]
