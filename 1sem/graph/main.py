class Graph:
    pass


class DFS:
    pass


ex1_dfs = """
   B-C-D
   | |
   A-E-F-G
"""
ex1_dfs_dated = """
   (Bw)(-2o)(Cw)(-2o)(Dw)
   (|2o) (|2o)
   (Aw)(-2)(Ew)(-2)(Fw)(-2)(Gw)
"""


# Основная функция
def main():
    graph = Graph(image=ex1_dfs_dated)
    graph.run(alghoritm=DFS)

if __name__ == "__main__":
    main()
