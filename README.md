# Bellman-Ford & Data Structures in Python

Python implementations of the **Bellman-Ford single-source shortest-path algorithm** and several core data structures (binary trees, binary search trees, hash tables), written for a Computer Science Fundamentals course at the Canadian Institute of Technology.

## Contents

| File | What it shows |
| --- | --- |
| `BellmanF_CSF.py` | Bellman-Ford on a weighted directed graph (`GraphBellman` class): relaxes every edge \|V\|−1 times, then does one more pass to detect **negative-weight cycles** |
| `TreeB_CSF.py` | Builds a binary tree from user input (root, left, right) and prints its nodes, in-order traversal, size, height and properties |
| `BSTree_CSF.py` | Generates random binary search trees: any height, a fixed height, and a perfect BST |
| `HashTable_CSF.py` | Hash-table basics using Python dictionaries: lookup, update and insert |

## Bellman-Ford in brief

```python
g = GraphBellman(4)          # 4 vertices
g.addEdge(u, v, w)           # directed edge u → v with weight w (negative weights allowed)
g.BellmanFord(src)           # prints the shortest distance from src to every vertex
```

- Time complexity: **O(V · E)**
- Unlike Dijkstra, it handles negative edge weights, and it reports a negative cycle instead of returning wrong distances

Sample output for the graph in the file (source vertex `3`):

```
Vertex Distance from Source
0		3
1		2
2		4
3		0
```

## Running

Requires Python 3. The tree scripts use the [`binarytree`](https://pypi.org/project/binarytree/) package.

```bash
pip install binarytree

python3 BellmanF_CSF.py
python3 TreeB_CSF.py      # prompts for root / left / right values
python3 BSTree_CSF.py
python3 HashTable_CSF.py
```

## License

[MIT](LICENSE)

---

Built by [Rexhino Kovaci](https://github.com/rexhinokovaci) — DevOps & AI engineer in Tirana, Albania. Need an app built? [Get in touch](mailto:kovacirexhino@gmail.com).
