import matplotlib.pyplot as plt
import NMR_utils as nmr

nmr.plotCSV("../Raw_Data/B4_DopedWaterCuSO4_P1.CSV", label="Doped Water", #dataOperator=nmr.rollingAverage,
            title='IR Trace for Doped Water')
plt.savefig("../images/B4_Doped_Water.pdf", format="pdf", bbox_inches="tight")
plt.show()


nmr.plotCSV("../Raw_Data/B4_Ethanol_P1.CSV", label="Ethanol", #dataOperator=nmr.rollingAverage,
            title='IR Trace for Ethanol')
plt.savefig("../images/B4_Ethanol.pdf", format="pdf", bbox_inches="tight")
plt.show()

nmr.plotCSV("../Raw_Data/B4_Rubber_P1.CSV", label="Rubber", #dataOperator=nmr.rollingAverage,
            title='IR Trace for Rubber')
plt.savefig("../images/B4_Rubber.pdf", format="pdf", bbox_inches="tight")
plt.show()
