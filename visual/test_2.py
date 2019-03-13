import kalmanFilter as KF
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import DBSCAN

filename = "log_data_960_machine.csv"

data = pd.read_csv(filename)
# 根据z轴的取值过滤掉明显异常的点
data = data[data.Z > -2]
data = data[data.Z < 3]
Frames = list(set(data["Frame"]))
# state = np.matrix(np.array([data.iloc[0, 2], data.iloc[0, 3], 0, 0])).T
# P = np.matrix(np.eye(4) * 1000)
# R = np.matrix(1e-3*np.eye(2))
# x_hat = []
# y_hat = []
# x_observ = []
# y_observ = []

preframe = Frames[0] - 1
fig = plt.figure()
meanx = 0
meany = 0
meanz = 0
plt.ion()
# ax = fig.add_subplot(111, projection="3d")
for frame in Frames:       
        # dt = (frame - preframe) * 0.2
        Intensity = np.array(data[data.Frame == frame].loc[:, ['Intensity']])
        x = np.array(data[data.Frame == frame].loc[:, ['X','Y']])
        z = np.array(data[data.Frame == frame].loc[:, ['Z']])
        clustering = DBSCAN(eps = 0.8, min_samples = 4).fit(x)
        labels = clustering.labels_
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
                
        if n_clusters > 1:  # 暂时选取一个最明显的类别
                Intensity_Sum = [ np.mean(Intensity[labels == i]) for i in range(n_clusters)]
                label = np.argmax(Intensity_Sum)
                meanx = np.mean(x[labels == label, 0])
                meany = np.mean(x[labels == label, 1])
                meanz = np.mean(z[labels == label])
        elif n_clusters == 1:
                meanx = np.mean(x[labels == 0, 0])
                meany = np.mean(x[labels == 0, 1])
                meanz = np.mean(z[labels == 0])
                # preframe = frame
        # if frame - preframe > 1:
        #         state = np.matrix(np.array([meanx, meany, 0, 0])).T
        #         P = np.matrix(np.eye(4) * 10)
        #         R = np.matrix(1e-3*np.eye(2)) 
        #         dt = 0
        # predictx, predicty, state, P, R = KF.kalman(meanx, meany, P, state, R, dt)
        # x_hat.append(predictx)
        # y_hat.append(predicty)
        # x_observ.append(meanx)
        # y_observ.append(meany)
        # preframe = frame
        # norm = colors.Normalize(vmin=0, vmax=1.0)
        # ax.scatter(meanx, meany, meanz)
        plt.scatter(meanx, meany)
        plt.show()
        plt.pause(0.05)
# plt.figure()
# plt.scatter(x_hat, y_hat)
# plt.xlim(-5, 5)
# plt.ylim(0, 8)
# plt.figure()
# plt.scatter(x_observ, y_observ)

# plt.xlim(-5, 5)
# plt.ylim(0, 8)
# plt.show()



        



    
    


