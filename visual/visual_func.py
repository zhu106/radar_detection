import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import colors
from mpl_toolkits.mplot3d import Axes3D

def visual_PointCloud_3D(filename):
    data = pd.read_csv(filename)
    Frames = list(set(data["Frame"]))
    fig = plt.figure()
    plt.ion()
    for frame in Frames:
        plt.clf()
        ax = fig.add_subplot(111, projection="3d")
        # norm = colors.Normalize(vmin=0, vmax=1.0)
        ax.scatter(data[data.Frame == frame].X, data[data.Frame == frame].Y, data[data.Frame == frame].Z)
        ax.set_xlabel("X Label")
        ax.set_ylabel("Y Label")
        ax.set_zlabel("Z Label")
        ax.set_xlim(-10, 10)
        ax.set_ylim(0, 10)
        ax.set_zlim(-5, 5)
        plt.show()
        plt.pause(0.005)
    plt.ioff()
    return

def visual_PointCloud_2D(filename):
    data = pd.read_csv(filename)
    Frames = list(set(data["Frame"]))
    # fig = plt.figure()
    plt.ion()
    for frame in Frames:
        plt.clf()
        # ax2 = fig.add_subplot(111)
        norm = colors.Normalize(vmin=-1, vmax=1.0)
        plt.xlim(right=2, left=-2)
        plt.ylim(top=-1, bottom=10)
        plt.scatter(data[data.Frame == frame].X, data[data.Frame == frame].Y, c=data[data.Frame == frame].Doppler,
                    norm=norm)
        # plt.scatter(data[data.Frame == frame].X, data[data.Frame == frame].Z, c=data[data.Frame == frame].Doppler)
        plt.show()
        plt.colorbar()
        plt.pause(0.005)
    plt.ioff()
    return

def plot_heatmap(filename, frame):
    data = pd.read_csv(filename)
    # filter
    data = data[data.Z > -3]
    data = data[data.Z < 3]
    data = data[data.X > -5]
    data = data[data.X < 5]
    # Frames = list(set(data["Frame"]))
    x = np.array(data[data.Frame == frame].loc[:, 'X'] * 100, dtype = 'int')
    # y = np.array(data[data.Frame == frame].loc[:, 'Y'] * 100, dtype = 'int')
    z = np.array(data[data.Frame == frame].loc[:, 'Z'] * 100, dtype = 'int')
    # Doppler = np.array(data[data.Frame == frame].loc[:, 'Doppler'])
    Intensity = np.array(data[data.Frame == frame].loc[:, 'Intensity'])
    # 将intensity归一化
    amin, amax = Intensity.min(), Intensity.max()
    Intensity = (Intensity - amin) / (amax - amin)
    matrix_heatmap = np.zeros((600, 1000))
    matrix_heatmap[z + 300, x + 500] = Intensity
    plt.figure()
    sns.heatmap(matrix_heatmap, cmap='jet')
    plt.figure()
    plt.scatter(x, z)
    plt.xlim(right = 500, left = -500)
    plt.ylim(top = 300, bottom = -300)
    plt.show()
    return

if __name__ == "__main__":
    filename = "log_data_960_machine.csv"
    visual_PointCloud_3D(filename)



