import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def readData(filename):
    df = pd.read_csv(filename, skiprows=15, header=0)
    new = df[['TIME', 'CH1']].copy()
    new.columns = ['TIME', 'V']
    return new


def empty(input):
    return input


def plotCSV(filename="", data=None, label="NMR", ylabel="Voltage", xlabel="Time (s)", title="NMR Decay Curve", dataOperator=empty, xoffset=0, yoffset=0):
    if filename != "":
        data = readData(filename).dropna()
    data = dataOperator(data)
    plt.plot(data['TIME'] + xoffset, data["V"] + yoffset, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.legend()


def createBestFit(df):
    df = df.dropna()
    slope, intercept = np.polyfit(df['TIME'], df['V'], 1)
    df['V'] = slope * df['TIME'] + intercept
    print("Slope:", slope)
    print("Intercept:", intercept)
    return df


def rollingAverage(df, window=20):
    df['V'] = df['V'].rolling(window=window).mean()
    return df.dropna()






