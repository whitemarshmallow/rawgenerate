import numpy as np
import pandas as pd

# 加载 .npy 文件
data = np.load('UMA4R32T10P.npy')  # 形状：(100, 20, 2, 32, 4, 8)

data = data[:1000]

num_users = data.shape[0]

# 创建CSV文件并写入表头
with open('CSI_data.csv', 'w') as f:
    f.write('User_ID,Time_TTI,Tx_Antenna,Rx_Antenna,Resource_Block,CSI_Real,CSI_Imag\n')

# 分批处理每个用户的数据
for user_id in range(num_users):
    print(f"正在处理用户 {user_id + 1}/{num_users}")
    user_data = data[user_id]  # 形状：(20, 2, 32, 4, 8)

    # 获取维度信息
    num_time, num_parts, num_tx, num_rx, num_rb = user_data.shape

    # 创建索引数组
    Time_TTI = np.arange(num_time)
    Tx_Antenna = np.arange(num_tx)
    Rx_Antenna = np.arange(num_rx)
    Resource_Block = np.arange(num_rb)

    # 使用 np.meshgrid 生成索引组合
    Time_TTI_grid, Tx_Antenna_grid, Rx_Antenna_grid, Resource_Block_grid = np.meshgrid(
        Time_TTI, Tx_Antenna, Rx_Antenna, Resource_Block, indexing='ij'
    )

    # print("Time_TTI_grid的样子是"+Time_TTI_grid)

    # 展开索引为一维数组
    Time_TTI_flat = Time_TTI_grid.ravel()
    Tx_Antenna_flat = Tx_Antenna_grid.ravel()
    Rx_Antenna_flat = Rx_Antenna_grid.ravel()
    Resource_Block_flat = Resource_Block_grid.ravel()

    # 提取实部和虚部并展开
    CSI_Real = user_data[:, 0, :, :, :].ravel()
    CSI_Imag = user_data[:, 1, :, :, :].ravel()

    # 创建DataFrame
    df_user = pd.DataFrame({
        'User_ID': user_id,
        'Time_TTI': Time_TTI_flat,
        'Tx_Antenna': Tx_Antenna_flat,
        'Rx_Antenna': Rx_Antenna_flat,
        'Resource_Block': Resource_Block_flat,
        'CSI_Real': CSI_Real,
        'CSI_Imag': CSI_Imag
    })

    # 将数据追加到CSV文件
    df_user.to_csv('CSI_data.csv', mode='a', header=False, index=False)
