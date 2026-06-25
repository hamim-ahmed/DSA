# ------------------------------------------------------------
# Make-Set(x)
#
# Create a new set whose only member is x.
#
# Initially every vertex belongs to its own set.
# ------------------------------------------------------------

def Make_Set(parent, vertex):

    parent[vertex] = vertex


# ------------------------------------------------------------
# Find-Set(x)
#
# Return the representative (root) of the set
# containing vertex x.
#
# If two vertices have the same representative,
# they belong to the same tree.
# ------------------------------------------------------------

def Find_Set(parent, vertex):

    while parent[vertex] != vertex:

        vertex = parent[vertex]

    return vertex


# ------------------------------------------------------------
# Union(x, y)
#
# Merge the two different sets into one.
#
# After Union(), both vertices belong to the
# same connected component.
# ------------------------------------------------------------

def Union(parent, u, v):

    root_u = Find_Set(parent, u)    #finding node u's parent

    root_v = Find_Set(parent, v)    #finding node v's parent

    parent[root_v] = root_u          # assigning u as the root of both tree union


# ------------------------------------------------------------
# MST-Kruskal(G,w)
# ------------------------------------------------------------

def MST_Kruskal(vertices, edges):

    # --------------------------------------------------------
    # A ← Ø
    #
    # A stores all edges selected for the MST.
    # --------------------------------------------------------

    A = []     #selected list for mst

    parent = {}     #initial parent for everyone.

    

    for vertex in vertices:

        Make_Set(parent, vertex)

    # --------------------------------------------------------
    # Sort every edge according to increasing weight.
    #
    # Kruskal always tries the cheapest edge first.
    # --------------------------------------------------------

    edges = sorted(edges, key=lambda edge: edge[2])

    print("Edges after sorting:\n")

    for edge in edges:

        print(edge)

    print("\nExecuting Kruskal Algorithm\n")

    # --------------------------------------------------------
    # for each edge(u,v)
    # --------------------------------------------------------

    for edge in edges:

        u = edge[0]      #edge one node

        v = edge[1]       #edge other node

        weight = edge[2]

        print(f"\nChecking Edge ({u},{v}) Weight={weight}")

        # ----------------------------------------------------
        # If u and v belong to different trees,
        # then adding this edge will NOT create
        # a cycle.
        #
        # Therefor accept the edge.
        # ----------------------------------------------------

        if Find_Set(parent, u) != Find_Set(parent, v):

            A.append(edge)

            print("Accepted")

            Union(parent, u, v)

        else:

            print("Rejected (Cycle Detected)")

    # --------------------------------------------------------
    # Final MST
    # --------------------------------------------------------

    print("\n\nMinimum Spanning Tree\n")

    total = 0

    for edge in A:

        print(edge)

        total += edge[2]

    print("\nTotal Cost =", total)









vertices = [1,2,3,4,5,6,7,8]

edges = [

    (1,6,54),
    (1,3,47),
    (1,5,80),

    (6,3,75),
    (6,4,74),

    (3,4,88),
    (3,2,55),
    (3,5,23),
    (3,7,66),

    (5,2,32),
    (5,7,93),

    (2,4,31),
    (2,7,74),
    (2,8,79),

    (4,8,29),

    (7,8,68)

]

MST_Kruskal(vertices, edges)