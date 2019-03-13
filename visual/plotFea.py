import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import colors

filename = "log_data_960_machine.csv"
data = pd.read_csv(filename)

plt.scatter(data.Frame, data.Doppler)
# plt.scatter(data[data.Frame == frame].X, data[data.Frame == frame].Z, c=data[data.Frame == frame].Doppler)
plt.show()