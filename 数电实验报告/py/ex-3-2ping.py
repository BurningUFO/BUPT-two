import numpy as np
import matplotlib.pyplot as plt

# ---------------------- 参数设置 ----------------------
# 基本参数（调整后幅值：波2从1→1.5）
fs = 100e3       # 100kHz (周期 T=10μs)
fm = 1e6         # 1MHz (周期 T=1μs)
A1, A2, A3 = 2.0, 1.5, 1.0  # 幅值（波2调整为1.5）

# 延迟设置（波峰相对第一个波的延迟，负号表示提前）
delay12 = -480e-9  # 波2比波1提前480ns (-0.48μs)
delay13 = -20e-9   # 波3比波1提前20ns (-0.02μs)

# 时间轴：显示一个100kHz周期（10μs），以波1峰值为原点
t_start = 0           # 起始时间0μs（波1波峰）
t_end = 1/fs          # 结束时间10μs（一个完整周期）
t = np.linspace(t_start, t_end, 2000)  # 高密度采样（2000点）

# ---------------------- 生成方波（水平/垂直段分离） ----------------------
def generate_wave_segments(freq, amp, delay, t):
    """生成方波的水平段（粗线）和垂直段（细线）坐标"""
    period = 1/freq          # 周期
    half_period = period/2   # 半周期（跳变间隔）
    
    # 计算所有跳变时间点（上升沿/下降沿）：t_jump = delay + n*half_period
    n_min = int(np.floor((t.min() - delay)/half_period)) - 1
    n_max = int(np.ceil((t.max() - delay)/half_period)) + 1
    jump_times = [delay + n*half_period for n in range(n_min, n_max+1)]
    jump_times = [tj for tj in jump_times if t.min() <= tj <= t.max()]  # 筛选有效跳变点
    jump_times.sort()
    
    segments = {"horizontal": [], "vertical": []}  # 存储线段（水平：(x0,x1,y,线宽)；垂直：(x,y0,y1,线宽)）
    current_level = amp  # 初始电平（波峰开始，高电平=幅值）
    
    # 遍历跳变点生成线段
    for i, tj in enumerate(jump_times):
        # 水平段：上一个跳变点→当前跳变点（电平不变）
        t_start_seg = tj if i == 0 else jump_times[i-1]
        segments["horizontal"].append((t_start_seg, tj, current_level, 3.0))  # 水平线粗3pt
        
        # 垂直段：跳变点处电平切换（高→低或低→高）
        new_level = 0 if current_level == amp else amp  # 50%占空比
        segments["vertical"].append((tj, current_level, new_level, 0.5))  # 竖直线细0.5pt
        
        current_level = new_level  # 更新当前电平
    
    # 最后一个区间（最后跳变点→时间轴终点）
    segments["horizontal"].append((jump_times[-1], t.max(), current_level, 3.0))
    
    return segments

# 生成三个波的线段数据（统一实线）
wave1_segs = generate_wave_segments(fs, A1, 0, t)          # 波1：100kHz/2.0V，无延迟
wave2_segs = generate_wave_segments(fs, A2, delay12, t)    # 波2：100kHz/1.5V，提前480ns
wave3_segs = generate_wave_segments(fm, A3, delay13, t)    # 波3：1MHz/1.0V，提前20ns

# ---------------------- 绘图 ----------------------
plt.figure(figsize=(12, 6), dpi=100)

# 绘制波1（红色实线，水平粗3pt，垂直细0.5pt）
for x0, x1, y, lw in wave1_segs["horizontal"]:
    plt.hlines(y, x0, x1, color='red', linewidth=lw, label='100kHz, Amp=2.0V' if x0==wave1_segs["horizontal"][0][0] else "")
for x, y0, y1, lw in wave1_segs["vertical"]:
    plt.vlines(x, y0, y1, color='red', linewidth=lw)

# 绘制波2（绿色实线，幅值1.5V）
for x0, x1, y, lw in wave2_segs["horizontal"]:
    plt.hlines(y, x0, x1, color='green', linewidth=lw, label='100kHz, Amp=1.5V' if x0==wave2_segs["horizontal"][0][0] else "")
for x, y0, y1, lw in wave2_segs["vertical"]:
    plt.vlines(x, y0, y1, color='green', linewidth=lw)

# 绘制波3（蓝色实线，1MHz/1.0V）
for x0, x1, y, lw in wave3_segs["horizontal"]:
    plt.hlines(y, x0, x1, color='blue', linewidth=lw, label='1MHz, Amp=1.0V' if x0==wave3_segs["horizontal"][0][0] else "")
for x, y0, y1, lw in wave3_segs["vertical"]:
    plt.vlines(x, y0, y1, color='blue', linewidth=lw)

# ---------------------- 图形美化 ----------------------
plt.title('One-Cycle Square Waves (Thick Horizontal, Thin Vertical Lines)', fontsize=14)
plt.xlabel('Time (μs)', fontsize=12)  # x轴单位μs
plt.ylabel('Amplitude (Volts)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)  # 基础网格

# 图例去重（仅保留首次出现的标签）
handles, labels = plt.gca().get_legend_handles_labels()
unique = [(h, l) for i, (h, l) in enumerate(zip(handles, labels)) if l not in labels[:i]]
plt.legend([u[0] for u in unique], [u[1] for u in unique], loc='upper right', fontsize=10)

# 坐标轴范围（聚焦一个周期）
plt.xlim(t_start, t_end)
plt.ylim(-0.2, max(A1, A2, A3)+0.3)  # 留少许余量

# 时间轴刻度优化（显示μs刻度）
ax = plt.gca()
ax.xaxis.set_major_locator(plt.MultipleLocator(2))  # 主刻度2μs
ax.xaxis.set_minor_locator(plt.MultipleLocator(1))  # 次刻度1μs
ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))  # 幅值刻度0.5V

# 添加周期标记
plt.axvline(x=0, color='black', linestyle='-', alpha=0.2)
plt.axvline(x=5, color='black', linestyle='-', alpha=0.2)
plt.axvline(x=10, color='black', linestyle='-', alpha=0.2)
plt.text(5, max(A1, A2, A3)+0.1, 'Half Period', ha='center', fontsize=9)
plt.text(10, max(A1, A2, A3)+0.1, 'Full Period (10μs)', ha='center', fontsize=9)

plt.tight_layout()
plt.show()