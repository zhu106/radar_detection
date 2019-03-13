clear
data = csvread("log_data.csv", 2);
state = [data(1,3), data(1, 4), 0, 0];
% param.R = 1e-3*eye(2);
% param.P = eye(4);
param = {};
t = 0:1:length(data);
previous_t = -1;
P_x = [];
P_y = [];
for i = 1: length(data)
    [predictx, predicty, state, param ] = kalmanFilter( t(i), data(i, 3), data(i, 4), state, param, previous_t );
    P_x = [P_x predictx];
    P_y = [P_y predicty];
    previous_t = t(i);   
end
plot(P_x, P_y)
