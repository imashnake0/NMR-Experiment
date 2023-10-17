import numpy as np
import matplotlib.pyplot as plt
import NMR_utils as nmr

yoffset = 0.75
nmr.plotCSV(filename="../Raw_Data/B2_DopedWaterCuSO4_90.CSV", dataOperator=nmr.rollingAverage, label="Water Doped with CuSO₄", yoffset=yoffset)
nmr.plotCSV(filename="../Raw_Data/B2_Ethanol_90.CSV", dataOperator=nmr.rollingAverage, label="Ethanol", yoffset=yoffset)
nmr.plotCSV(filename="../Raw_Data/B2_Rubber_90.CSV", dataOperator=nmr.rollingAverage, label="Rubber", title="FID Curves of Different Materials with a 90° Pulse", yoffset=yoffset)
plt.savefig("images/B2.pdf", format="pdf", bbox_inches="tight")
plt.show()

#Plot semi-log graphs of all the materials
#Set the window in which we see exponential decay
window_start = 0.0001
window_end = 0.002
trim_operator = lambda df:df[(df['TIME'] >= window_start) & (df['TIME'] <= window_end)].dropna()
#Vertically shift voltage data because you can't take log of negatives
vertical_shift = 3
log_operator= lambda x:x.assign(V=np.log(nmr.rollingAverage(trim_operator(x)).dropna()["V"] + vertical_shift))
nmr.plotCSV(filename="../Raw_Data/B2_DopedWaterCuSO4_90.CSV", dataOperator=log_operator, label="Water Doped with CuSO₄")
nmr.plotCSV(filename="../Raw_Data/B2_Ethanol_90.CSV", dataOperator=log_operator, label="Ethanol")
nmr.plotCSV(filename="../Raw_Data/B2_Rubber_90.CSV", dataOperator=log_operator, label="Rubber", title="FID semi-log Curves of Different Materials with a 90° Pulse", ylabel="log(Voltage)")
plt.savefig("images/B2_log.pdf", format="pdf", bbox_inches="tight")
plt.show()

#Plot Best-fit lines
nmr.plotCSV(filename="../Raw_Data/B2_DopedWaterCuSO4_90.CSV", dataOperator=log_operator, label="Water Doped with CuSO₄")
nmr.plotCSV(filename="../Raw_Data/B2_DopedWaterCuSO4_90.CSV", dataOperator=lambda x:nmr.createBestFit(log_operator(x)), label="Best Fit line", title="FID semi-log Curve of Doped Water", ylabel="log(Voltage)")

nmr.plotCSV(filename="../Raw_Data/B2_Ethanol_90.CSV", dataOperator=log_operator, label="Ethanol")
nmr.plotCSV(filename="../Raw_Data/B2_Ethanol_90.CSV", dataOperator=lambda x:nmr.createBestFit(log_operator(x)), label="Best Fit line", title="FID semi-log Curve of Ethanol", ylabel="log(Voltage)")

nmr.plotCSV(filename="../Raw_Data/B2_Rubber_90.CSV", dataOperator=log_operator, label="Rubber")
nmr.plotCSV(filename="../Raw_Data/B2_Rubber_90.CSV", dataOperator=lambda x:nmr.createBestFit(log_operator(x)), label="Best Fit line", title="FID semi-log Curve of All Samples", ylabel="log(Voltage)")

plt.savefig("images/B2_log_best_fit.pdf", format="pdf", bbox_inches="tight")
plt.show()


