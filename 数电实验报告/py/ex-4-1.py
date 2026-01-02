import matplotlib.pyplot as plt
import numpy as np

# 设置绘图风格
plt.style.use('default')
fig, ax = plt.subplots(figsize=(12, 8))

# 定义时间轴 (0 到 16 个脉冲)
t = np.arange(0, 17, 0.01)

# 生成波形数据
# CP: 简单的方波，周期为1
cp = (t % 1) < 0.5
cp = cp.astype(float)

# 计数器逻辑模拟
# Q0: 每1个周期翻转一次 (频率是CP的一半)
q0 = (t.astype(int) % 2) == 1
# Q1: 每2个周期翻转一次
q1 = ((t.astype(int) // 2) % 2) == 1
# Q2: 每4个周期翻转一次
q2 = ((t.astype(int) // 4) % 2) == 1
# Q3: 每8个周期翻转一次
q3 = ((t.astype(int) // 8) % 2) == 1

# 转换为0/1数值用于绘图
q0 = q0.astype(float)
q1 = q1.astype(float)
q2 = q2.astype(float)
q3 = q3.astype(float)

# 设置Y轴偏移量，让波形垂直堆叠
# 从上到下: CP, Q0, Q1, Q2, Q3
offset_cp = 8
offset_q0 = 6
offset_q1 = 4
offset_q2 = 2
offset_q3 = 0

# 绘制波形 (使用step函数绘制数字信号)
ax.step(t, cp + offset_cp, where='post', color='gray', linewidth=1.5, alpha=0.6, label='CP')
ax.step(t, q0 + offset_q0, where='post', color='tab:blue', linewidth=2, label='Q0')
ax.step(t, q1 + offset_q1, where='post', color='tab:orange', linewidth=2, label='Q1')
ax.step(t, q2 + offset_q2, where='post', color='tab:green', linewidth=2, label='Q2')
ax.step(t, q3 + offset_q3, where='post', color='tab:red', linewidth=2, label='Q3')

# 添加文字标签
ax.text(-0.5, offset_cp + 0.5, 'CP', fontsize=12, fontweight='bold', color='gray')
ax.text(-0.5, offset_q0 + 0.5, 'Q0 (LSB)', fontsize=12, fontweight='bold', color='tab:blue')
ax.text(-0.5, offset_q1 + 0.5, 'Q1', fontsize=12, fontweight='bold', color='tab:orange')
ax.text(-0.5, offset_q2 + 0.5, 'Q2', fontsize=12, fontweight='bold', color='tab:green')
ax.text(-0.5, offset_q3 + 0.5, 'Q3 (MSB)', fontsize=12, fontweight='bold', color='tab:red')

# 添加触发关系箭头 (Ripple Effect)
# 寻找下降沿并绘制箭头
def add_arrow(x, y_start, y_end):
    ax.annotate('', xy=(x, y_end + 0.2), xytext=(x, y_start + 0.8),
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5, ls='--'))

# Q0 下降沿 -> 触发 Q1
for i in range(1, 17):
    if i % 2 == 0: # Q0 在偶数时刻下降
        add_arrow(i, offset_q0, offset_q1)

# Q1 下降沿 -> 触发 Q2
for i in range(1, 17):
    if i % 4 == 0: # Q1 在4的倍数时刻下降
        add_arrow(i, offset_q1, offset_q2)

# Q2 下降沿 -> 触发 Q3
for i in range(1, 17):
    if i % 8 == 0: # Q2 在8的倍数时刻下降
        add_arrow(i, offset_q2, offset_q3)

# 设置网格和坐标轴
ax.set_xlim(0, 16.5)
ax.set_ylim(-0.5, 10)
ax.set_xticks(range(17))
ax.set_yticks([]) # 隐藏Y轴刻度
ax.grid(True, axis='x', linestyle='--', alpha=0.5)
ax.set_xlabel('Clock Pulses / Count', fontsize=12)
ax.set_title('4-Bit Asynchronous Up Counter Timing Diagram (Q0-Q3)', fontsize=14, pad=20)

# 底部添加计数值
for i in range(17):
    val = i % 16
    ax.text(i + 0.5, -0.8, str(val), ha='center', fontsize=11, fontweight='bold')
    # 添加二进制状态
    bin_str = f"{val:04b}"
    # ax.text(i + 0.5, 9.5, bin_str, ha='center', fontsize=8, color='gray')

plt.tight_layout()
plt.savefig('counter_waveform.png')
plt.show()