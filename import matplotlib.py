import matplotlib.pyplot as plt

def visualize_2D(arr, title, x_lim, y_lim):
    """
    绘制二维数组的散点图
    """
    # 创建画布
    fig, ax = plt.subplots()

    # 绘制散点图
    ax.scatter(arr[:, 0], arr[:, 1])

    # 设置坐标轴范围
    ax.set_xlim(-x_lim, x_lim)
    ax.set_ylim(-y_lim, y_lim)

    # 设置标题
    ax.set_title(title)

    # 显示图表
    plt.show()

# 绘制二维数组的散点图
visualize_2D(a_2D, '二维数组可视化', 3, 3)
