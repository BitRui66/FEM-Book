import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = False

# ---------------------- 1. 数据 ----------------------
n_blue = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
h_blue = np.array([1.0 / n for n in n_blue])
error_blue = 1.2 * (h_blue ** 2)

h_red = np.array([1/2, 1/4, 1/8, 1/16, 1/32, 1/64])
error_red = np.array([0.3, 1e-3, 1e-6, 1e-9, 1e-12, 1e-15])

# ---------------------- 2. 绘图 ----------------------
plt.figure(figsize=(8, 6))

plt.loglog(h_blue, error_blue, 'b-v', markersize=8, linewidth=1.5)
plt.loglog(h_red, error_red, 'r-^', markersize=8, linewidth=1.5)

plt.text(0.1, 0.008, 'Slope = 2.00', color='blue', fontsize=14, fontweight='bold')
plt.text(0.03, 2e-10, 'Slope ≈ 6.00', color='red', fontsize=14, fontweight='bold')

# 设置坐标轴标签和范围
plt.xlim(1e-3, 1)
plt.ylim(1e-15, 1e3)
plt.xlabel('$h = 1/n$ (log scale)', fontsize=16)
plt.ylabel('$e_n = |\pi - \pi_n|$ (log scale)', fontsize=16)
plt.grid(True, which="both", ls="--")

plt.show()