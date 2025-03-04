import matplotlib.pyplot as plt
import numpy as np
import json
import os

# Function to load JSON data
# Here I've reduced the repetitive file opening
def load_json(directory, iterations=3):
    data = []
    for i in range(1, iterations + 1):
        file_path = os.path.join(directory, f'1-topic-16-partitions-1kb-Kafka-iter-{i}.json')
        with open(file_path) as f:
            data.append(json.load(f))
    return data

# Load data
data_sub = load_json('stretch-submariner')
data_cil = load_json('stretch-cilium')
data_normal = load_json('non-stretch')

fig, axs = plt.subplots(2, 2)

# Function to plot quantiles
def plotQuantiles(json_key, plot_x, plot_y, title, x_label, y_label):
    colors = {'Submariner': 'red', 'Cilium': 'blue', 'Non Stretch': 'green'}
    datasets = [(data_sub, 'Submariner'), (data_cil, 'Cilium'), (data_normal, 'Non Stretch')]

    # it's always better to use loops for cleaner and more readable plotting logic
    # So try this and see if this works, it should
    for dataset, label in datasets:
        for data in dataset:
            x = [float(k) for k in data[json_key].keys()]
            y = list(data[json_key].values())
            axs[plot_x, plot_y].plot(x, y, label=label if dataset.index(data) == 0 else "", color=colors[label])

    axs[plot_x, plot_y].legend()
    axs[plot_x, plot_y].set_title(title)
    axs[plot_x, plot_y].set_xlabel(x_label)
    axs[plot_x, plot_y].set_ylabel(y_label)

# Function to plot bar chart
def plotBar(json_key, plot_x, plot_y, title, x_label, y_label):
    colors = ['red', 'blue', 'green']
    labels = ['Submariner', 'Cilium', 'Non Stretch']
    datasets = [data_sub, data_cil, data_normal]

    means = [[np.mean(data[json_key]) for data in dataset] for dataset in datasets]

    for i, (label, color) in enumerate(zip(labels, colors)):
        axs[plot_x, plot_y].bar([f"{label} {j+1}" for j in range(3)], means[i], color=color)

    axs[plot_x, plot_y].set_title(title)
    axs[plot_x, plot_y].set_xlabel(x_label)
    axs[plot_x, plot_y].set_ylabel(y_label)

# Generate plots
plotQuantiles('aggregatedEndToEndLatencyQuantiles', 0, 0, 'Aggregated End To End Latency', 'Benchmark Progress Percentile', 'Latency (ms)')
plotQuantiles('aggregatedPublishLatencyQuantiles', 0, 1, 'Aggregated Publish Latency', 'Benchmark Progress Percentile', 'Latency (ms)')
plotBar('publishRate', 1, 0, 'Average Publish Rate', 'Network Technology', 'Number of Messages')
plotBar('consumeRate', 1, 1, 'Average Consume Rate', 'Network Technology', 'Number of Messages')

plt.show()
