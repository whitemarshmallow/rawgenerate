import numpy as np
import matplotlib.pyplot as plt

# 加载数据并提取前100个UE的第一个样本作为示例
data = np.load('UMA4R32T10P.npy')
sample_data = np.abs(data[0, :, 0, :, :, 0])  # 提取第一个UE、时间上所有TTI、实部、发射和接收天线、首个RB的幅度

# 绘制热力图
plt.figure(figsize=(10, 6))
plt.imshow(sample_data, aspect='auto', cmap='viridis')
plt.colorbar(label='Amplitude')
plt.xlabel('Rx Antenna Index')
plt.ylabel('Tx Antenna Index')
plt.title('CSI Amplitude Heatmap for a Sample UE')
plt.show()