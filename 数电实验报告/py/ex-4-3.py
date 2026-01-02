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
num_pulses = 12  # 显示12个CLK_in脉冲
total_time = num_pulses * T_in
points_per_pulse = 200
num_points = points_per_pulse * num_pulses

t = np.linspace(0, total_time, num_points, endpoint=False)

# --- 2. 生成 CLK_in 信号 ---
# 外部输入时钟 (共同时钟)
CLK_in = (t % T_in) < (T_in / 2)
CLK_in = CLK_in.astype(int)

# 找到 CLK_in 的下降沿的时间索引 (同步触发点)
clk_in_down_edges_idx = np.where(np.diff(CLK_in) < 0)[0] + 1

# --- 3. 定义各级时钟 ---
# 在同步计数器中，所有时钟都是相同的
CLK = {
    0: CLK_in,  # CLK0 = CLK_in (驱动 FF0)
    1: CLK_in,  # CLK1 = CLK_in (驱动 FF1)
    2: CLK_in,  # CLK2 = CLK_in (驱动 FF2)
    3: CLK_in   # CLK3 = CLK_in (驱动 FF3)
}

# --- 4. 绘图 ---

fig, axes = plt.subplots(4, 1, figsize=(12, 8), sharex=True)
plt.suptitle('同步模十计数器 各级时钟 (CLK) 波形图', fontsize=16)

# 信号标签
signals = ['$CLK_0$', '$CLK_1$', '$CLK_2$', '$CLK_3$']
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
    
    # 标记下降沿 (即同步触发的有效沿)
    for edge_idx in clk_in_down_edges_idx:
        ax.axvline(t[edge_idx], color='gray', linestyle=':', alpha=0.5)

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