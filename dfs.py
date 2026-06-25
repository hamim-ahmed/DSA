# Global timestamp used by DFS
time = 0


def DFS_Visit(G, vertices, u, color, prev, d, f):

    global time

    color[u] = "GRAY"

    # Record the discovery time of u.
    time += 1
    d[u] = time

    print(f"\nDiscovered {u} at time {d[u]}")

    u_index = vertices.index(u)

    # ----------------------------------------------------
    # Explore every outgoing edge of u.
    # ----------------------------------------------------

    for v_index in range(len(vertices)):

        if G[u_index][v_index] == 1:

            v = vertices[v_index]

            # If v has never been visited,
            # then u becomes its parent in the DFS tree.
            if color[v] == "WHITE":

                prev[v] = u

                print(f"{u} -> {v} (Tree Edge)")

                DFS_Visit(
                    G,
                    vertices,
                    v,
                    color,
                    prev,
                    d,
                    f
                )



    color[u] = "BLACK"

    time += 1

    f[u] = time

    print(f"Finished {u} at time {f[u]}")


def DFS(G, vertices):

    global time

    color = {}
    prev = {}
    d = {}
    f = {}

    for u in vertices:

        color[u] = "WHITE"
        prev[u] = None
        d[u] = float('inf')
        f[u] = float('inf')

    time = 0



    for u in vertices:

        if color[u] == "WHITE":

            print(f"\nStarting New DFS Tree from {u}")

            DFS_Visit(
                G,
                vertices,
                u,
                color,
                prev,
                d,
                f
            )

    # ----------------------------------------------------
    # Final DFS Table
    # ----------------------------------------------------

    print("\n\nFINAL DFS TABLE")
    print("------------------------------------------------------")
    print("Vertex\tColor\tDiscovery\tFinish\tPrev")

    for u in vertices:

        print(
            f"{u}\t"
            f"{color[u]}\t"
            f"{d[u]}\t\t"
            f"{f[u]}\t"
            f"{prev[u]}"
        )


# =====================================================
# GRAPH FROM THE IMAGE
# =====================================================

vertices = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

G = [

# S  A  B  C  D  E  F  G

 [0, 1, 0, 1, 1, 0, 0, 0],  # S
 [0, 0, 1, 1, 0, 0, 0, 0],  # A
 [1, 0, 0, 0, 0, 0, 0, 0],  # B
 [0, 0, 1, 0, 0, 0, 0, 0],  # C
 [0, 0, 0, 1, 0, 1, 0, 0],  # D
 [0, 0, 0, 1, 0, 0, 0, 0],  # E
 [0, 0, 0, 0, 1, 1, 0, 1],  # F
 [0, 0, 0, 1, 0, 0, 0, 0]   # G

]

DFS(G, vertices)