function [ predictx, predicty, state, param ] = kalmanFilter( t, x, y, state, param, previous_t )
%UNTITLED Summary of this function goes here
%   Four dimensional state: position_x, position_y, velocity_x, velocity_y

    %% Place parameters like covarainces, etc. here:
    sigm =  eye(4);
    sigo =  1e-3*eye(2);
    dt = t- previous_t;
    A = [1 0 dt 0 ;0 1 0 dt;0 0 1 0;0 0 0 1];
    C = [1 0 -10* dt 0;0 1 0 -10*dt];
    % Check if the first time running this function
    if previous_t<0
        state = [x,y,0,0];
        param.P = 10 * sigm;
        param.R =  sigo;
        predictx = x;
        predicty = y;
        return;
    end
    param.R = sigo;
    P = A*param.P*A'+ sigm;
    K = P*C'/(param.R+C*P*C');
    state = A*state'+ K*([x,y]'-C*A*state');
    state = state';
    param.P = P - K*C*P;
    predictx = state(1);
    predicty = state(2);
    return
end