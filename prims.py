
def ExtractMin(Q, key):

    min_vertex = None
    min_value = float('inf')

    for vertex in Q:


        if key[vertex] < min_value:
            print("here", key[vertex])
            print("here", key)

            min_value = key[vertex]
            min_vertex = vertex
    print("finished",'\n')
    return min_vertex


def MST_Prim(G, vertices, r):


    Q = vertices.copy()

    key = {}            #minimum weight
    p = {}              #parent node
    T = {}              # included into the tree



    for u in Q:         #initialization

        key[u] = float('inf')

        p[u] = None

        T[u] = 0



    key[r] = 0            #root node cost

    print("\nPrim Algorithm Execution\n")


    while len(Q) != 0:          #until all vertices

        # --------------------------------------------
        # Select the vertex whose connection cost
        # to the current MST is minimum.
        #
        # This vertex now becomes part of the MST.
        # --------------------------------------------

        u = ExtractMin(Q, key)

        Q.remove(u)                     #removing processed vertices
        print("here final:",u)

        T[u] = 1                            #included in the tree

        print(
            f"Added {u} to MST "
            f"(key={key[u]})"
        )

        u_index = vertices.index(u)

        # --------------------------------------------
        # Examine every adjacent vertex of u.
        # --------------------------------------------

        for v_index in range(len(vertices)):

            if G[u_index][v_index] != 0 and \
               G[u_index][v_index] != float('inf'):

                v = vertices[v_index]

                weight = G[u_index][v_index]

                # --------------------------------------------
                # If v is not yet in MST and
                # edge(u,v) is cheaper than the
                # best connection previously known,
                # then improve key[v].
                # --------------------------------------------

                if v in Q and weight < key[v]:      #v not included in tree and if weight minimum than previous

                    p[v] = u

                    key[v] = weight

                    print(
                        f"Updated {v}: "
                        f"parent={u}, "
                        f"key={weight}"
                    )

    # --------------------------------------------
    # Final MST Table
    # --------------------------------------------

    print("\n\nFINAL TABLE")
    print("-----------------------------------")
    print("Vertex\tKey\tParent")

    total_cost = 0

    for v in vertices:

        print(
            f"{v}\t"
            f"{key[v]}\t"
            f"{p[v]}"
        )

        total_cost += key[v]

    print("\nMST Cost =", total_cost)



INF = float('inf')

G = [

# a  b  c  d  e  f  g  h  i

[0, 4,INF,INF,INF,INF,INF, 8,INF],  # a
[4, 0, 8,INF,INF,INF,INF,11,INF],  # b
[INF,8,0,7,INF,4,INF,INF,2],        # c
[INF,INF,7,0,9,14,INF,INF,INF],     # d
[INF,INF,INF,9,0,10,INF,INF,INF],   # e
[INF,INF,4,14,10,0,2,INF,INF],      # f
[INF,INF,INF,INF,INF,2,0,1,6],      # g
[8,11,INF,INF,INF,INF,1,0,7],       # h
[INF,INF,2,INF,INF,INF,6,7,0]       # i

]

vertices = ['a','b','c','d','e','f','g','h','i']

MST_Prim(G, vertices, 'a')
