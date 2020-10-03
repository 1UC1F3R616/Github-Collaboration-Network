# using set differences, recommend repositories from a second user that the first user should contribute to
# Method 2 (current Method): Recommend repo with max edges from my network
import networkx as nx
from networkx.algorithms import bipartite

from github_scrape import followers, following, get_repos


"""
Older Code that use to find differ set from the two users
that is suggest repos that that user2 can contribute from user1 repo
"""
# G = nx.Graph()

# def recommend_repositories(G, from_user, to_user):

#     users = [from_user, to_user]
#     repos = set()
#     user2repo = []
#     for user in users:
#         user_repos = get_repos(user, url="", repo_list=[])
#         repos.update(repo + "_repo" for repo in user_repos)
#         user2repo += [(user, repo + "_repo") for repo in user_repos]
#     repos = list(repos)
#     # print(repos)

#     G.add_nodes_from(users, bipartite="users")
#     G.add_nodes_from(repos, bipartite="repos")

#     # print(G.nodes(data=True))

#     G.add_edges_from(user2repo)

#     print(nx.is_bipartite(G))
#     # Get the set of repositories that from_user has contributed to
#     from_repos = set(G.neighbors(from_user))
#     # Get the set of repositories that to_user has contributed to
#     to_repos = set(G.neighbors(to_user))

#     # Identify repositories that the from_user is connected to that the to_user is not connected to
#     return from_repos.difference(to_repos)


# # Print the repositories to be recommended
# print(recommend_repositories(G, "1UC1F3R616", "Defcon27"))

############################Method2#################################

G = nx.Graph()
username = "1UC1F3R616"

users = set()
users.update(user for user in followers(username, page="1", followers_list=[]))
users.update(user for user in following(username, page="1", following_list=[]))

users = list(users)
repos = set()
user2repo = []
for user in users:
    if user == username: # Don't recommend self repos
        continue
    user_repos = get_repos(user, url="", repo_list=[])
    repos.update(repo + "_repo" for repo in user_repos)
    user2repo += [(user, repo + "_repo") for repo in user_repos]
repos = list(repos)
G.add_nodes_from(users, bipartite="users")
G.add_nodes_from(repos, bipartite="repos")
G.add_edges_from(user2repo)

nx.write_edgelist(G, "imro8_bipartite_recommending_repo.edgelist")

# G = nx.read_edgelist('imro8_bipartite_recommending_repo.edgelist')
# print(G.edges())

# repos  = ['teach-flask-through-doing_repo', 'Hades_App_repo']
for repo in repos:
    degX, degY = bipartite.degrees(G, repo)
    break
degX = list(degX)

repos_only = []
for ind in degX:
    if ind[0] not in users:
        repos_only.append(ind)

repos_only.sort(key=lambda x: x[-1], reverse=True)
print(repos_only[:10])
