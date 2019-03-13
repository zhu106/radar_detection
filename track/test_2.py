import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

filename = "log_data_human.csv"

data = pd.read_csv(filename)
# 根据z轴的取值过滤掉明显异常的点
Frames = list(set(data["Frame"]))

preframe = Frames[0] - 1
fig = plt.figure()
plt.ion()
for frame in Frames:       
        dt = (frame - preframe) * 0.2
        Intensity = np.array(data[data.Frame == frame].loc[:, ['Intensity']])
        x = np.array(data[data.Frame == frame].loc[:, ['X','Y']])
        clustering = DBSCAN(eps = 0.8, min_samples = 4).fit(x)
        labels = clustering.labels_
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
                
        if n_clusters > 1:  # 暂时选取一个最明显的类别
                Intensity_Sum = [ np.mean(Intensity[labels == i]) for i in range(n_clusters)]
                label = np.argmax(Intensity_Sum)
                meanx = np.mean(x[labels == label, 0])
                meany = np.mean(x[labels == label, 1])
        elif n_clusters == 1:
                meanx = np.mean(x[labels == 0, 0])
                meany = np.mean(x[labels == 0, 1])
                preframe = frame
        plt.scatter(meanx, meany)
        plt.show()
        plt.pause(0.005)




        



    
    


