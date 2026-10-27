import matplotlib.pyplot as plt
import numpy as np

# Define workloads and algorithm results
workloads = ['lru_test', 'mru_test', 'mru_test2', 'rr_test', 'rr_test2', 'zipfian']

# Results in order: FIFO, LRU, MRU, Random
# Based on the provided data, I'll extract the values (removing the algorithm labels)
results = {
    'FIFO': [
        0.7901097545936614,   # lru_test
        0.4997953575396129,   # mru_test
        0.6665133923439476,   # mru_test2
        0.4546456967094191,   # rr_test
        0.4544920383101240,   # rr_test2
        0.3896985659935616    # zipfian
    ],
    'LRU': [
        0.9030730129390018,   # lru_test (marked LRU)
        0.5001811813020896,   # mru_test
        0.0003453436168988,   # mru_test2
        0.0001773678609436,   # rr_test
        0.0003463403371046,   # rr_test2
        0.4421638545834058    # zipfian (marked LRU)
    ],
    'MRU': [
        0.4537612146307798,   # lru_test
        0.9499254843517139,   # mru_test (marked MRU)
        0.8180821601661666,   # mru_test2 (marked MRU)
        0.0024572899602153,   # rr_test
        0.0028230312297830,   # rr_test2
        0.1633362293657689    # zipfian
    ],
    'Random': [
        0.7712195951692465,   # lru_test
        0.9120253536005634,   # mru_test
        0.6758520244683950,   # mru_test2
        0.5700783771323190,   # rr_test (marked RR)
        0.5704200700116686,   # rr_test2 (marked RR)
        0.3848411906299536    # zipfian
    ]
}

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Bar width and positions
x = np.arange(len(workloads))
width = 0.2

# Colors for each algorithm
colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']

# Create bars for each algorithm
bars = []
for i, (algo, values) in enumerate(results.items()):
    bar = ax.bar(x + i * width - 1.5 * width, values, width, label=algo, color=colors[i])
    bars.append(bar)
    
    # Add value labels on top of bars
    for j, v in enumerate(values):
        ax.text(x[j] + i * width - 1.5 * width, v + 0.01, f'{v:.3f}', 
                ha='center', va='bottom', fontsize=7, rotation=90)

# Customize the plot
ax.set_xlabel('Workload', fontsize=12, fontweight='bold')
ax.set_ylabel('Hit Rate', fontsize=12, fontweight='bold')
ax.set_title('Performance Comparison of Cache Replacement Algorithms\nAcross Different Workloads', 
             fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(workloads)
ax.set_ylim(0, 1.05)
ax.legend(title='Algorithm', loc='upper right', fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Highlight the best algorithm for each workload
for j, workload in enumerate(workloads):
    best_algo = None
    best_val = -1
    for algo, values in results.items():
        if values[j] > best_val:
            best_val = values[j]
            best_algo = algo
    # Add a star or annotation for the best performer
    algo_idx = list(results.keys()).index(best_algo)
    ax.annotate('★', xy=(x[j] + algo_idx * width - 1.5 * width, best_val), 
                xytext=(x[j] + algo_idx * width - 1.5 * width, best_val + 0.05),
                ha='center', fontsize=10, color='gold')

plt.tight_layout()

# Save the figure
plt.savefig('cache_algorithm_comparison.png', dpi=150, bbox_inches='tight')
plt.show()

# Print summary table
print("\n" + "="*90)
print("CACHE ALGORITHM PERFORMANCE SUMMARY (Hit Rate)")
print("="*90)
print(f"{'Workload':<15} {'FIFO':<12} {'LRU':<12} {'MRU':<12} {'Random':<12} {'Best':<10}")
print("-"*90)
for j, workload in enumerate(workloads):
    values = [results[algo][j] for algo in results]
    best_algo = list(results.keys())[values.index(max(values))]
    print(f"{workload:<15} {values[0]:<12.4f} {values[1]:<12.4f} {values[2]:<12.4f} {values[3]:<12.4f} {best_algo:<10}")
print("="*90)