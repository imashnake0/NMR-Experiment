import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Raw_Data\B5_DopesWaterCuSO4_P1.CSV', skiprows=15, header=0)
print(df)
time = df['TIME']
ch1 = df['CH1']

plt.figure(figsize=(10, 6))
plt.plot(time, ch1, label='CH1')
plt.xlabel('Time')
plt.ylabel('CH1')
plt.title('CH1 vs Time')
plt.grid(True)
plt.legend()
plt.show()
