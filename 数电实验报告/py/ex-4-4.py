import numpy as np
import matplotlib.pyplot as plt

# >>> 【解决中文乱码的关键代码】 <<<
# 检查您的系统是否有以下字体，通常都有：
# Windows: 'SimHei' (黑体) 或 'Microsoft YaHei' (微软雅黑)
# macOS/Linux: 'Heiti TC' (黑体) 或 'PingFang HK' (苹果苹方)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
plt.rcParams['axes.unicode_minus'] = False     # 解决负号 '-' 显示为方块的问题


# --- 1. 定义参数和时间轴 ---
T_in = 1  # 输入时钟周期
num_pulses = 10  # 显示 10 个脉冲，展示 3->9->3->4 的完整循环
total_time = num_pulses * T_in
points_per_pulse = 500  # 增加采样点，确保捕捉到变化
num_points = points_per_pulse * num_pulses

t = np.linspace(0, total_time, num_points, endpoint=False)

# --- 2. 生成 CLK_in 和 Q 信号 ---

# CLK_in (同步时钟，下降沿触发)
CLK_in = (t % T_in) < (T_in / 2)
CLK_in = CLK_in.astype(int)

# 找到 CLK_in 的下降沿的时间索引
clk_down_edges_idx = np.where(np.diff(CLK_in) < 0)[0] + 1

# Q 信号和当前状态 (QA, QB, QC, QD)
Q_waves = {i: np.zeros_like(t) for i in range(4)} 
current_Q_states = [1, 1, 0, 0] # Q_A=1, Q_B=1, Q_C=0, Q_D=0 (即 0011)

# Load Data (QA, QB, QC, QD = 1, 1, 0, 0)
LOAD_DATA = [1, 1, 0, 0]

# --- 3. 模拟计数器逻辑 (关键修正部分) ---
LD_bar_wave = np.ones_like(t) # 默认高电平 (不加载)
count_idx = 0

for i in range(1, num_points):
    # 1. LD_bar 逻辑: 检测 1001 (Q_D=1, Q_A=1, Q_C=0, Q_B=0)
    QD_current, QC_current, QB_current, QA_current = current_Q_states[3], current_Q_states[2], current_Q_states[1], current_Q_states[0]
    
    # 假设精确检测 1001
    is_detect_1001 = (QD_current == 1 and QC_current == 0 and QB_current == 0 and QA_current == 1)
    
    if is_detect_1001:
        LD_bar_wave[i] = 0 # 满足条件，LD_bar 拉低
    else:
        LD_bar_wave[i] = 1 # 否则，保持高电平

    # 2. 将当前状态写入波形数组 (波形保持到下一个 CLK 沿)
    for j in range(4):
        Q_waves[j][i] = current_Q_states[j]
    
    # 3. 检查是否是 CLK_in 的下降沿 (同步触发)
    if CLK_in[i-1] == 1 and CLK_in[i] == 0:
        
        # --- 读取时钟沿前的 LD 状态 ---
        LD_bar_before_edge = LD_bar_wave[i-1]
        
        if LD_bar_before_edge == 0:
            # 动作 A: LD=0 激活，强制加载 LOAD_DATA (0011)
            current_Q_states = LOAD_DATA[:]
        else:
            # 动作 B: LD=1，正常计数
            
            # 计算 Dn, Cn, Bn, An 状态，这在 74LS162 中是内部逻辑
            # 由于是同步计数器，我们直接应用 Q(n+1) = Q(n) + 1 逻辑
            
            # 将当前 Q_A, Q_B, Q_C, Q_D 组合成十进制数
            decimal_val = QD_current * 8 + QC_current * 4 + QB_current * 2 + QA_current * 1
            
            # 正常 BCD 计数 (0-9 循环)
            new_val = (decimal_val + 1) % 10 # 162是BCD计数器，到9后自然变0，但这里被LD截断
            
            # 更新 Q 状态
            current_Q_states[0] = (new_val >> 0) & 1 # QA
            current_Q_states[1] = (new_val >> 1) & 1 # QB
            current_Q_states[2] = (new_val >> 2) & 1 # QC
            current_Q_states[3] = (new_val >> 3) & 1 # QD
            
            # 修正：当LD被拉低时，新状态已经写入LOAD_DATA，无需再执行计数逻辑
            # 上面的 decimal_val+1 逻辑只在 LD=1 时执行

# --- 4. 绘图 (与上次相同，但数据已修正) ---

fig, axes = plt.subplots(6, 1, figsize=(12, 12), sharex=True)
plt.suptitle('74LS162 模 7 计数器 (置位法：3 -> 9 -> 3) 波形图', fontsize=16)

# 注意 Q 信号的顺序是 Q_D, Q_C, Q_B, Q_A
waveforms = [CLK_in, LD_bar_wave, Q_waves[3], Q_waves[2], Q_waves[1], Q_waves[0]]
signals = ['$CLK_{in}$', '$\overline{LD}$', '$Q_D$ (MSB)', '$Q_C$', '$Q_B$', '$Q_A$ (LSB)']
colors = ['k', 'r', 'g', 'b', 'm', 'c']
y_offset = 0.5

for i, ax in enumerate(axes):
    sig = waveforms[i]
    label = signals[i]
    color = colors[i]

    ax.step(t, sig + y_offset, where='post', color=color, linewidth=2)

    ax.set_yticks([y_offset, 1 + y_offset])
    ax.set_yticklabels(['0', '1'])
    ax.set_ylabel(label, rotation=0, labelpad=30, fontsize=14)
    ax.set_ylim(0, 2)
    ax.grid(axis='x', linestyle='--', alpha=0.6)

    # 标记 CLK 下降沿
    for edge_idx in clk_down_edges_idx:
        ax.axvline(t[edge_idx], color='gray', linestyle=':', alpha=0.5)
    
    # 标出十进制状态
    if i == 5:
        # 获取每个时钟沿后的状态
        decimal_states = []
        for edge_idx in clk_down_edges_idx:
            if edge_idx < num_points:
                state = Q_waves[3][edge_idx] * 8 + Q_waves[2][edge_idx] * 4 + Q_waves[1][edge_idx] * 2 + Q_waves[0][edge_idx] * 1
                decimal_states.append(state)
        
        unique_states = [decimal_states[k] for k in range(min(len(decimal_states), num_pulses))]
        
        # 标注十进制计数
        for k in range(len(unique_states)):
            # 标注位置在当前时钟周期内
            ax.text(t[clk_down_edges_idx[k]] + T_in/2, 1.7, str(unique_states[k]), 
                    horizontalalignment='center', fontsize=10, color='darkred')
            
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