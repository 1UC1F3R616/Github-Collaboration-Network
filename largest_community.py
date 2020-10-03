import matplotlib.pyplot as plt

# Find Maximum Clique which is basically a community in which every person knows each other

# If A-->B then is it B-->A?
# Now make a Undirected Graph using these nodes
# Now Find clique and max_clique

import networkx as nx

from github_scrape import followers, following


G = nx.Graph()

AtoB = []
BtoA = []

username = "1UC1F3R616"  # 'IMRO832000'

followers_list = followers(username)  # A-->B
following_list = following(username)  # B-->A
# followers_list inside tuple is present in following_list tuple when reversed

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
            if follower_ in total_users:  # saving computation here
                AtoB.append([follower_, user])

        for following_ in following_list_:
            if following_ in total_users:  # saving computation here
                BtoA.append([user, following_])

    except Exception as e:
        print(e)
        pass

# Reversing AtoB
for ind in range(len(AtoB)):
    AtoB[ind] = AtoB[ind][::-1]

nodes = list()

for obj in AtoB:
    if obj in BtoA and tuple(obj) not in nodes:
        nodes.append(tuple(obj))

print(nodes)

G.add_edges_from(nodes)

cliques = sorted(nx.find_cliques(G), key=lambda x: len(x))
if len(cliques) > 0:
    largest_clique = cliques[-1]
    if len(cliques) > 1:
        second_largest_cliques = cliques[-2]

print(largest_clique)
print(second_largest_cliques)

nx.draw_networkx(G)
plt.show()
# print()
# print(AtoB)
# print()
# print(BtoA)
