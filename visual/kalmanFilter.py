import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


def kalman(x, y, P, state, R, dt):
    '''
    x, y: measurement
    state: estimation 
    '''
    # system model
    sigm = np.matrix(np.eye(4))  # 4 by 4   
    A = np.matrix(np.array([[1, 0, dt, 0],[0, 1, 0, dt],[0, 0, 1, 0],[0, 0, 0, 1]])) # 4 by 4
    # measurement model
    # sigo = np.matrix(1e-3*np.eye(2))  # 2 by 2
    C = np.matrix(np.array([[1, 0, -10 * dt, 0],[0, 1, 0, -10 * dt]]))  # 2 by 4
    P_ = A * P * A.T + sigm 
    # kalman gain   
    k = P_ * C.T * (R + C * P_ * C.T).I
    # 
    #  state
    state = A * state + k * ( np.matrix(np.array([x, y])).T - C * A * state)
    P = P_ - k * C * P_
    predictx = state[0].tolist()[0][0]
    predicty = state[1].tolist()[0][0]

    return predictx, predicty, state, P, R


filename = "log_data.csv"
data = pd.read_csv(filename)
# initial state
state = np.matrix(np.array([data.iloc[0, 2], data.iloc[0, 3], 0, 0])).T
P = np.matrix(np.eye(4) * 10)
R = np.matrix(1e-3*np.eye(2))
dt = 1
x_hat = []
y_hat = []
for i in range(len(data)):
    predictx, predicty, state, P, R = kalman( data.iloc[i, 2], data.iloc[i, 3], P, state, R, dt)
    x_hat.append(predictx)
    y_hat.append(predicty)

# plt.plot(x_hat, y_hat, 'g')
# plt.plot(data.iloc[:, 2], data.iloc[:, 3], 'r')
# plt.show()






