import networkx as nx
from .github_scrape import followers, following

def largest_community(username):
    G = nx.Graph()

    AtoB = []
    BtoA = []

    followers_list = followers(username)
    following_list = following(username)

    total_users = list(set(followers_list + following_list))

    for user in followers_list:
        AtoB.append([user, username])
    for user in followers_list:
        BtoA.append([username, user])

    for user in total_users:
        print("current user is {}, total users are {}".format(user, len(total_users)))
        try:
            followers_list_ = followers(user, page="1", followers_list=[])
            following_list_ = following(user, page="1", following_list=[])

            for follower_ in followers_list_:
                if follower_ in total_users:
                    AtoB.append([follower_, user])

            for following_ in following_list_:
                if following_ in total_users:
                    BtoA.append([user, following_])

        except Exception as e:
            print(e)
            pass

    for ind in range(len(AtoB)):
        AtoB[ind] = AtoB[ind][::-1]

    nodes = list()

    for obj in AtoB:
        if obj in BtoA and tuple(obj) not in nodes:
            nodes.append(tuple(obj))

    G.add_edges_from(nodes)

    cliques = sorted(nx.find_cliques(G), key=lambda x: len(x))
    result = []
    largest_clique = []
    if len(cliques) > 0:
        largest_clique = cliques[-1]
        result.append(largest_clique)
    if len(cliques) > 1:
        second_largest_cliques = cliques[-2]
        result.append(second_largest_cliques)

    return result