import matplotlib.pyplot as plt
import NMR_utils as nmr

nmr.plotCSV("../Raw_Data/B3_DopedWaterCuSO4_90.CSV", label="Doped Water", #dataOperator=nmr.rollingAverage,
            title='IR Trace for Doped Water')
plt.savefig("../images/B3_Doped_Water.pdf", format="pdf", bbox_inches="tight")
plt.show()


nmr.plotCSV("../Raw_Data/B3_Ethanol_90.CSV", label="Ethanol", #dataOperator=nmr.rollingAverage,
            title='IR Trace for Ethanol')
plt.savefig("../images/B3_Ethanol.pdf", format="pdf", bbox_inches="tight")
plt.show()

nmr.plotCSV("../Raw_Data/B3_Rubber_90.CSV", label="Rubber", #dataOperator=nmr.rollingAverage,
            title='IR Trace for Rubber')
plt.savefig("../images/B3_Rubber.pdf", format="pdf", bbox_inches="tight")
plt.show()
