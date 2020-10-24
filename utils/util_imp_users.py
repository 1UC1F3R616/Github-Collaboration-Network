
import networkx as nx

# code imports
from .github_scrape import followers, following

def imp_users(username):
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

    centrality = nx.out_degree_centrality(G)
    prestige = nx.in_degree_centrality(G)

    result = [[k, v] for k, v in prestige.items()]
    result.sort(key=lambda x: x[1], reverse=True)
    if len(prestige) >= 5:
        return result[:5]
    else:
        return result[: len(prestige)]
