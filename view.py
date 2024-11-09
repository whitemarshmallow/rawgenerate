import pandas as pd
import numpy as np

# 加载 .npy 文件
data = np.load('UMA4R32T10P.npy')

# 打印数据的形状和数据类型
print("Data shape:", data.shape)
print("Data dtype:", data.dtype)

# 打印数据的一部分，查看具体内容
print("Data sample (first elements):", data.flatten()[:10])


import numpy as np

# 加载 .npy 文件
data = np.load('UMA4R32T10P.npy')

# 打印整体数据的形状和数据类型
print("Data shape:", data.shape)
print("Data dtype:", data.dtype)

# 逐个维度打印特征
# 打印第一个维度（样本数 - UE编号）
print("\nFirst dimension (Sample/UE number):")
for i in range(2):  # 只打印前2个样本
    print(f"Sample {i}:", data[i].shape)

# 打印第二个维度（时间 - 20个TTI）
print("\nSecond dimension (Time - TTI):")
for i in range(2):  # 只打印第一个样本的前2个时间点
    print(f"Sample 0, TTI {i}:", data[0, i].shape)

# 打印第三个维度（实部和虚部）
print("\nThird dimension (Real & Imaginary parts):")
for i in range(2):  # 只打印第一个样本第一个TTI的2个复数部分
    print(f"Sample 0, TTI 0, Part {i}:", data[0, 0, i].shape)

# 打印第四个维度（发射天线 - 32个Tx）
print("\nFourth dimension (Tx Antennas):")
for i in range(2):  # 只打印第一个样本第一个TTI第一个复数部分的前2个发射天线
    print(f"Sample 0, TTI 0, Part 0, Tx Antenna {i}:", data[0, 0, 0, i].shape)

# 打印第五个维度（接收天线 - 4个Rx）
print("\nFifth dimension (Rx Antennas):")
for i in range(2):  # 只打印第一个样本第一个TTI第一个复数部分的第一个发射天线的前2个接收天线
    print(f"Sample 0, TTI 0, Part 0, Tx Antenna 0, Rx Antenna {i}:", data[0, 0, 0, 0, i].shape)

# 打印第六个维度（资源块 - 8个RB）
print("\nSixth dimension (Resource Blocks):")
for i in range(2):  # 只打印第一个样本第一个TTI第一个复数部分的第一个发射天线、第一个接收天线的前2个RB
    print(f"Sample 0, TTI 0, Part 0, Tx Antenna 0, Rx Antenna 0, RB {i}:", data[0, 0, 0, 0, 0, i])

# 打印部分数据内容
print("\nSample data content (First sample, TTI, Part, Tx, Rx, RB):")
print(data[0, 0, 0, 0, 0, :])  # 打印第一个样本的一个RB的数据



# # 将numpy数组转换为DataFrame
# df = pd.DataFrame(data)
#
# # 显示DataFrame的前几行以及列名
# print(df.head())
# print("Columns:", df.columns)