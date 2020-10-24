from itertools import combinations
from collections import defaultdict
import networkx as nx

from .github_scrape import followers, following

def recommended_networking(username):
    recommended = defaultdict(int)

    G = nx.DiGraph(
        directed=True,
        arrows=True,
        options={
            "node_color": "blue",
            "node_size": 100,
            "width": 3,
            "arrowstyle": "-|>",
            "arrowsize": 12,
        },
    )

    followers_list = followers(username)
    following_list = following(username)

    total_users = list(set(followers_list + following_list))

    ## Prestige | Reversed the link for graph nodes
    for follower_ in followers_list:
        G.add_edge(follower_, username)

    for following_ in following_list:
        G.add_edge(username, following_)


    for user in total_users:
        print("current user is {}, total users are {}".format(user, len(total_users)))
        try:
            followers_list_ = followers(user, page="1", followers_list=[])
            following_list_ = following(user, page="1", following_list=[])

            for follower_ in followers_list_:
                if follower_ in total_users:
                    G.add_edge(follower_, user)

            for following_ in following_list_:
                if following_ in total_users:
                    G.add_edge(user, following_)
        except Exception as e:
            print(e)
            pass

    for n, d in G.nodes(data=True):

        for n1, n2 in combinations(G.neighbors(n), 2):

            if not G.has_edge(n1, n2):

                recommended[(n1, n2)] += 1

    all_counts = sorted(recommended.values())
    top10_pairs = [pair for pair, count in recommended.items() if count > all_counts[-10]]
    top10_pairs = [list(pair) for pair in top10_pairs]
    return top10_pairs
