import visual_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import trainingClassifier
from trainingClassifier import feature_extraction
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import time
from sklearn.svm import LinearSVC

filename = "log_data_human.csv"
visual_func.visual_PointCloud_3D(filename)
# data = pd.read_csv(filename)
# # 根据z轴的取值过滤掉明显异常的点
# data = data[data.Z > -2]
# data = data[data.Z < 3]
# plt.figure()
# plt.scatter(data["Frame"], data["Doppler"])
# plt.show()
# Frames = list(set(data["Frame"]))

# for frame in Frames:
#     x = np.array(data[data.Frame == frame].loc[:, ['X','Y']])
#     clustering = DBSCAN(eps = 0.8, min_samples = 4).fit(x)
#     labels = clustering.labels_
#     n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
# 将聚类的结果写回.csv文件， cluster_id, -1 represents noise
#     print(n_clusters)
#     for i in range(n_clusters):
#         class_member_mask = (labels == i)
#         meanx = np.mean(x[class_member_mask, 0])
#         meany = np.mean(x[class_member_mask, 1])
#         # meanz = np.mean(x[class_member_mask, 2])

# filename = "log_data.csv"
# save_path = "result.txt"
# feature_extraction(filename, 1, save_path )

# filename = "log_data_2.csv"
# save_path = "result_2.txt"
# feature_extraction(filename, 0, save_path )

# filename = "log_data_3.csv"
# save_path = "result_3.txt"
# feature_extraction(filename, 0, save_path )

# filename = "log_data_4.csv"
# save_path = "result_4.txt"
# feature_extraction(filename, 0, save_path )

# # 读入所有数据
# column = ['mean_Intensity', 'variance_Doppler','point_Num', 'label']
# data_1 = pd.read_table("result.txt", sep=' ', header=None, names=column)
# data_2 = pd.read_table("result_2.txt", sep=' ', header=None, names=column)
# data_3 = pd.read_table("result_3.txt", sep=' ', header=None, names=column)
# data_4 = pd.read_table("result_4.txt", sep=' ', header=None, names=column)
# data = data_1.append(data_2, sort=False)
# data = data.append(data_3, sort=False)
# data = data.append(data_4, sort=False)
# # split dataset into training set and test set
# x = data.iloc[:, 0:3]
# y = data.iloc[:, 3]
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
# # training
# # Scaling Features
# scaler = StandardScaler().fit(x_train)
# fds = scaler.transform(x_train)
# clf = LinearSVC()
# print("Training a Linear SVM Classifier")
# t = time.time()
# clf.fit(fds, y_train)
# t2 = time.time()
# print(round(t2-t, 4), "seconds to training model")

# # testing
# # scaler = StandardScaler().fit(x_test)
# fds = scaler.transform(x_test)
# print("testing model")
# accuracy = clf.score(fds, y_test)
# print("the accuracy is {}".format(accuracy))




