# K-Means & Maximin Pattern Recognition

A Python-based educational implementation of two foundational clustering algorithms for pattern recognition: **K-Means** and **Maximin**. The project provides an interactive command-line interface for generating synthetic 2D datasets, executing clustering routines, and visualizing results with iterative convergence tracking.

---

## 📋 Features

- **Interactive CLI**: Configurable dataset size and cluster parameters via standard input.
- **K-Means Clustering**: Fixed `k` implementation with convergence detection and first/final iteration visualization.
- **Maximin Algorithm**: Dynamic cluster determination based on inter-point and inter-centroid distance thresholds.
- **Vectorized Computation**: Optimized distance calculations using `numpy` broadcasting.
- **Visualization**: Matplotlib scatter plots with cluster coloring, centroid markers, and descriptive titles.
- **Educational Focus**: Designed for laboratory exercises in pattern recognition and unsupervised learning.

---

## 🛠️ Prerequisites & Installation

### Requirements
- Python 3.8 or higher
- `numpy`
- `matplotlib`

### Setup
```bash
# Clone or navigate to the project directory
cd k-means-pattern-recognition

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the desired algorithm from the terminal and follow the interactive prompts.

### K-Means (`main.py`)
```bash
python main.py
```
**Prompts:**
1. `Введите количество образов (от 1000 до 100000):` → Number of data points.
2. `Введите количество классов (от 2 до 20):` → Target number of clusters (`k`).

**Output:**
- Displays a plot of the first iteration.
- Runs until centroid convergence (`np.allclose`).
- Displays a final plot with converged clusters and centroids.

### Maximin (`main2.py`)
```bash
python main2.py
```
**Prompts:**
1. `Введите количество образов (1000 - 100000):` → Number of data points.

**Output:**
- Automatically determines the optimal number of clusters based on distance thresholds.
- Logs each newly discovered centroid.
- Displays a final plot with all identified clusters and centroids.

---

## 📁 Project Structure

```
k-means-pattern-recognition/
├── .aiignore          # AI tool exclusion rules
├── .gitignore         # Git exclusion rules
├── .vscode/
│   └── settings.json  # Editor configuration
├── main.py            # K-Means implementation & visualization
├── main2.py           # Maximin implementation & visualization
└── requirements.txt   # Python dependencies
```

---

## 🧠 Algorithm Implementation Details

### K-Means (`main.py`)
1. **Initialization**: Randomly selects `k` data points as initial centroids.
2. **Assignment**: Computes Euclidean distances from all points to all centroids using vectorized broadcasting. Assigns each point to the nearest centroid.
3. **Update**: Recomputes centroids as the mean of assigned points.
4. **Convergence**: Repeats assignment and update steps until centroid positions stabilize (`np.allclose`).
5. **Visualization**: Plots cluster assignments at iteration 1 and upon convergence.

### Maximin (`main2.py`)
1. **Initialization**: Selects one random point as the first centroid. The second centroid is the point farthest from the first.
2. **Distance Evaluation**: For each iteration, computes the minimum distance from every point to its nearest centroid.
3. **Candidate Selection**: Identifies the point with the maximum of these minimum distances.
4. **Threshold Check**: Compares this maximum distance to half the average pairwise distance between existing centroids.
5. **Termination**: If the threshold is exceeded, the candidate becomes a new centroid. Otherwise, the algorithm halts.
6. **Visualization**: Renders the final partitioning with dynamically determined clusters.

---

## ⚠️ Notes & Limitations

- **Data Generation**: Both scripts generate synthetic 2D data uniformly distributed in `[0, 1] × [0, 1]`. Real-world dataset integration requires modifying the data loading step.
- **Language**: CLI prompts and plot titles are in Russian to align with the original laboratory exercise context.
- **Performance**: Vectorized operations ensure efficient execution for up to 100,000 points. Memory usage scales with `O(n × k)` for distance matrices.
- **Determinism**: Results vary between runs due to random initialization. Set `np.random.seed()` for reproducible outputs.

---

## 📄 License

This project is provided for educational and research purposes. Modify and distribute as needed under your preferred open-source license.