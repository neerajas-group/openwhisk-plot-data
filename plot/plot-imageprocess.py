import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../data/image-process.csv')
print(df.to_string())
print(len(df))

df_16_cores = df[df['cpu_lim'] == 16]
df_80_cores = df[df['cpu_lim'] == 80]
df_img_size_largest = df[df['data_size'] == '4.6M']
x_order = ['12K', '80K', '184K', '244K', '384K', '440K', '608K', '756K', '860K', '928K', '1.2M', '2.4M', '3.4M', '4.6M']

# Plot input function size vs. execution time (constant: 16 cores)
fig, ax = plt.subplots(figsize=(7,5))
sns.boxplot(ax=ax, data=df_16_cores, x='data_size', y='exec_time', order=x_order)
ax.set_xlabel("Image Size")
ax.set_ylabel("Execution Time (s)")
plt.xticks(rotation=45)
plt.savefig("../graphs-cpu/imageprocess-size-exectime.png", dpi=300, bbox_inches='tight')

# Plot input function size vs. memory utilization (constant: 16 cores)
fig, ax = plt.subplots(figsize=(7,5))
sns.barplot(ax=ax, data=df_16_cores, x='data_size', y='mem_util', order=x_order)
ax.set_xlabel("Image Size")
ax.set_ylabel("Mem Utilization (%)")
plt.xticks(rotation=45)
plt.savefig("../graphs-cpu/imageprocess-size-memutil.png", dpi=300, bbox_inches='tight')

# Plot CPU count vs. exeuction time (constant: input image size of 4.6MB)
fig, ax = plt.subplots(figsize=(7,5))
sns.boxplot(ax=ax, data=df_img_size_largest, x='cpu_lim', y='exec_time')
ax.set_xlabel("Number of Logical CPUs")
ax.set_ylabel("Execution Time (s)")
plt.savefig("../graphs-cpu/imageprocess-cpucount-exec.png", dpi=300, bbox_inches='tight')

# Plot image size vs. cpu utilization (constant: 80 cores)
fig, ax = plt.subplots(figsize=(7,5))
graph = sns.boxplot(ax=ax, data=df_80_cores, x='data_size', y='cpu_util', order=x_order)
graph.axhline(8000)
graph.set_xlabel("Image Size")
plt.xticks(rotation=45)
graph.set_ylabel("CPU Utilization (%)")
plt.savefig("../graphs-cpu/imageprocess-size-cpuutil.png", dpi=300, bbox_inches='tight')