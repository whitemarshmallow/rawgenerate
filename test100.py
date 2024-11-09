import numpy as np

# 加载原始 .npy 文件
data = np.load('UMA4R32T10P.npy')

# 提取前100个UE的数据
subset_data = data[:100]

print(subset_data.shape)
print(subset_data)

# # 将提取的数据保存为新的 .npy 文件
# np.save('UMA4R32T10P_subset.npy', subset_data)
#
# print("新的文件 UMA4R32T10P_subset.npy 已保存，包含前100个UE的数据。")
