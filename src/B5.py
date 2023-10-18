import matplotlib.pyplot as plt
import numpy as np

import NMR_utils as nmr

df=nmr.rollingAverage(nmr.readData("../Raw_Data/B5_DopesWaterCuSO4_P1.CSV"))
M_zero = df[df['TIME']>=0]
print(M_zero)
for i in range(1,6):
    nmr.plotCSV(f"../Raw_Data/B5_DopesWaterCuSO4_P{i}.CSV",
            title='Trace for Doped Water', label=f"Curve {i}"
                )
plt.savefig("../images/B5_water.pdf", format="pdf", bbox_inches="tight")
plt.show()

for i in range(1,6):
    nmr.plotCSV(f"../Raw_Data/B5_Ethanol_P{i}.CSV",
            title='Trace for Ethanol', label=f"Curve {i}"
                )
plt.savefig("../images/B5_water.pdf", format="pdf", bbox_inches="tight")
plt.show()

for i in range(1,6):
    nmr.plotCSV(f"../Raw_Data/B5_Rubber_P{i}.CSV",
            title='Trace for Rubber', label=f"Curve {i}"
                )
plt.savefig("../images/B5_water.pdf", format="pdf", bbox_inches="tight")
plt.show()