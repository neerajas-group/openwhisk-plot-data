import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../data/matmult.csv')
print(df.to_string())
print(len(df))

df_16_cores = df[df['cpu_lim'] == 16]
df_80_cores = df[df['cpu_lim'] == 80]
df_mat_size_8000 = df[df['data_size'] == 8000]

# Plot input function size vs. execution time (constant: 16 cores)
fig, ax = plt.subplots(figsize=(7,5))
sns.boxplot(ax=ax, data=df_16_cores, x='data_size', y='exec_time')
ax.set_xlabel("Matrix Size")
ax.set_ylabel("Execution Time (s)")
plt.savefig("../graphs-cpu/matmult-size-exectime.png", dpi=300, bbox_inches='tight')

# Plot input function size vs. memory utilization (constant: 16 cores)
fig, ax = plt.subplots(figsize=(7,5))
sns.barplot(ax=ax, data=df_80_cores, x='data_size', y='mem_util')
ax.set_xlabel("Matrix Size")
ax.set_ylabel("Mem Utilization (%)")
plt.savefig("../graphs-cpu/matmult-size-memutil.png", dpi=300, bbox_inches='tight')

# Plot CPU count vs. exeuction time (constant: input matrix size of 8000)
fig, ax = plt.subplots(figsize=(7,5))
sns.boxplot(ax=ax, data=df_mat_size_8000, x='cpu_lim', y='exec_time')
ax.set_xlabel("Number of Logical CPUs")
ax.set_ylabel("Execution Time (s)")
plt.savefig("../graphs-cpu/matmult-cpucount-exec.png", dpi=300, bbox_inches='tight')

# Plot matrix size vs. cpu utilization (constant: 80 cores)
fig, ax = plt.subplots(figsize=(7,5))
graph = sns.boxplot(ax=ax, data=df_80_cores, x='data_size', y='cpu_util')
graph.axhline(8000)
graph.set_xlabel("Matrix Size")
graph.set_ylabel("CPU Utilization (%)")
plt.savefig("../graphs-cpu/matmult-size-cpuutil.png", dpi=300, bbox_inches='tight')
