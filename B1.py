import pandas as pd
import matplotlib.pyplot as plt
import NMR_utils as nmr


def averageAcrossExperiments():  #
    # Using a loop to read the data and compute the average
    dfs = [nmr.readData(f'Raw_Data/B1_90_S{i}.CSV') for i in range(1, 5)]
    average = pd.concat([df['V'] for df in dfs], axis=1).mean(axis=1)
    average_df = pd.DataFrame({'TIME': dfs[0]['TIME'], 'V': average})
    # Extract the 'TIME' column from the first dataframe and combine it with the averaged 'V' values
    return average_df

yoffset = 0.68

nmr.plotCSV("Raw_Data/B1_90_S1.CSV", label="90° pulse", dataOperator=nmr.rollingAverage, yoffset=yoffset)
nmr.plotCSV("Raw_Data/B1_180_S1.CSV", label="180° pulse", dataOperator=nmr.rollingAverage, yoffset=yoffset)
nmr.plotCSV("Raw_Data/B1_270_S1.CSV", label="270° pulse", dataOperator=nmr.rollingAverage, yoffset=yoffset,
            title='Free Induction Decay Curve of Water Doped with CuSO₄')
plt.savefig("images/B1.pdf", format="pdf", bbox_inches="tight")
plt.show()
