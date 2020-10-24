# Recommending co-editors who have yet to edit together
# leverage the concept of open triangles to recommend users on GitHub to collaborate!

# Import necessary modules
from itertools import combinations
from collections import defaultdict
import networkx as nx

# Initialize the defaultdict: recommended
recommended = defaultdict(int)

G = nx.read_edgelist("luc1f3r616.edgelist", create_using=nx.DiGraph)

# Iterate over all the nodes in G
for n, d in G.nodes(data=True):

    # Iterate over all possible triangle relationship combinations
    for n1, n2 in combinations(G.neighbors(n), 2):

        # Check whether n1 and n2 do not have an edge
        if not G.has_edge(n1, n2):

            # Increment recommended
            recommended[(n1, n2)] += 1

# Identify the top 10 pairs of users
all_counts = sorted(recommended.values())
top10_pairs = [pair for pair, count in recommended.items() if count > all_counts[-10]]
print(top10_pairs)
