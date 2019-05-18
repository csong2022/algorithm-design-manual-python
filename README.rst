algorithm-design-manual-python
==============================

Python translation of algorithm design manual C code. Code has been tested in Python 3.6

.. image:: http://www.algorist.com/images/adm2cover.jpg
   :alt: Algorithm Design Manual 2nd Edition
   :target: https://www.amazon.com/exec/obidos/ASIN/1848000693/thealgorith01-20

Original C code <https://www3.cs.stonybrook.edu/~skiena/algorist/book/programs/>

Features:

1. Translated original C programs in procedural language style into Object Oriented fashion. Remove all global variables.
2. Converted original test cases, included in test-script, into set of nosetests.
3. Implemented generic Graph data structure to cover unweighted, weights, flow graph instances. Removed code duplication in original C implementation.


List of files:

Chapter 3. Data Structures
algorist.data_structure

- linked_list.py --- linked implementation.
- linked_stack.py --- Implementation of a LIFO stack abstract data type.
- linked_queue.py --- implementation of a FIFO queue abstract data type.
- tree.py --- binary search tree implementation
- priority_queue.py -- Implementation of a heap / priority queue abstract data type.
- set_union.py --- union-find data structure implementation
- war.py --- simulation of the children's card game War

Chapter 4. Sorting and Search
algorist.sorting

- sorting.py --- implementations of primary sorting algorithms
- polly.py --- rank the desirability of suitors -- sorting example

Chapter 5. Graph Traversal
algorist.graph

- graph.py -- graph data type
- bfs_dfs.py --- generic implementation of breath/depth first search.
- connected.py --- compute connected components of a graph
- bipartite.py --- Two color a bipartite graph
- findcycle.py --- identify a cycle in a graph, if one exists
- biconnected.py --- Identify articulation vertices in a graph
- topsort1.py --- Topologically sort a directed acyclic graph by DFS numbering (DAG)
- topsort.py --- topologically sort a directed acyclic graph
- strong.py --- Identify strongly connected components in a graph

Chapter 6. Weighted Graph Algorithms
algorist.wgraph

- prim.py --- compute minimum spanning trees of graphs via Prim's algorithm
- kruskal.py --- Compute minimum spanning trees of graphs via Kruskal's algorithm.
- dijkstra.py --- compute shortest paths in weighted graphs
- floyd.py --- compute all-pairs shortest paths in weighted graphs
- netflow.py --- network flow implementation -- augmenting path algorithm

Chapter 7. Combinatorial Search and Heuristic Methods
algorist.backtrack

- backtrack.py --- a generic implementation of backtracking
- subsets.py --- construct all subsets via backtracking
- permutations.py --- construct all permutations via backtracking
- paths.py --- Enumerate the paths in a graph via backtracking
- sudoku.py --- A backtracking program to solve Seduku
- nqueens.py --- solve the eight queens problem using backtracking
- tsp.py --- Heuristics for solving TSP
- annealing.py --- a fairly generic implementation of simulated annealing

Chapter 8. Dynamic Programming
algorist.dp

- fib.py --- Compute the binomial coefficients using dynamic programming
- binomial.py --- compute the binomial coefficients using dynamic programming
- stringedit.py --- compute the optimal alignment matching two strings
- substringedit.py --- approximately match one string as a substring of another
- lcs.py --- longest common subsequence of two strings
- editdistance_cell.py
- editdistance.py--- a generic implementation of string comparison via dp
- editbrute.py --- compute string edit distance *without* dynamic programming
- partition.py --- Optimally balance partitions using dynamic programming
- elevator.py --- elevator stop optimization via dynamic programming

Chapter 13. Numerical Problems
algorist.numerical

- gcd.py --- compute the greatest common divisor of two integers
- primes.py --- compute the prime factorization of an integer
- bignum.py --- implementation of large integer arithmetic
- matrix.py --- Multiply two matrices.

Chapter 17. Computational Geometry
algorist.geometry

- distance.py --- compute Euclidian distances
- geometry.py --- basic geometric primitives and data types
- geotest.py --- driver program for geometry routines
- cgtest.py  --- driver program for computational geometry routines
- convex_hull.py --- compute convex hulls of points in the plane
- order.py --- demonstrate traversal orders on a grid
- superman.py --- compute Superman's flight path -- geometry example
- triangulate.py --- triangulate a polygon via ear-clipping, and compute area
- plates.py --- compute the number of circles in two different packings

Chapter 18. Set and String Problems
algorist.string

- name.py --- corporate name changing program -- string example

Project setup
1. Check out source code

2. Create Python virtual environment
https://docs.python.org/3/tutorial/venv.html
python3 -m venv ~/venv
source ~/venv/bin/activate

Install required Python pacakges
pip install -r requirements.txt
make

3. Setup in IntelliJ
Install Python Community Edition Plugin
File / Project Structure...
Create new Python SDK pointing to existing virtual environment in ~/venv