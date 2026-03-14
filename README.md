<div align="center">
   <h1>🔍 Graph Search Algorithms in Python</h1>
  
  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Algorithm-Graph_Search-orange?style=for-the-badge" />
    <img src="https://img.shields.io/badge/AI-Search-red?style=for-the-badge" />
  </p>

  <p>
    <strong>Implementation of BFS, DFS, and Best-First Search algorithms in Python</strong><br />
  </p>

  <p>
    <img src="https://img.shields.io/badge/Status-Active-success" />
    <img src="https://img.shields.io/badge/Version-1.0.0-blue" />
  </p>
</div>

---

## 🌟 Overview

> A collection of Python scripts implementing fundamental **graph search algorithms** used in Artificial Intelligence and route-finding problems.

This project covers three core search strategies — **uninformed** (BFS, DFS) and **informed** (Best-First Search) — applied to real-world city map traversal and abstract directed graph problems.

---

## ✨ Key Features

### 🔹 Core Algorithms
- 🗺️ **Breadth-First Search (BFS)** (Task 4a) — Finds the path with the fewest hops level by level
- 🌲 **Depth-First Search (DFS)** (Task 4b) — Explores deeply using recursion and backtracking
- 🎯 **Best-First Search** (Task 5) — Greedy heuristic-guided search toward the goal

### 🔹 Technical Highlights
- 📦 **FIFO Queue** in BFS for level-order traversal
- 🔁 **Recursive Stack** with backtracking in DFS
- 📊 **Heuristic Priority Queue** in Best-First Search
- 🗂️ **Graph as Dictionary** with weighted edges `(city, distance)`
- 📏 **Automatic Distance Calculation** along the discovered path

---

