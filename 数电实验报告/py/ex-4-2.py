import numpy as np
import matplotlib.pyplot as plt

# >>> 【解决中文乱码的关键代码】 <<<
# 检查您的系统是否有以下字体，通常都有：
# Windows: 'SimHei' (黑体) 或 'Microsoft YaHei' (微软雅黑)
# macOS/Linux: 'Heiti TC' (黑体) 或 'PingFang HK' (苹果苹方)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
plt.rcParams['axes.unicode_minus'] = False     # 解决负号 '-' 显示为方块的问题

# --- 1. 定义参数和时间轴 (与上次相同) ---
T_in = 1  # 输入时钟周期
num_pulses = 16  # 完整的计数周期需要16个CLK_in脉冲
total_time = num_pulses * T_in  # 总时长
points_per_pulse = 200  # 每个脉冲周期内的采样点数
num_points = points_per_pulse * num_pulses

t = np.linspace(0, total_time, num_points, endpoint=False)
dt = t[1] - t[0]

# --- 2. 生成 Q 信号 (即 CLK 信号) ---

# 初始化所有信号数组
CLK_in = np.zeros_like(t)
Q = {i: np.zeros_like(t) for i in range(4)}  # Q0, Q1, Q2, Q3

# 模拟 CLK_in (方波，周期 T_in)
CLK_in = (t % T_in) < (T_in / 2)
CLK_in = CLK_in.astype(int)

# 模拟计数器翻转逻辑 (下降沿触发)
q_state = [0, 0, 0, 0]  # Q0, Q1, Q2, Q3 初始状态 0000

for i in range(1, num_points):
    # CLK_0 (CLK_in) 下降沿
    if CLK_in[i-1] == 1 and CLK_in[i] == 0:
        q_state[0] = 1 - q_state[0]
        
        # CLK_1 (Q0) 下降沿
        if q_state[0] == 0:  
            q_state[1] = 1 - q_state[1]
            
            # CLK_2 (Q1) 下降沿
            if q_state[1] == 0:  
                q_state[2] = 1 - q_state[2]
                
                # CLK_3 (Q2) 下降沿
                if q_state[2] == 0: 
                    q_state[3] = 1 - q_state[3]
    
    # 将当前状态记录到波形数组中
    for j in range(4):
        Q[j][i] = q_state[j]

# 根据级联关系定义 CLK_n
CLK = {
    0: CLK_in,  # CLK0 = CLK_in
    1: Q[0],    # CLK1 = Q0
    2: Q[1],    # CLK2 = Q1
    3: Q[2]     # CLK3 = Q2
}

# --- 3. 绘图 ---

fig, axes = plt.subplots(4, 1, figsize=(12, 8), sharex=True)
plt.suptitle('4位异步计数器 各级时钟 (CLK) 波形图', fontsize=16)

# 信号标签
signals = ['$CLK_0$ (Input)', '$CLK_1$ ($Q_0$)', '$CLK_2$ ($Q_1$)', '$CLK_3$ ($Q_2$)']
colors = ['k', 'r', 'b', 'g']
y_offset = 0.5 

for i, ax in enumerate(axes):
    sig = CLK[i]
    label = signals[i]
    color = colors[i]
    
    # 绘制波形
    ax.step(t, sig + y_offset, where='post', color=color, linewidth=2)
    
    # 设置y轴标签和刻度
    ax.set_yticks([y_offset, 1 + y_offset])
    ax.set_yticklabels(['0', '1'])
    ax.set_ylabel(label, rotation=0, labelpad=30, fontsize=14)
    ax.set_ylim(0, 2)
    ax.grid(axis='x', linestyle='--', alpha=0.6)
    
    # 标记下降沿 (即下一级触发的有效沿)
    down_edges_idx = np.where(np.diff(sig) < 0)[0] + 1
    for edge_idx in down_edges_idx:
        ax.axvline(t[edge_idx], color=color, linestyle=':', alpha=0.3)

# 设置x轴
axes[-1].set_xlabel('时间 ($t$ / $T_{in}$)', fontsize=14)
axes[-1].set_xticks(np.arange(0, total_time + 1, T_in))
axes[-1].set_xticklabels(map(str, np.arange(0, num_pulses + 1)))
axes[-1].set_xlim(0, total_time)

# 隐藏不必要的y轴刻度
for ax in axes:
    ax.tick_params(axis='y', left=False, labelleft=True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95]) 
plt.show()