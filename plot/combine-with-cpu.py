import pandas as pd
import os

# df_matmult_mem = pd.read_csv("../data/matmult-data.csv")
# df_matmult_cpu = pd.read_csv("../data/matmult-cpu.csv")
# df_matmult = pd.merge(df_matmult_mem, df_matmult_cpu, on=['benchmark', 'cpu_lim', 'mem_lim', 'data_size', 'run_no'])
# df_matmult.to_csv("../data/matmult.csv", index=False)

# df_linpack_mem = pd.read_csv("../data/linpack-data.csv")
# df_linpack_cpu = pd.read_csv("../data/linpack-cpu.csv")
# df_linpack = pd.merge(df_linpack_mem, df_linpack_cpu, on=['benchmark', 'cpu_lim', 'mem_lim', 'data_size', 'run_no'])
# df_linpack.to_csv("../data/linpack.csv", index=False)

# df_encrypt_mem = pd.read_csv("../data/encrypt-data.csv")
# df_encrypt_cpu = pd.read_csv("../data/encrypt-cpu.csv")
# df_encrypt = pd.merge(df_encrypt_mem, df_encrypt_cpu, on=['benchmark', 'cpu_lim', 'mem_lim', 'data_size', 'run_no'])
# df_encrypt.to_csv("../data/encrypt.csv", index=False)

df_image_process_mem = pd.read_csv("../data/image-process-data.csv")
df_image_process_cpu = pd.read_csv("../data/image-process-cpu.csv")
df_image_process = pd.merge(df_image_process_mem, df_image_process_cpu, on=['benchmark', 'cpu_lim', 'mem_lim', 'data_size', 'run_no'])
print(df_image_process)
df_image_process.to_csv("../data/image-process.csv", index=False)