## 📋 Table of Contents
1. [Prerequisites](#-1-prerequisites)
2. [Installation](#-2-installation)
3. [Project Structure](#-3-project-structure)
4. [Script Breakdown](#-4-script-breakdown)
5. [Running the Scripts](#-5-running-the-scripts)
6. [Algorithm Comparison](#-6-algorithm-comparison)
7. [Output Results](#-7-output-results)
8. [Troubleshooting](#️-8-troubleshooting)
9. [Closing](#-9-closing)

---

## 🔧 1. Prerequisites

Make sure your development environment meets the following requirements:
- **Python** >= 3.8
- No external libraries required — uses only Python built-ins

---

## 📦 2. Installation

Clone the repository and navigate into the project folder:

```bash
git clone <repository-url>
cd <folder-name>
```

> No additional `pip` packages are needed. Python's standard library is sufficient.

---

## 📁 3. Project Structure

```
project/
├── soal-4/
│   ├── breadth-first-search.py    # Task 4a - BFS from Milan to Innsbruck
│   └── depth-first-search.py      # Task 4b - DFS from Milan to Innsbruck
├── soal-5/
│   └── best-first-search.py       # Task 5  - Best-First Search from A to H
└── README.md
```

### Architecture Layer Explanation

1. **soal-4/** → Search scripts applied to a geographic city map (Milan → Innsbruck)
2. **soal-5/** → Search script applied to an abstract directed weighted graph (A → H)

---

## 🔬 4. Script Breakdown

### Task 4a — Breadth-First Search (`breadth-first-search.py`)

Finds the route from Milan to Innsbruck by exploring all neighbors level by level. Guarantees the path with the **fewest stops (minimum hops)**, not necessarily the shortest distance.

**Techniques used:**
- FIFO queue (list with `pop(0)`) to process nodes in discovery order
- Full path stored in queue to trace the route without backtracking
- Visited list prevents revisiting nodes and infinite loops
- Post-search distance calculation by iterating through path pairs

```python
antrian = [[awal]]
while len(antrian) > 0:
    path_sekarang = antrian.pop(0)
    node_sekarang = path_sekarang[-1]
    for tetangga, jarak in graph[node_sekarang]:
        if tetangga not in sudah_dikunjungi:
            antrian.append(path_sekarang + [tetangga])
```

**Output:**

| Result | Description |
|--------|-------------|
| `Step-by-step log` | Each node visited and current path printed to console |
| `Route` | Final path from Milan to Innsbruck with minimum hops |
| `Total distance` | Cumulative km along the discovered route |

---

### Task 4b — Depth-First Search (`depth-first-search.py`)

Explores as deep as possible into the graph before backtracking. Implemented **recursively**. May not find the shortest path — result depends on graph neighbor ordering.

**Techniques used:**
- Recursive function with visited list and current path as mutable arguments
- Backtracking via `path.pop()` when a dead end is reached
- Global step counter as a list to allow mutation inside recursion
- Returns `True` immediately when goal is found, stopping further recursion

```python
def depth_first_search(graph, node_sekarang, tujuan, sudah_dikunjungi, path_sekarang):
    sudah_dikunjungi.append(node_sekarang)
    path_sekarang.append(node_sekarang)
    if node_sekarang == tujuan:
        return True
    for tetangga, jarak in graph[node_sekarang]:
        if tetangga not in sudah_dikunjungi:
            if depth_first_search(graph, tetangga, tujuan, sudah_dikunjungi, path_sekarang):
                return True
    path_sekarang.pop()  # Backtrack
    return False
```

**Output:**

| Result | Description |
|--------|-------------|
| `Step-by-step log` | Each visited node and path printed per recursive call |
| `Route` | First path found (not guaranteed shortest distance or hops) |
| `Total distance` | Cumulative km of the DFS-discovered route |

---

### Task 5 — Best-First Search (`best-first-search.py`)

Greedily selects the next node with the **lowest heuristic value** (estimated time to goal). Applied to an abstract directed graph (A → H) using a manually defined heuristic table.

**Techniques used:**
- Priority selection via custom `ambil_minimum()` — picks lowest h-value from queue
- Heuristic table maps every node to its estimated cost to reach goal H
- Visited list prevents reprocessing of already-explored nodes
- Directed graph — not all edges are bidirectional

```python
antrian = [(heuristik[awal], awal, [awal])]
while len(antrian) > 0:
    h_nilai, node_sekarang, path = ambil_minimum(antrian)
    if node_sekarang in sudah_dikunjungi:
        continue
    sudah_dikunjungi.append(node_sekarang)
    if node_sekarang == tujuan:
        # report and return
    for tetangga, bobot in graph[node_sekarang]:
        antrian.append((heuristik[tetangga], tetangga, path + [tetangga]))
```

**Heuristic Table (estimated minutes to H):**

| Node | h value | Interpretation |
|------|---------|----------------|
| `A` | 60 | Far from goal |
| `B` | 80 | Slightly farther (indirect path) |
| `C` | 20 | Close to goal |
| `D` | 25 | Close to goal |
| `E` | 70 | Far |
| `F` | 25 | Close to goal |
| `G` | 35 | Moderate |
| `H` | 0 | Goal node |

---

## 🚀 5. Running the Scripts

Run each script independently from the project root folder:

```bash
# Task 4a - Breadth-First Search
python soal-4/breadth-first-search.py

# Task 4b - Depth-First Search
python soal-4/depth-first-search.py

# Task 5 - Best-First Search
python soal-5/best-first-search.py
```

> ✅ **All three scripts are independent** — they can be run in any order.

---

## 📊 6. Algorithm Comparison

| Feature | BFS | DFS | Best-First Search |
|---------|-----|-----|-------------------|
| Data Structure | Queue (FIFO) | Stack (Recursion) | Priority Queue (min-h) |
| Completeness | Complete | Complete (finite graphs) | Complete (finite graphs) |
| Optimality | Optimal (min hops) | Not optimal | Not optimal (greedy) |
| Space Complexity | O(b^d) | O(d) | O(b^d) |
| Uses Heuristic? | No | No | Yes |
| Problem Applied | Milan → Innsbruck | Milan → Innsbruck | A → H |

---

## 📊 7. Output Results

### Expected Results

**Task 4a (BFS):**
- Visits nodes level by level from Milan outward
- Finds route with the **fewest intermediate cities**
- Prints total distance in km of the discovered path

**Task 4b (DFS):**
- Dives deep along the first available neighbor at each step
- May find a **longer route** than BFS (more km or more hops)
- Backtracks and prints path updates on each recursive call

**Task 5 (Best-First Search):**
- Jumps directly toward nodes with lower heuristic values
- May skip lower-cost edges in favor of greedy heuristic guidance
- Prints each step with the `h-value` of the node being visited

---

## 🛠️ 8. Troubleshooting

### Problem: `RecursionError` in DFS

Python's default recursion limit may be exceeded for large graphs.

**Solution:**
```python
import sys
sys.setrecursionlimit(10000)  # Add at the top of depth-first-search.py
```

---

### Problem: DFS produces a different/longer route than expected

DFS result depends on the **order of neighbors** in the graph dictionary. Reordering neighbors will change which path is discovered first.

**Solution:**
This is expected behavior. DFS is not guaranteed to find the optimal path.

---

### Problem: Best-First Search does not find the shortest distance

Best-First Search is a **greedy algorithm** — it optimizes for heuristic value, not actual path cost.

**Solution:**
If you need the distance-optimal path, use **Dijkstra's Algorithm** or **A\* Search** instead.

---

### Problem: `SyntaxError` when running the script

Ensure you are using Python 3.8 or above. Python 2 is not supported.

**Solution:**
```bash
python --version  # Should show Python 3.8 or higher
```

---

## 📧 9. Closing

This project demonstrates three foundational search algorithms used in Artificial Intelligence — from uninformed strategies (BFS, DFS) to informed heuristic-based approaches (Best-First Search). These algorithms form the basis of modern pathfinding, planning, and reasoning systems used in robotics, game AI, and navigation software.

---
