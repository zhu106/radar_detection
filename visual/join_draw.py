import json
import os
import scipy.io as sio
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import time


json_filepath = "C:/Users/Administrator/OneDrive/Research/database/pose/7"
pd_filepath = "C:/Users\Administrator\OneDrive\Research\database\pointcloud_frame/7"

for json_i in range(1,1917):

    i = json_i//3 + 1
    pd_filename = os.path.join(pd_filepath,str(i))
    pd_filename = pd_filename + ".mat"
    pd_load_dict = sio.loadmat(pd_filename)
    pd_point_list = pd_load_dict['point']
    pd_X = pd_point_list[:,2]
    pd_Y = pd_point_list[:,4]
    pd_H = pd_point_list[:,3]
    pd_Z = pd_point_list[:,6]/400


    json_filename = os.path.join(json_filepath,str(json_i))
    json_filename = json_filename + "_keypoints.json"
    with open(json_filename, "r") as load_f:
        json_load_dict = json.load(load_f)
        # print(load_dict['people'][0]['pose_keypoints_2d'])
        json_point_list = json_load_dict['people'][0]['pose_keypoints_2d']
    json_X = []
    json_Y = []
    json_Z = []
    for json_j in range(0, len(json_point_list)):
        # print(i)
        if json_j % 3 == 0:
            json_X.append(json_point_list[json_j])
        if json_j % 3 == 1:
            json_Y.append(800-json_point_list[json_j])
        if json_j % 3 == 2:
            json_Z.append(json_point_list[json_j])

    plt.ion()
    # plt.figure(facecolor='black')
    norm = colors.Normalize(vmin=0, vmax=1.0)
    plt.title("json figure")

    plt.subplot(211)
    plt.xlim(right=1000, left=0)
    plt.ylim(top=1000, bottom=0)
    plt.scatter(json_X, json_Y, c=json_Z, norm=norm)
    plt.colorbar()
    plt.show()

    # plt.close()

    plt.subplot(212)
    plt.ion()
    norm = colors.Normalize(vmin=0, vmax=1.0)
    plt.xlim(right=2, left=-2)
    plt.ylim(top=3, bottom=-1)
    plt.scatter(pd_X, pd_Y, c=pd_Z, norm=norm)
    plt.colorbar()
    plt.show()
    plt.pause(0.005)
    plt.clf()
