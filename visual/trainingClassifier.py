from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
import pandas as pd
import numpy as np
import time

def feature_extraction(filename, label, save_path):
    unscaled_fds = []
    print("Calculating the descriptors for samples ")
    data = pd.read_csv(filename)
    # filter
    data = data[data.Z > -2]
    data = data[data.Z < 3]
    Frames = list(set(data["Frame"]))
    for frame in Frames:
        # for every frame, calculate the mean of intensity and variance of Doppler
        mean_intensity = np.mean(data[data["Frame"] == frame].Intensity)
        variance_Doppler = np.var(data[data["Frame"] == frame].Doppler) 
        point_Num = data[data["Frame"] == frame].Obj.iloc[0]
        unscaled_fds.append([mean_intensity, variance_Doppler, point_Num, label])
    # 写入文件  
    np.savetxt(save_path, np.array(unscaled_fds))

    print("completing calculating")
    return 

    