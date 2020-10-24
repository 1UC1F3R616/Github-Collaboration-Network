import networkx as nx
from networkx.algorithms import bipartite

from .github_scrape import followers, following, get_repos

def commit_here(username):
    G = nx.Graph()

    users = set()
    users.update(user for user in followers(username, page="1", followers_list=[]))
    users.update(user for user in following(username, page="1", following_list=[]))

    users = list(users)
    repos = set()
    user2repo = []
    for user in users:
        if user == username:
            continue
        user_repos = get_repos(user, url="", repo_list=[])
        repos.update(repo + "_repo" for repo in user_repos)
        user2repo += [(user, repo + "_repo") for repo in user_repos]
    repos = list(repos)
    G.add_nodes_from(users, bipartite="users")
    G.add_nodes_from(repos, bipartite="repos")
    G.add_edges_from(user2repo)


    for repo in repos:
        degX, degY = bipartite.degrees(G, repo)
        break
    degX = list(degX)

    repos_only = []
    for ind in degX:
        if ind[0] not in users:
            repos_only.append(ind)

    repos_only.sort(key=lambda x: x[-1], reverse=True)
    repos_only = [list(repo) for repo in repos_only]
    return repos_only[:10]
