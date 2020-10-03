# using set differences, recommend repositories from a second user that the first user should contribute to

import networkx as nx
from networkx.algorithms import bipartite

from github_scrape import followers, following, get_repos

G = nx.Graph()

def recommend_repositories(G, from_user, to_user):

    users = [from_user, to_user]
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
    # Get the set of repositories that from_user has contributed to
    from_repos = set(G.neighbors(from_user))
    # Get the set of repositories that to_user has contributed to
    to_repos = set(G.neighbors(to_user))

    # Identify repositories that the from_user is connected to that the to_user is not connected to
    return from_repos.difference(to_repos)

# Print the repositories to be recommended
print(recommend_repositories(G, '1UC1F3R616', 'Defcon27'))