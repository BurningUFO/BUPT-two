import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
# >>> 【解决中文乱码的关键代码】 <<<
# 检查您的系统是否有以下字体，通常都有：
# Windows: 'SimHei' (黑体) 或 'Microsoft YaHei' (微软雅黑)
# macOS/Linux: 'Heiti TC' (黑体) 或 'PingFang HK' (苹果苹方)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
plt.rcParams['axes.unicode_minus'] = False     # 解决负号 '-' 显示为方块的问题

# --- 1. 定义波形参数 ---

# 第一个方波 (Wave 1)
f1 = 50e3      # 频率: 50 KHz
A1_peak = 2    # 峰值幅值: 2
T1 = 1 / f1    # 周期: 20 us
duty_cycle_1 = 0.5

# 第二个方波 (Wave 2)
f2 = 100e3     # 频率: 100 KHz
A2_peak = 1    # 峰值幅值: 1
T2 = 1 / f2    # 周期: 10 us
duty_cycle_2 = 0.5

# 延迟 (Delay)
delay = 5e-6   # 延迟: 5 us

# --- 2. 设定时间轴和采样点 ---

# 绘图时间范围: 3 个 Wave 1 周期
t_stop = 3 * T1
num_points = 5000
t = np.linspace(0, t_stop, num_points, endpoint=False)

# --- 3. 生成单极性方波数据 (关键修改部分) ---

# signal.square 生成的是 -1 到 +1 的方波
# 单极性转换公式: (A/2) * (signal.square(...) + 1)
# 这样波形就在 0 到 A 之间切换。

# Wave 1: 50KHz, 峰值幅值 2
# 原始范围: -1 到 +1, 乘以 A1_peak 得到 -2 到 +2
# 转换后范围: 0 到 +2
wave1_data_bipolar = signal.square(2 * np.pi * f1 * t, duty=duty_cycle_1)
wave1_data = (A1_peak / 2) * (wave1_data_bipolar + 1)

# Wave 2: 100KHz, 峰值幅值 1, 延迟 5us
# 原始范围: -1 到 +1, 乘以 A2_peak 得到 -1 到 +1
# 转换后范围: 0 到 +1
wave2_data_bipolar = signal.square(2 * np.pi * f2 * (t - delay), duty=duty_cycle_2)
wave2_data = (A2_peak / 2) * (wave2_data_bipolar + 1)

# --- 4. 绘制波形图 ---

plt.figure(figsize=(12, 6))

# Wave 1 绘制 (蓝色)
line1, = plt.plot(
    t * 1e6, # 转换为微秒 (us)
    wave1_data,
    color='blue',
    linewidth=1.5,
    linestyle='-',
    marker='.',
    markersize=1,
    label=f'方波 1: 频率={f1/1e3:.0f} KHz, 峰值={A1_peak}'
)

# Wave 2 绘制 (红色)
line2, = plt.plot(
    t * 1e6, # 转换为微秒 (us)
    wave2_data,
    color='red',
    linewidth=1.5,
    linestyle='-',
    marker='.',
    markersize=1,
    label=f'方波 2: 频率={f2/1e3:.0f} KHz, 峰值={A2_peak}'
)


# --- 5. 添加图示和注解 ---

plt.title('双通道单极性方波信号对比 (波谷在 Y=0)')
plt.xlabel('时间 ($\mu s$)')
plt.ylabel('幅值 (V)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(0, color='black', linewidth=1.0) # 绘制加粗的X轴 (即0轴)

# 增加延迟关系的注解
plt.text(
    0.2,
    2.2, # 调整 Y 轴位置以适应新的最大值
    f'延迟关系: 波峰到波峰延迟 $\\Delta t$ = {delay*1e6:.0f} $\\mu s$',
    fontsize=12,
    color='green',
    bbox=dict(facecolor='white', alpha=0.8, edgecolor='green', boxstyle='round,pad=0.5')
)

# 突出显示延迟 (波峰到波峰)
t1_peak = 0
t2_peak = delay * 1e6
plt.annotate(
    '',
    xy=(t1_peak, A1_peak),
    xytext=(t2_peak, A1_peak),
    arrowprops=dict(arrowstyle="<->", color='darkorange', linewidth=2)
)
plt.text(
    t1_peak + (t2_peak - t1_peak)/2, A1_peak + 0.05,
    f'{delay*1e6:.0f} $\\mu s$ 延迟',
    color='darkorange',
    horizontalalignment='center'
)

plt.legend(loc='upper right', fontsize=11)
plt.ylim(-0.1, A1_peak + 0.3) # 稍微调整Y轴范围，使其更美观
plt.tight_layout()
plt.show()