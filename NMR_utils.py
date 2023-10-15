import pandas as pd
import matplotlib.pyplot as plt

def readData(filename):
    df = pd.read_csv(filename, skiprows=15, header=0)
    new = df[['TIME', 'CH1']].copy()
    new.columns = ['TIME', 'V']
    return new

def plotCSV(filename, label="NMR", ylabel="Voltage", xlabel="Time", title="NMR Decay Curve", rollingAverageWindow=1):
    data = readData(filename)
    plt.plot(data['TIME'], data['V'].rolling(window=rollingAverageWindow).mean(), label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.legend()


