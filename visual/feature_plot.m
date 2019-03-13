data = csvread("log_data_aircondition.csv", 2);
figure;
plot(data(:, 1), data(:, 6), '.');
title("doppler")
xlabel("Frame")
ylabel("doppler (m/s)")

hold off;
figure;
plot(data(:, 1), data(:, 7), '.');
title("intensity")
xlabel("Frame")
ylabel("intensity")
hold off;
figure;
plot(data(:, 1), data(:, 5), '.');
title("pos Z")
xlabel("Frame")
ylabel("pos Z (m)")
hold off;
