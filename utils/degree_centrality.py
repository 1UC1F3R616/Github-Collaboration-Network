import matplotlib.pyplot as plt
import networkx as nx

# code imports
from github_scrape import followers, following

# We have directed graph over here of Followers and Following Users
# So we will be using degree centrality formula for Directed Graph

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
# Edges are | for Centrality:: username<<---following | followers--->>username
# Directed Grpah uses OutLinks only

username = "1UC1F3R616"  # 'IMRO832000'
# (followers + following)^(followers + following)  == (100 + 13)*2

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


# Write Graph
nx.write_edgelist(G, "luc1f3r616.edgelist")

# Read Graph
# G = nx.read_edgelist("1uc1f3r616.edgelist", create_using=nx.DiGraph)

## Indegree --> Importance of User | Biased if considering only self

centrality = nx.out_degree_centrality(G)  # out gives us the centrality measure
# G2 = G.reverse(copy=True)
prestige = nx.in_degree_centrality(G)  # Indegree will give us prestige measure

# Finding Top 5 if they exsists
result = [[k, v] for k, v in prestige.items()]
result.sort(key=lambda x: x[1], reverse=True)
if len(prestige) >= 5:
    print(result[:5])
else:
    print(result[: len(prestige)])
# print(max(result, key=result.get))
# Plot the degree/prestige distribution of the GitHub collaboration network
# plt.hist(list(nx.degree_centrality(G).values()))
# print(G.in_edges('1UC1F3R616'))
# print(G.out_edges('1UC1F3R616'))
nx.draw_networkx(G)
plt.show()

## What does username means in prestige code (Inlinks that is following)?
### It means that that person has highest following in the network of the user who gave his username. Considering only his/her nodes.
