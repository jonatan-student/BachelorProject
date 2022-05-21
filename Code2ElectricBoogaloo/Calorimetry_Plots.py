# %%
from cProfile import label
from scipy.optimize import curve_fit
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#------Importing pure datas
WaterQuench = pd.read_csv('Watertest1.csv', sep = ';')
WaterSlow = pd.read_csv('Watertest2.csv', sep = ';')
GlycerolQuench = pd.read_csv('Glyceroltest1.csv', sep = ';')
GlycerolSlow = pd.read_csv('Glyceroltest2.csv', sep = ';')

#-----Importing all data at 0.23 molar concentration glycerol with stuff in it
BSAQ023 = pd.read_csv('BSA-Q023.csv', sep = ';')
BUFQ023 = pd.read_csv('BUF-Q023.csv', sep = ';')
IAFPQ023 = pd.read_csv('IAFP-Q023.csv', sep = ';')
BSAS023 = pd.read_csv('BSA-S023.csv', sep = ';')
BUFS023 = pd.read_csv('BUF-S022.csv', sep = ';')
IAFPS023 = pd.read_csv('IAFP-S022.csv', sep = ';')

#importing all data at 0.047 molar concentration
BUFQ0047 = pd.read_csv('BUF-Q0047.csv', sep = ';')
IAFPQ0047 = pd.read_csv('IAFP-Q0047.csv', sep = ';')
BUFS0047 = pd.read_csv('BUF-S0047.csv', sep = ';')
IAFPS0047 = pd.read_csv('IAFP-S0047.csv', sep = ';')
BSAQ0047 = pd.read_csv('BSA-Q0047.csv', sep = ';')
BSAS0047 = pd.read_csv('BSA-S0047.csv', sep = ';')

#------Importing all data for quench spectrum of pure mixtures
Q0047 = pd.read_csv('Quench0047.csv', sep = ';')
Q010 = pd.read_csv('quench010.csv', sep = ';')
Q023 = pd.read_csv('quench023.csv', sep = ';')
Q030 = pd.read_csv('quench030.csv', sep = ';')
Q040 = pd.read_csv('quench040.csv', sep = ';')
Q050 = pd.read_csv('quench050.csv', sep = ';')
Q060 = pd.read_csv('quench060.csv', sep = ';')

#----Importing all data for slow spectrum of pure mixtures
S0047 = pd.read_csv('Slow0047.csv', sep = ';')
S010 = pd.read_csv('slow010.csv', sep = ';')
S023 = pd.read_csv('slow023.csv', sep = ';')
S030 = pd.read_csv('slow030.csv', sep = ';')
S040 = pd.read_csv('slow040.csv', sep = ';')
S050 = pd.read_csv('slow050.csv', sep = ';')
S060 = pd.read_csv('slow060.csv', sep = ';')


#----Importing all data from fish afp
FAFPQ05 = pd.read_csv('FAFP-Q05.csv', sep = ';')
FAFPQ10 = pd.read_csv('FAFP-Q10.csv', sep = ';')
FAFPQ15 = pd.read_csv('FAFP-Q15.csv', sep = ';')
FAFPS05 = pd.read_csv('FAFP-S05.csv', sep = ';')
FAFPS10 = pd.read_csv('FAFP-S10.csv', sep = ';')
FAFPS15 = pd.read_csv('FAFP-S15.csv', sep = ';')

#----importing data from sources on eutectic stuff
PCCP17 = pd.read_csv('PCCP17Dielectrics.csv', sep = ',')
PCCP18 = pd.read_csv('PCCP18Dielectrics.csv', sep = ',')
MeltingPts = pd.read_csv('Meltingpoints.csv', sep = ',')
jnoncryst = pd.read_csv('jnoncrystDIelectrics.csv', sep = ',')
Jensen2018 = pd.read_csv('OtherCalorimetry.csv', sep = ',')

#our recorded glass transistion temperatures
QuenchGlassTemps = np.array([
    [0.047, 167.78],
    [0.1, 167.78],
    [0.23, 161.01],
    [0.3, 166.64],
    [0.4, 172.54],
    [0.5, 176.65],
    [0.6, 180.77],
    [0.995, 192.39]
])

RelQuenchGlassTemps = np.array([
    [0.047, 167.78],
    [0.1, 167.78],
    [0.23, 161.01]
])

QuenchBUFglassTemps = np.array([
    [0.047, 169.56],
    [0.23, 169.81]
])

QuenchBSAglassTemps = np.array([
    [0.047, 170.72],
    [0.23, 173.47]
])

QuenchIAFPglassTemps = np.array([
    [0.047, 170.27],
    [0.23, 167.78]
])

QuenchFAFPglassTemps = np.array([
    [0.0, 169.81],
    [0.5, 160.19],
    [1.0, 158.49],
    [1.5, 158.69]
])

SlowGlassTemps = np.array([
    [0.047, 167.74],
    [0.1, 167.66],
    [0.23, 160.01],
    [0.3, 165.71],
    [0.4, 171.27],
    [0.5, 176.17],
    [0.6, 179.84],
    [0.995, 191.93]
])

relSlowGlassTemps = np.array([
    [0.047, 167.74],
    [0.1, 167.66],
    [0.23, 160.01],
])

SlowBUFglassTemps = np.array([
    [0.047, 170.38],
    [0.23, 170.27]
])

SlowBSAglassTemps = np.array([
    [0.047, 169.88],
    [0.23, 172.95]
])

SlowIAFPglassTemps = np.array([
    [0.047, 169.44],
    [0.23, 167.48]
])
SlowFAFPglassTemps = np.array([
    [0.0, 170.27],
    [0.5, 158.98],
    [1.0, 157.73],
    [1.5, 157.89],
])

#recorded melting temperatures

QuenchMeltTemps = np.array([
    [0.0, 273.50],
    [0.047, 266.21],
    [0.1, 258.10],
    [0.23, 235.54]
])

QuenchBUFmeltTemps = np.array([
    [0.047, 262.13],
    [0.23, 257.85]
])

QuenchBSAmeltTemps = np.array([
    [0.047, 263.69],
    [0.23, 264.85]
])

QuenchIAFPmeltTemps = np.array([
    [0.047, 262.85],
    [0.23, 257.1]
])

QuenchFAFPmeltTemps = np.array([
    [0.0, 257.85],
    [0.5, 239.6],
    [1.0, 242.64],
    [1.5, 242.51]
])

SlowMeltTemps = np.array([
    [0.0, 273.55],
    [0.1, 258.5],
    [0.23, 236.00]
])

SlowBUFmeltTemps = np.array([
    [0.047, 262.20],
    [0.23, 259.11]
])

SlowBSAmeltTemps = np.array([
    [0.047, 263.62],
    [0.23, 265.1]
])


SlowIAFPmeltTemps = np.array([
    [0.047, 262.70],
    [0.23, 257.5]
])

SlowFAFPmeltTemps = np.array([
    [0.0, 259.11],
    [0.5, 239.1],
    [1.0, 242.52],
    [1.5, 242.60]
])



#-----Isolating data around glass transition by cutting the data-
# ----to a range on the x axis and limiting it to above 0 on the y axis
GlycerolQuenchGlass = GlycerolQuench[(GlycerolQuench['T']> 188) & (GlycerolQuench['T']< 196) & (GlycerolQuench['dTdt [K/s]']>0) ]
GlycerolSlowGlass = GlycerolSlow[(GlycerolSlow['T [K]']> 188) & (GlycerolSlow['T [K]']< 196) & (GlycerolSlow['dTdt [K/s]']>0) ]

#quench tests at glass transition
Q0047glass = Q0047[(Q0047['T [K] '] > 162) & (Q0047['T [K] '] < 174) & (Q0047[' dTdt [K/s] '] > 0)]
Q010glass = Q010[(Q010['T [K] '] > 162) & (Q010['T [K] '] < 174) & (Q010[' dTdt [K/s] '] > 0)]
Q023glass = Q023[(Q023['T [K] '] > 156) & (Q023['T [K] '] < 165) & (Q023[' dTdt [K/s] '] > 0)]
Q030glass = Q030[(Q030['T [K] '] > 160) & (Q030['T [K] '] < 170) & (Q030[' dTdt [K/s] '] > 0)]
Q040glass = Q040[(Q040['T [K] '] > 168) & (Q040['T [K] '] < 176) & (Q040[' dTdt [K/s] '] > 0)]
Q050glass = Q050[(Q050['T[K] '] > 172) & (Q050['T[K] '] < 181) & (Q050[' dTdt [K/s] '] > 0) & (Q050[' dTdt [K/s] '] < 0.35)]
Q060glass = Q060[(Q060['T[K] '] > 176) & (Q060['T[K] '] < 185) & (Q060[' dTdt [K/s] '] > 0)]

#slow tests at glass transition time is also a cutting factor here as crystalization in cooling makes for messy data
S0047glass = S0047[(S0047['T [K] '] > 150) & (S0047['T [K] '] < 176) & (S0047[' dTdt [K/s] '] > 0) & (S0047[' etime [s] '] > 1000)]
S010glass = S010[(S010['T [K] '] > 162) & (S010['T [K] '] < 174) & (S010[' dTdt [K/s] '] > 0) & (S010[' etime [s] '] > 1000)]
S023glass = S023[(S023['T [K] '] > 154.5) & (S023['T [K] '] < 166.5) & (S023[' dTdt [K/s] '] > 0) & (S023[' etime [s] '] > 1000)]
S030glass = S030[(S030['T [K] '] > 161) & (S030['T [K] '] < 170) & (S030[' dTdt [K/s] '] > 0) & (S030[' etime [s] '] > 1000)]
S040glass = S040[(S040['T [K] '] > 166) & (S040['T [K] '] < 176) & (S040[' dTdt [K/s] '] > 0) & (S040[' etime [s] '] > 1000)]
S050glass = S050[(S050['T [K] '] > 172) & (S050['T [K] '] < 180) & (S050[' dTdt [K/s] '] > 0) & (S050[' etime [s] '] > 1000)]
S060glass = S060[(S060['T [K] '] > 175) & (S060['T [K] '] < 185) & (S060[' dTdt [K/s] '] > 0) & (S010[' etime [s] '] > 1000)]

#Quench tests glasses for mixtures with stuff added
BUF_Q023glass = BUFQ023[(BUFQ023['T [K] '] > 164) & (BUFQ023['T [K] '] < 176) & (BUFQ023[' dTdt [K/s] '] > 0)]
IAFP_Q023glass = IAFPQ023[(IAFPQ023['T [K] '] > 160) & (IAFPQ023['T [K] '] < 174) & (IAFPQ023[' dTdt [K/s] '] > 0)]
BSA_Q023glass = BSAQ023[(BSAQ023['T [K] '] > 168) & (BSAQ023['T [K] '] < 180) & (BSAQ023[' dTdt [K/s] '] > 0)]

BUF_Q0047glass = BUFQ0047[(BUFQ0047['T [K] '] > 164) & (BUFQ0047['T [K] '] < 175) & (BUFQ0047[' dTdt [K/s] '] > 0)]
IAFP_Q0047glass = IAFPQ0047[(IAFPQ0047['T [K] '] > 164) & (IAFPQ0047['T [K] '] < 175) & (IAFPQ0047[' dTdt [K/s] '] > 0)]
BSA_Q0047glass = BSAQ0047[(BSAQ0047['T [K] '] > 165.5) & (BSAQ0047['T [K] '] < 176) & (BSAQ0047[' dTdt [K/s] '] > 0)]

#Quench Test glasses for FAFPs in buffer
FAFP_Q05_Glass = FAFPQ05[(FAFPQ05['T [K] '] > 154) & (FAFPQ05['T [K] ']< 167) & (FAFPQ05[' dTdt [K/s] '] > 0)]
FAFP_Q10_Glass = FAFPQ10[(FAFPQ10['T [K] '] > 152) & (FAFPQ10['T [K] ']< 164) & (FAFPQ10[' dTdt [K/s] '] > 0)]
FAFP_Q15_Glass = FAFPQ15[(FAFPQ15['T [K] '] > 152) & (FAFPQ15['T [K] ']< 164) & (FAFPQ15[' dTdt [K/s] '] > 0)]

#Slow Test glasses for mixtures with stuff added
BUF_S023glass = BUFS023[(BUFS023['T [K] '] > 164) & (BUFS023['T [K] '] < 176) & (BUFS023[' dTdt [K/s] '] > 0) & (BUFS023[' etime [s] '] > 1000)]
IAFP_S023glass = IAFPS023[(IAFPS023['T [K] '] > 160) & (IAFPS023['T [K] '] < 174) & (IAFPS023[' dTdt [K/s] '] > 0) & (IAFPS023[' etime [s] '] > 1000)]
BSA_S023glass = BSAS023[(BSAS023['T [K] '] > 168) & (BSAS023['T [K] '] < 180) & (BSAS023[' dTdt [K/s] '] > 0) & (BSAS023[' etime [s] '] > 1000)]

BUF_S0047glass = BUFS0047[(BUFS0047['T [K] '] > 166) & (BUFS0047['T [K] '] < 175) & (BUFS0047[' dTdt [K/s] '] > 0) & (BUFS0047[' etime [s] '] > 1000)]
IAFP_S0047glass = IAFPS0047[(IAFPS0047['T [K] '] > 164) & (IAFPS0047['T [K] '] < 175) & (IAFPS0047[' dTdt [K/s] '] > 0) & (IAFPS0047[' etime [s] '] > 1000)]
BSA_S0047glass = BSAS0047[(BSAS0047['T [K] '] > 164) & (BSAS0047['T [K] '] < 175) & (BSAS0047[' dTdt [K/s] '] > 0) & (BSAS0047[' etime [s] '] > 1000)]

#Slow test glasses for FAFPs in buffer
FAFP_S05_Glass = FAFPS05[(FAFPS05['T [K] '] > 152) & (FAFPS05['T [K] ']< 166) & (FAFPS05[' dTdt [K/s] '] > 0) & (FAFPS05[' etime [s] ']> 1000)]
FAFP_S10_Glass = FAFPS10[(FAFPS10['T [K] '] > 152) & (FAFPS10['T [K] ']< 164) & (FAFPS10[' dTdt [K/s] '] > 0) & (FAFPS10[' etime [s] ']> 1000)]
FAFP_S15_Glass = FAFPS15[(FAFPS15['T [K] '] > 152) & (FAFPS15['T [K] ']< 164) & (FAFPS15[' dTdt [K/s] '] > 0) & (FAFPS15[' etime [s] ']> 1000)]

#-----Isolating data around Melting temperature
#pure
WaterQuenchMelt = WaterQuench[(WaterQuench['T']> 272.6) & (WaterQuench['T']< 274.6) & (WaterQuench['dTdt [K/s]'] > 0)]
WaterSlowMelt = WaterSlow[(WaterSlow['T']> 272) & (WaterSlow['T']< 274.3) & (WaterSlow['dTdt [K/s]'] > 0) & (WaterSlow['etime [s]']> 1000)]

#quench melting temperatures
Q0047Melt = Q0047[(Q0047['T [K] '] > 265) & (Q0047['T [K] '] < 270) & (Q0047[' dTdt [K/s] '] > 0) & (Q0047[' etime [s] ']> 500)]
Q010Melt = Q010[(Q010['T [K] '] > 258) & (Q010['T [K] '] < 260) & (Q010[' dTdt [K/s] '] > 0) & (Q010[' etime [s] ']> 500)]
Q023Melt = Q023[(Q023['T [K] '] > 231) & (Q023['T [K] '] < 238) & (Q023[' dTdt [K/s] '] > 0) & (Q023[' etime [s] ']> 500)]

#Slow melting temperatures
S0047Melt = S0047[(S0047['T [K] '] > 150) & (S0047['T [K] '] < 580) & (S0047[' dTdt [K/s] '] > -0.5)  & (S0047[' etime [s] ']> 500)]
S010Melt = S010[(S010['T [K] '] > 253) & (S010['T [K] '] < 260) & (S010[' dTdt [K/s] '] > 0)  & (S010[' etime [s] ']> 1000)]
S023Melt = S023[(S023['T [K] '] > 231) & (S023['T [K] '] < 239) & (S023[' dTdt [K/s] '] > 0)  & (S023[' etime [s] ']> 1000)]

#melting for mixtures with stuff added
#Quench melts
BUF_Q023Melt = BUFQ023[(BUFQ023['T [K] '] > 255) & (BUFQ023['T [K] '] < 262.5) & (BUFQ023[' dTdt [K/s] '] > 0)]
IAFP_Q023Melt = IAFPQ023[(IAFPQ023['T [K] '] > 255) & (IAFPQ023['T [K] '] < 260) & (IAFPQ023[' dTdt [K/s] '] > 0)]
BSA_Q023Melt = BSAQ023[(BSAQ023['T [K] '] > 263.5) & (BSAQ023['T [K] '] < 273) & (BSAQ023[' dTdt [K/s] '] > 0)]

BUF_Q0047Melt = BUFQ0047[(BUFQ0047['T [K] '] > 259) & (BUFQ0047['T [K] '] < 269) & (BUFQ0047[' dTdt [K/s] '] > 0)]
IAFP_Q0047Melt = IAFPQ0047[(IAFPQ0047['T [K] '] > 261.9) & (IAFPQ0047['T [K] '] < 263.3) & (IAFPQ0047[' dTdt [K/s] '] > 0)]
BSA_Q0047Melt = BSAQ0047[(BSAQ0047['T [K] '] > 263) & (BSAQ0047['T [K] '] < 268) & (BSAQ0047[' dTdt [K/s] '] > 0)]

#Slow melts
BUF_S023Melt = BUFS023[(BUFS023['T [K] '] > 262) & (BUFS023['T [K] '] < 263) & (BUFS023[' dTdt [K/s] '] > 0) & (BUFS023[' etime [s] '] > 1000)]
IAFP_S023Melt = IAFPS023[(IAFPS023['T [K] '] > 255) & (IAFPS023['T [K] '] < 260) & (IAFPS023[' dTdt [K/s] '] > 0) & (IAFPS023[' etime [s] '] > 1000)]
BSA_S023Melt = BSAS023[(BSAS023['T [K] '] > 263.5) & (BSAS023['T [K] '] < 273) & (BSAS023[' dTdt [K/s] '] > 0) & (BSAS023[' etime [s] '] > 1000)]

BUF_S0047Melt = BUFS0047[(BUFS0047['T [K] '] > 266) & (BUFS0047['T [K] '] < 269) & (BUFS0047[' dTdt [K/s] '] > 0) & (BUFS0047[' etime [s] '] > 1000)]
IAFP_S0047Melt = IAFPS0047[(IAFPS0047['T [K] '] > 262) & (IAFPS0047['T [K] '] < 267) & (IAFPS0047[' dTdt [K/s] '] > 0) & (IAFPS0047[' etime [s] '] > 1000)]
BSA_S0047Melt = BSAS0047[(BSAS0047['T [K] '] > 263) & (BSAS0047['T [K] '] < 269) & (BSAS0047[' dTdt [K/s] '] > 0) & (BSAS0047[' etime [s] '] > 1000)]

#melting for FAFPs in buffer
FAFP_Q05_Melt = FAFPQ05[(FAFPQ05['T [K] '] > 235) & (FAFPQ05['T [K] '] < 242) & (FAFPQ05[' dTdt [K/s] '] > 0) & (FAFPQ05[' etime [s] '] > 400)]
FAFP_Q10_Melt = FAFPQ10[(FAFPQ10['T [K] '] > 239) & (FAFPQ10['T [K] '] < 246) & (FAFPQ10[' dTdt [K/s] '] > 0) & (FAFPQ10[' etime [s] '] > 400)]
FAFP_Q15_Melt = FAFPQ15[(FAFPQ15['T [K] '] > 239) & (FAFPQ15['T [K] '] < 246) & (FAFPQ15[' dTdt [K/s] '] > 0) & (FAFPQ15[' etime [s] '] > 400)]
FAFP_S05_Melt = FAFPS05[(FAFPS05['T [K] '] > 235) & (FAFPS05['T [K] '] < 242) & (FAFPS05[' dTdt [K/s] '] > 0) & (FAFPS05[' etime [s] '] > 1000)]
FAFP_S10_Melt = FAFPS10[(FAFPS10['T [K] '] > 239) & (FAFPS10['T [K] '] < 246) & (FAFPS10[' dTdt [K/s] '] > 0) & (FAFPS10[' etime [s] '] > 1000)]
FAFP_S15_Melt = FAFPS15[(FAFPS15['T [K] '] > 239) & (FAFPS15['T [K] '] < 246) & (FAFPS15[' dTdt [K/s] '] > 0) & (FAFPS15[' etime [s] '] > 1000)]


#-------reduction of noise by rolling average
n=20

#___glasses__
#quench
Q0047glass = Q0047glass.rolling(n).mean()
Q010glass = Q010glass.rolling(n).mean()
Q023glass = Q023glass.rolling(n).mean()
Q030glass = Q030glass.rolling(n).mean()
Q040glass = Q040glass.rolling(n).mean()
Q050glass = Q050glass.rolling(n).mean()
Q060glass = Q060glass.rolling(n).mean()
GlycerolQuenchGlass = GlycerolQuenchGlass.rolling(n).mean()

#slow
S0047glass = S0047glass.rolling(n).mean()
S010glass = S010glass.rolling(n).mean()
S023glass = S023glass.rolling(n).mean()
S030glass = S030glass.rolling(n).mean()
S040glass = S040glass.rolling(n).mean()
S050glass = S050glass.rolling(n).mean()
S060glass = S060glass.rolling(n).mean()
GlycerolSlowGlass = GlycerolSlowGlass.rolling(n).mean()

#quench+stuff
BUF_Q023glass = BUF_Q023glass.rolling(n).mean()
IAFP_Q023glass = IAFP_Q023glass.rolling(n).mean()
BSA_Q023glass = BSA_Q023glass.rolling(n).mean()

BUF_Q0047glass = BUF_Q0047glass.rolling(n).mean()
IAFP_Q0047glass = IAFP_Q0047glass.rolling(n).mean()
BSA_Q0047glass = BSA_Q0047glass.rolling(n).mean()

FAFP_Q05_Glass = FAFP_Q05_Glass.rolling(n).mean()
FAFP_Q10_Glass = FAFP_Q10_Glass.rolling(n).mean()
FAFP_Q15_Glass = FAFP_Q15_Glass.rolling(n).mean()

#slow+stuff
BUF_S023glass = BUF_S023glass.rolling(n).mean()
IAFP_S023glass = IAFP_S023glass.rolling(n).mean()
BSA_S023glass = BSA_S023glass.rolling(n).mean()

BUF_S0047glass = BUF_S0047glass.rolling(n).mean()
IAFP_S0047glass = IAFP_S0047glass.rolling(n).mean()
BSA_S0047glass = BSA_S0047glass.rolling(n).mean()

FAFP_S05_Glass = FAFP_S05_Glass.rolling(n).mean()
FAFP_S10_Glass = FAFP_S10_Glass.rolling(n).mean()
FAFP_S15_Glass = FAFP_S15_Glass.rolling(n).mean()


#__MELTING__

#quench
WaterQuenchMelt = WaterQuenchMelt.rolling(n).mean()
Q0047Melt = Q0047Melt.rolling(n).mean()
Q010Melt = Q010Melt.rolling(n).mean()
Q023Melt = Q023Melt.rolling(n).mean()


#slow
WaterSlowMelt = WaterSlowMelt.rolling(n).mean()
S0047Melt = S0047Melt.rolling(n).mean()
S010Melt = S010Melt.rolling(n).mean()
S023Melt = S023Melt.rolling(n).mean()


#quench+stuff
BUF_Q023Melt = BUF_Q023Melt.rolling(n).mean()
IAFP_Q023Melt = IAFP_Q023Melt.rolling(n).mean()
BSA_Q023Melt = BSA_Q023Melt.rolling(n).mean()

BUF_Q0047Melt = BUF_Q0047Melt.rolling(n).mean()
IAFP_Q0047Melt = IAFP_Q0047Melt.rolling(n).mean()
BSA_Q0047Melt = BSA_Q0047Melt.rolling(n).mean()

FAFP_Q05_Melt = FAFP_Q05_Melt.rolling(n).mean()
FAFP_Q10_Melt = FAFP_Q10_Melt.rolling(n).mean()
FAFP_Q15_Melt = FAFP_Q15_Melt.rolling(n).mean()

#slow+stuff
BUF_S023Melt = BUF_S023Melt.rolling(n).mean()
IAFP_S023Melt = IAFP_S023Melt.rolling(n).mean()
BSA_S023Melt = BSA_S023Melt.rolling(n).mean()

BUF_S0047Melt = BUF_S0047Melt.rolling(n).mean()
IAFP_S0047Melt = IAFP_S0047Melt.rolling(n).mean()
BSA_S0047Melt = BSA_S0047Melt.rolling(n).mean()

FAFP_S05_Melt = FAFP_S05_Melt.rolling(n).mean()
FAFP_S10_Melt = FAFP_S10_Melt.rolling(n).mean()
FAFP_S15_Melt = FAFP_S15_Melt.rolling(n).mean()

#------Deriving the data based on temperature step one - finding differences
#quench tests
Q0047glassDiff = Q0047glass.diff(axis = 0, periods= 1)
Q010glassDiff = Q010glass.diff(axis = 0, periods= 1)
Q023glassDiff = Q023glass.diff(axis = 0, periods= 1)
Q030glassDiff = Q030glass.diff(axis = 0, periods= 1)
Q040glassDiff = Q040glass.diff(axis = 0, periods= 1)
Q050glassDiff = Q050glass.diff(axis = 0, periods= 1)
Q060glassDiff = Q060glass.diff(axis = 0, periods= 1)
Q0047MeltDiff = Q0047Melt.diff(axis = 0, periods = 1)
Q010MeltDiff = Q010Melt.diff(axis = 0, periods = 1)
Q023MeltDiff = Q023Melt.diff(axis = 0, periods = 1)


#Slow tests
S0047glassDiff = S0047glass.diff(axis = 0, periods= 1)
S010glassDiff = S010glass.diff(axis = 0, periods= 1)
S023glassDiff = S023glass.diff(axis = 0, periods= 1)
S030glassDiff = S030glass.diff(axis = 0, periods= 1)
S040glassDiff = S040glass.diff(axis = 0, periods= 1)
S050glassDiff = S050glass.diff(axis = 0, periods= 1)
S060glassDiff = S060glass.diff(axis = 0, periods= 1)
S0047MeltDiff = S0047Melt.diff(axis = 0, periods =1)
S010MeltDiff = S010Melt.diff(axis = 0, periods = 1)
S023MeltDiff = S023Melt.diff(axis = 0, periods = 1)



#--Buffer and + with stuff
#glasss
BUF_Q023glassDiff = BUF_Q023glass.diff(axis = 0, periods= 1)
IAFP_Q023glassDiff = IAFP_Q023glass.diff(axis = 0, periods= 1)
BSA_Q023glassDiff = BSA_Q023glass.diff(axis = 0, periods= 1)

BUF_S023glassDiff = BUF_S023glass.diff(axis=0, periods=1)
IAFP_S023glassDiff = IAFP_S023glass.diff(axis=0, periods=1)
BSA_S023glassDiff = BSA_S023glass.diff(axis=0, periods=1)

BUF_Q0047glassDiff = BUF_Q0047glass.diff(axis = 0, periods= 1)
IAFP_Q0047glassDiff = IAFP_Q0047glass.diff(axis = 0, periods= 1)
BSA_Q0047glassDiff = BSA_Q0047glass.diff(axis = 0, periods= 1)

BUF_S0047glassDiff = BUF_S0047glass.diff(axis=0, periods=1)
IAFP_S0047glassDiff = IAFP_S0047glass.diff(axis=0, periods=1)
BSA_S0047glassDiff = BSA_S0047glass.diff(axis=0, periods=1)

#melting
BUF_Q023MeltDiff = BUF_Q023Melt.diff(axis = 0, periods= 1)
IAFP_Q023MeltDiff = IAFP_Q023Melt.diff(axis = 0, periods= 1)
BSA_Q023MeltDiff = BSA_Q023Melt.diff(axis = 0, periods= 1)

BUF_S023MeltDiff = BUF_S023Melt.diff(axis=0, periods=1)
IAFP_S023MeltDiff = IAFP_S023Melt.diff(axis=0, periods=1)
BSA_S023MeltDiff = BSA_S023Melt.diff(axis=0, periods=1)

BUF_Q0047MeltDiff = BUF_Q0047Melt.diff(axis = 0, periods= 1)
IAFP_Q0047MeltDiff = IAFP_Q0047Melt.diff(axis = 0, periods= 1)
BSA_Q0047MeltDiff = BSA_Q0047Melt.diff(axis = 0, periods= 1)

BUF_S0047MeltDiff = BUF_S0047Melt.diff(axis=0, periods=1)
IAFP_S0047MeltDiff = IAFP_S0047Melt.diff(axis=0, periods=1)
BSA_S0047MeltDiff = BSA_S0047Melt.diff(axis=0, periods=1)

#----FAFP stuff
#quench
FAFP_Q15_MeltDiff = FAFP_Q15_Melt.diff(axis=0, periods=1)
FAFP_Q15_GlassDiff = FAFP_Q15_Glass.diff(axis=0, periods=1)
FAFP_Q10_MeltDiff = FAFP_Q10_Melt.diff(axis=0, periods=1)
FAFP_Q10_GlassDiff = FAFP_Q10_Glass.diff(axis=0, periods=1)
FAFP_Q05_MeltDiff  = FAFP_Q05_Melt.diff(axis=0, periods=1)
FAFP_Q05_GlassDiff = FAFP_Q05_Glass.diff(axis=0, periods=1)

#slow
FAFP_S15_MeltDiff = FAFP_S15_Melt.diff(axis=0, periods=1)
FAFP_S15_GlassDiff = FAFP_S15_Glass.diff(axis=0, periods=1)
FAFP_S10_MeltDiff = FAFP_S10_Melt.diff(axis=0, periods=1)
FAFP_S10_GlassDiff = FAFP_S10_Glass.diff(axis=0, periods=1)
FAFP_S05_MeltDiff  = FAFP_S05_Melt.diff(axis=0, periods=1)
FAFP_S05_GlassDiff = FAFP_S05_Glass.diff(axis=0, periods=1)


#--pure stuff
WaterQuenchMeltDiff= WaterQuenchMelt.diff(axis = 0, periods = 1)
WaterSlowMeltDiff= WaterSlowMelt.diff(axis = 0, periods = 1)

GlycerolQuenchGlassDiff = GlycerolQuenchGlass.diff(axis = 0, periods=1)
GlycerolSlowGlassDiff = GlycerolSlowGlass.diff(axis=0, periods=1)

#--- Deriving data based on temperature step 2 ---- dividing by temperature difference
#quench Melt data
WaterQuenchMeltDerived = WaterQuenchMeltDiff['dTdt [K/s]']/WaterQuenchMeltDiff['T']
Q0047MeltDerived = Q0047MeltDiff[' dTdt [K/s] ']/ Q0047MeltDiff['T [K] ']
Q010MeltDerived = Q010MeltDiff[' dTdt [K/s] ']/ Q010MeltDiff['T [K] ']
Q023MeltDerived = Q023MeltDiff[' dTdt [K/s] ']/ Q023MeltDiff['T [K] ']
BUF_Q0047MeltDerived = BUF_Q0047MeltDiff[' dTdt [K/s] ']/BUF_Q0047MeltDiff['T [K] ']
BSA_Q0047MeltDerived = BSA_Q0047MeltDiff[' dTdt [K/s] ']/BSA_Q0047MeltDiff['T [K] ']
IAFP_Q0047MeltDerived = IAFP_Q0047MeltDiff[' dTdt [K/s] ']/IAFP_Q0047MeltDiff['T [K] ']
BUF_Q023MeltDerived = BUF_Q023MeltDiff[' dTdt [K/s] ']/BUF_Q023MeltDiff['T [K] ']
BSA_Q023MeltDerived = BSA_Q023MeltDiff[' dTdt [K/s] ']/BSA_Q023MeltDiff['T [K] ']
IAFP_Q023MeltDerived = IAFP_Q023MeltDiff[' dTdt [K/s] ']/IAFP_Q023MeltDiff['T [K] ']
FAFP_Q05_MeltDerived = FAFP_Q05_MeltDiff[' dTdt [K/s] ']/FAFP_Q05_MeltDiff['T [K] ']
FAFP_Q10_MeltDerived = FAFP_Q10_MeltDiff[' dTdt [K/s] ']/FAFP_Q10_MeltDiff['T [K] ']
FAFP_Q15_MeltDerived = FAFP_Q15_MeltDiff[' dTdt [K/s] ']/FAFP_Q15_MeltDiff['T [K] ']

#quench glass data
Q0047glassDerived = Q0047glassDiff[' dTdt [K/s] '] / Q0047glassDiff['T [K] ']
Q010glassDerived = Q010glassDiff[' dTdt [K/s] '] / Q010glassDiff['T [K] ']
Q023glassDerived = Q023glassDiff[' dTdt [K/s] '] / Q023glassDiff['T [K] ']
Q030glassDerived = Q030glassDiff[' dTdt [K/s] '] / Q030glassDiff['T [K] ']
Q040glassDerived = Q040glassDiff[' dTdt [K/s] '] / Q040glassDiff['T [K] ']
Q050glassDerived = Q050glassDiff[' dTdt [K/s] '] / Q050glassDiff['T[K] ']
Q060glassDerived = Q060glassDiff[' dTdt [K/s] '] / Q060glassDiff['T[K] ']
GlycerolQuenchGlassDerived = GlycerolQuenchGlassDiff['dTdt [K/s]']/GlycerolQuenchGlassDiff['T']
BUF_Q0047glassDerived = BUF_Q0047glassDiff[' dTdt [K/s] '] / BUF_Q0047glassDiff['T [K] ']
BSA_Q0047glassDerived = BSA_Q0047glassDiff[' dTdt [K/s] '] / BSA_Q0047glassDiff['T [K] ']
IAFP_Q0047glassDerived = IAFP_Q0047glassDiff[' dTdt [K/s] '] / IAFP_Q0047glassDiff['T [K] ']
BUF_Q023glassDerived = BUF_Q023glassDiff[' dTdt [K/s] '] / BUF_Q023glassDiff['T [K] ']
BSA_Q023glassDerived = BSA_Q023glassDiff[' dTdt [K/s] '] / BSA_Q023glassDiff['T [K] ']
IAFP_Q023glassDerived = IAFP_Q023glassDiff[' dTdt [K/s] '] / IAFP_Q023glassDiff['T [K] ']
FAFP_Q05_GlassDerived = FAFP_Q05_GlassDiff[' dTdt [K/s] ']/FAFP_Q05_GlassDiff['T [K] ']
FAFP_Q10_GlassDerived = FAFP_Q10_GlassDiff[' dTdt [K/s] ']/FAFP_Q10_GlassDiff['T [K] ']
FAFP_Q15_GlassDerived = FAFP_Q15_GlassDiff[' dTdt [K/s] ']/FAFP_Q15_GlassDiff['T [K] ']

#Slow Melt data
WaterSlowMeltDerived = WaterSlowMeltDiff['dTdt [K/s]']/WaterSlowMeltDiff['T']
S0047MeltDerived = S0047MeltDiff[' dTdt [K/s] ']/ S0047MeltDiff['T [K] ']
S010MeltDerived = S010MeltDiff[' dTdt [K/s] ']/ S010MeltDiff['T [K] ']
S023MeltDerived = S023MeltDiff[' dTdt [K/s] ']/ S023MeltDiff['T [K] ']
BUF_S0047MeltDerived = BUF_S0047MeltDiff[' dTdt [K/s] ']/BUF_S0047MeltDiff['T [K] ']
BSA_S0047MeltDerived = BSA_S0047MeltDiff[' dTdt [K/s] ']/BSA_S0047MeltDiff['T [K] ']
IAFP_S0047MeltDerived = IAFP_S0047MeltDiff[' dTdt [K/s] ']/IAFP_S0047MeltDiff['T [K] ']
BUF_S023MeltDerived = BUF_S023MeltDiff[' dTdt [K/s] ']/BUF_S023MeltDiff['T [K] ']
BSA_S023MeltDerived = BSA_S023MeltDiff[' dTdt [K/s] ']/BSA_S023MeltDiff['T [K] ']
IAFP_S023MeltDerived = IAFP_S023MeltDiff[' dTdt [K/s] ']/IAFP_S023MeltDiff['T [K] ']
FAFP_S05_MeltDerived = FAFP_S05_MeltDiff[' dTdt [K/s] ']/FAFP_S05_MeltDiff['T [K] ']
FAFP_S10_MeltDerived = FAFP_S10_MeltDiff[' dTdt [K/s] ']/FAFP_S10_MeltDiff['T [K] ']
FAFP_S15_MeltDerived = FAFP_S15_MeltDiff[' dTdt [K/s] ']/FAFP_S15_MeltDiff['T [K] ']

#Slow glass data
S0047glassDerived = S0047glassDiff[' dTdt [K/s] '] / S0047glassDiff['T [K] ']
S010glassDerived = S010glassDiff[' dTdt [K/s] '] / S010glassDiff['T [K] ']
S023glassDerived = S023glassDiff[' dTdt [K/s] '] / S023glassDiff['T [K] ']
S030glassDerived = S030glassDiff[' dTdt [K/s] '] / S030glassDiff['T [K] ']
S040glassDerived = S040glassDiff[' dTdt [K/s] '] / S040glassDiff['T [K] ']
S050glassDerived = S050glassDiff[' dTdt [K/s] '] / S050glassDiff['T [K] ']
S060glassDerived = S060glassDiff[' dTdt [K/s] '] / S060glassDiff['T [K] ']
GlycerolSlowGlassDerived = GlycerolSlowGlassDiff['dTdt [K/s]']/GlycerolSlowGlassDiff['T [K]']
BUF_S0047glassDerived = BUF_S0047glassDiff[' dTdt [K/s] '] / BUF_S0047glassDiff['T [K] ']
BSA_S0047glassDerived = BSA_S0047glassDiff[' dTdt [K/s] '] / BSA_S0047glassDiff['T [K] ']
IAFP_S0047glassDerived = IAFP_S0047glassDiff[' dTdt [K/s] '] / IAFP_S0047glassDiff['T [K] ']
BUF_S023glassDerived = BUF_S023glassDiff[' dTdt [K/s] '] / BUF_S023glassDiff['T [K] ']
BSA_S023glassDerived = BSA_S023glassDiff[' dTdt [K/s] '] / BSA_S023glassDiff['T [K] ']
IAFP_S023glassDerived = IAFP_S023glassDiff[' dTdt [K/s] '] / IAFP_S023glassDiff['T [K] ']
FAFP_S05_GlassDerived = FAFP_S05_GlassDiff[' dTdt [K/s] ']/FAFP_S05_GlassDiff['T [K] ']
FAFP_S10_GlassDerived = FAFP_S10_GlassDiff[' dTdt [K/s] ']/FAFP_S10_GlassDiff['T [K] ']
FAFP_S15_GlassDerived = FAFP_S15_GlassDiff[' dTdt [K/s] ']/FAFP_S15_GlassDiff['T [K] ']

## quadratic function to fit to our data in the cells below
def quadratic(x, a, b, c):
    y = a*(x**2) + b*x+ c
    return y


# %%
'''
#fitting quadratic function to slow 0 xgly melt
plt.plot(WaterSlowMelt['T'], WaterSlowMelt['dTdt [K/s]'], '^')
plt.show()

# %%
#fitting quadratic function to quench 0 xgly melt
plt.plot(WaterQuenchMelt['T'], WaterQuenchMelt['dTdt [K/s]'], '^')
plt.show()

# %%
#fitting quadratic function to Quench 0.047 xgly melt
plt.plot(Q0047Melt['T [K] '], Q0047Melt[' dTdt [K/s] '], '^')
plt.show()

# %%
#fitting quadratic function to slow 0.1 xgly melt
plt.plot(S010Melt['T [K] '], S010Melt[' dTdt [K/s] '], '^')
plt.show()

# %%
#fitting quadratic function to Quench 0.1 xgly melt

plt.plot(Q010Melt['T [K] '], Q010Melt[' dTdt [K/s] '], '^')
plt.show()

# %%
#fitting quadratic function to slow 0.23 xgly melt

plt.plot(S023Melt['T [K] '], S023Melt[' dTdt [K/s] '], '^')
plt.show()

# %%
#fitting quadratic function to slow 0.23 xgly melt
plt.plot(Q023Melt['T [K] '], Q023Melt[' dTdt [K/s] '], '^')

plt.show()

# %%
#fitting quadratic function to slow 0.047 xgly melt with buffer
plt.plot(BUF_S0047Melt['T [K] '], BUF_S0047Melt[' dTdt [K/s] '], '^')
plt.show()

# %%
#fitting quadratic function to slow 0.047 xgly melt with buffer

plt.plot(BUF_Q0047Melt['T [K] '], BUF_Q0047Melt[' dTdt [K/s] '], '^')
plt.show()

# %%
#fitting quadratic function to slow 0.047 xgly melt with buffer and bsa
plt.plot(BSA_S0047Melt['T [K] '], BSA_S0047Melt[' dTdt [K/s] '], '^')
plt.show()

# %%
#fitting quadratic function to Quench 0.047 xgly melt with buffer and bsa
plt.plot(BSA_Q0047Melt['T [K] '], BSA_Q0047Melt[' dTdt [K/s] '], '^')
plt.show()

# %%
#fitting quadratic function to slow 0.047 xgly melt with buffer and IAFP
plt.plot(IAFP_S0047Melt['T [K] '], IAFP_S0047Melt[' dTdt [K/s] '], '^')
plt.show()

# %%
#fitting quadratic function to Quench 0.047 xgly melt with buffer and IAFP
plt.plot(IAFP_Q0047Melt['T [K] '], IAFP_Q0047Melt[' dTdt [K/s] '], '^')
plt.show()

# %%
#fitting quadratic function to slow 0.23 xgly melt with buffer
plt.plot(BUF_S023Melt['T [K] '], BUF_S023Melt[' dTdt [K/s] '], '^')
plt.show()


# %%
#fitting quadratic function to Quench 0.23 xgly melt with buffer
plt.plot(BUF_Q023Melt['T [K] '], BUF_Q023Melt[' dTdt [K/s] '], '^')
plt.show()

# %%
#fitting quadratic function to slow 0.23 xgly melt with BSA
plt.plot(BSA_S023Melt['T [K] '], BSA_S023Melt[' dTdt [K/s] '], '^')
plt.show()

# %%
#fitting quadratic function to Quench 0.23 xgly melt with BSA
plt.plot(BSA_Q023Melt['T [K] '], BSA_Q023Melt[' dTdt [K/s] '], '^')
plt.show()

# %%
#fitting quadratic function to Slow 0.23 xgly melt with IAFP

plt.plot(IAFP_S023Melt['T [K] '], IAFP_S023Melt[' dTdt [K/s] '], '^')
plt.show()

# %%
#fitting quadratic function to Quench 0.23 xgly melt with IAFP
plt.plot(IAFP_Q023Melt['T [K] '], IAFP_Q023Melt[' dTdt [K/s] '], '^')
plt.show()

# %%
#fitting quadratic function to Slow 0.23 xgly melt with 0.5mM XFAFP
plt.plot(FAFP_S05_Melt['T [K] '], FAFP_S05_Melt[' dTdt [K/s] '], '^')
plt.show()

# %%
#fitting quadratic function to Quench 0.23 xgly melt with 0.5mM XFAFP
plt.plot(FAFP_Q05_Melt['T [K] '], FAFP_Q05_Melt[' dTdt [K/s] '], '^')
plt.show()

# %%
#fitting quadratic function to Slow 0.23 xgly melt with 1.0mM XFAFP
plt.plot(FAFP_S10_Melt['T [K] '], FAFP_S10_Melt[' dTdt [K/s] '], '^')
plt.show()


# %%
#fitting quadratic function to Quench 0.23 xgly melt with 1.0mM XFAFP

plt.plot(FAFP_Q10_Melt['T [K] '], FAFP_Q10_Melt[' dTdt [K/s] '], '^')
plt.show()

# %%
#fitting quadratic function to Slow 0.23 xgly melt with 1.5mM XFAFP
plt.plot(FAFP_S15_Melt['T [K] '], FAFP_S15_Melt[' dTdt [K/s] '], '^')
plt.show()

# %%
#fitting quadratic function to Quench 0.23 xgly melt with 1.5mM XFAFP
plt.plot(FAFP_Q15_Melt['T [K] '], FAFP_Q15_Melt[' dTdt [K/s] '], '^')
plt.show()

#SLOW GLASS GLASS SLOW GLASS GLASS SLOW
# SLow Glas GLASS GLASS GLASS SLOW GLASS GLASS SLO GLASS
# SLOW GLASS GLASS SLOW SLOW GLASS

# %%
#fitting quadratic function to slow 0.047xgly glass
p , c = curve_fit(quadratic,S0047glass['T [K] '].dropna().iloc[:-1], S0047glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(162, 174, num =100)
plt.plot(S0047glass['T [K] '], S0047glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.1 xgly glass
p , c = curve_fit(quadratic,S010glass['T [K] '].dropna().iloc[:-1], S010glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(165, 172, num =100)
plt.plot(S010glass['T [K] '], S010glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.23 xgly glass
p , c = curve_fit(quadratic,S023glass['T [K] '].dropna().iloc[:-1], S023glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(158.5, 164, num =100)
plt.plot(S023glass['T [K] '], S023glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.30 xgly glass
p , c = curve_fit(quadratic,S030glass['T [K] '].dropna().iloc[:-1], S030glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(163.5, 168.5, num =100)
plt.plot(S030glass['T [K] '], S030glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.40 xgly glass
p , c = curve_fit(quadratic,S040glass['T [K] '].dropna().iloc[:-1], S040glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(168, 175, num =100)
plt.plot(S040glass['T [K] '], S040glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.50 xgly glass
p , c = curve_fit(quadratic,S050glass['T [K] '].dropna().iloc[:-1], S050glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(174, 179, num =100)
plt.plot(S050glass['T [K] '], S050glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.60 xgly glass
p , c = curve_fit(quadratic,S060glass['T [K] '].dropna().iloc[:-1], S060glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(177, 184, num =100)
plt.plot(S060glass['T [K] '], S060glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 1.0 xgly glass
p , c = curve_fit(quadratic, GlycerolSlowGlass['T [K]'].dropna().iloc[:-1], GlycerolSlowGlassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(190, 195, num =100)
plt.plot(GlycerolSlowGlass['T [K]'], GlycerolSlowGlassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.047 xgly glass with buffer
p , c = curve_fit(quadratic, BUF_S0047glass['T [K] '].dropna().iloc[:-1], BUF_S0047glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(168, 173, num =100)
plt.plot(BUF_S0047glass['T [K] '], BUF_S0047glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.047 xgly glass with buffer
p , c = curve_fit(quadratic, BSA_S0047glass['T [K] '].dropna().iloc[:-1], BSA_S0047glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(166.69, 173, num =100)
plt.plot(BSA_S0047glass['T [K] '], BSA_S0047glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.047 xgly glass with buffer
p , c = curve_fit(quadratic, IAFP_S0047glass['T [K] '].dropna().iloc[:-1], IAFP_S0047glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(166.69, 173, num =100)
plt.plot(IAFP_S0047glass['T [K] '], IAFP_S0047glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 1.0 xgly glass with buffer
p , c = curve_fit(quadratic, BUF_S023glass['T [K] '].dropna().iloc[:-1], BUF_S023glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(166.69, 174, num =100)
plt.plot(BUF_S023glass['T [K] '], BUF_S023glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.047 xgly glass with BSA
p , c = curve_fit(quadratic, BSA_S023glass['T [K] '].dropna().iloc[:-1], BSA_S023glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(171, 178, num =100)
plt.plot(BSA_S023glass['T [K] '], BSA_S023glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.047 xgly glass with IAFP
p , c = curve_fit(quadratic, IAFP_S023glass['T [K] '].dropna().iloc[:-1], IAFP_S023glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(164, 171.5, num =100)
plt.plot(IAFP_S023glass['T [K] '], IAFP_S023glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.023 xgly glass with FAFP at 0.5mM concentration
p , c = curve_fit(quadratic, FAFP_S05_Glass['T [K] '].dropna().iloc[:-1], FAFP_S05_GlassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(154, 165, num =100)
plt.plot(FAFP_S05_Glass['T [K] '], FAFP_S05_GlassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.023 xgly glass with FAFP at 1.0mM concentration
p , c = curve_fit(quadratic, FAFP_S10_Glass['T [K] '].dropna().iloc[:-1], FAFP_S10_GlassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(154, 165, num =100)
plt.plot(FAFP_S10_Glass['T [K] '], FAFP_S10_GlassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.023 xgly glass with FAFP at 1.5mM concentration
p , c = curve_fit(quadratic, FAFP_S15_Glass['T [K] '].dropna().iloc[:-1], FAFP_S15_GlassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(155, 162, num =100)
plt.plot(FAFP_S15_Glass['T [K] '], FAFP_S15_GlassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

#   Quench                         Qeunch
#             Quench                                                           Quench
#                        Quench                             Quench
#  QUENCH
#
#                                         Quench


# %%
#fitting quadratic function to Quench 0.047 xgly glass
p , c = curve_fit(quadratic,Q0047glass['T [K] '].dropna().iloc[:-1], Q0047glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(165, 172, num =100)
plt.plot(Q0047glass['T [K] '], Q0047glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to Quench 0.10 xgly glass
p , c = curve_fit(quadratic,Q010glass['T [K] '].dropna().iloc[:-1], Q010glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(165, 172, num =100)
plt.plot(Q010glass['T [K] '], Q010glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to Quench 0.23 xgly glass
p , c = curve_fit(quadratic,Q023glass['T [K] '].dropna().iloc[:-1], Q023glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(159, 164, num =100)
plt.plot(Q023glass['T [K] '], Q023glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to Quench 0.30 xgly glass
p , c = curve_fit(quadratic,Q030glass['T [K] '].dropna().iloc[:-1], Q030glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(163, 169, num =100)
plt.plot(Q030glass['T [K] '], Q030glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to Quench 0.40 xgly glass
p , c = curve_fit(quadratic,Q040glass['T [K] '].dropna().iloc[:-1], Q040glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(170.5, 175, num =100)
plt.plot(Q040glass['T [K] '], Q040glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to Quench 0.50 xgly glass
p , c = curve_fit(quadratic,Q050glass['T[K] '].dropna().iloc[:-1], Q050glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(174, 180, num =100)
plt.plot(Q050glass['T[K] '], Q050glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to Quench 0.60 xgly glass
p , c = curve_fit(quadratic,Q060glass['T[K] '].dropna().iloc[:-1], Q060glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(178, 184, num =100)
plt.plot(Q060glass['T[K] '], Q060glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to Quench 1.0 xgly glass
p , c = curve_fit(quadratic, GlycerolQuenchGlass['T'].dropna().iloc[:-1], GlycerolQuenchGlassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(190, 195, num =100)
plt.plot(GlycerolQuenchGlass['T'], GlycerolQuenchGlassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 1.0 xgly glass
p , c = curve_fit(quadratic, BUF_Q0047glass['T [K] '].dropna().iloc[:-1], BUF_Q0047glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(166.9, 173, num =100)
plt.plot(BUF_Q0047glass['T [K] '], BUF_Q0047glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.047 xgly glass with buffer
p , c = curve_fit(quadratic, BSA_Q0047glass['T [K] '].dropna().iloc[:-1], BSA_Q0047glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(168.29, 174, num =100)
plt.plot(BSA_Q0047glass['T [K] '], BSA_Q0047glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.047 xgly glass with buffer
p , c = curve_fit(quadratic, IAFP_Q0047glass['T [K] '].dropna().iloc[:-1], IAFP_Q0047glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(166.29, 173, num =100)
plt.plot(IAFP_Q0047glass['T [K] '], IAFP_Q0047glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 1.0 xgly glass with buffer
p , c = curve_fit(quadratic, BUF_Q023glass['T [K] '].dropna().iloc[:-1], BUF_Q023glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(166.69, 174, num =100)
plt.plot(BUF_Q023glass['T [K] '], BUF_Q023glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.047 xgly glass with BSA
p , c = curve_fit(quadratic, BSA_Q023glass['T [K] '].dropna().iloc[:-1], BSA_Q023glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(171, 178, num =100)
plt.plot(BSA_Q023glass['T [K] '], BSA_Q023glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.047 xgly glass with IAFP
p , c = curve_fit(quadratic, IAFP_Q023glass['T [K] '].dropna().iloc[:-1], IAFP_Q023glassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(164, 171.5, num =100)
plt.plot(IAFP_Q023glass['T [K] '], IAFP_Q023glassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.023 xgly glass with FAFP at 0.5mM concentration
p , c = curve_fit(quadratic, FAFP_Q05_Glass['T [K] '].dropna().iloc[:-1], FAFP_Q05_GlassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(156.5, 165, num =100)
plt.plot(FAFP_Q05_Glass['T [K] '], FAFP_Q05_GlassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.023 xgly glass with FAFP at 1.0mM concentration
p , c = curve_fit(quadratic, FAFP_Q10_Glass['T [K] '].dropna().iloc[:-1], FAFP_Q10_GlassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(155, 163, num =100)
plt.plot(FAFP_Q10_Glass['T [K] '], FAFP_Q10_GlassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

# %%
#fitting quadratic function to slow 0.023 xgly glass with FAFP at 1.5mM concentration
p , c = curve_fit(quadratic, FAFP_Q15_Glass['T [K] '].dropna().iloc[:-1], FAFP_Q15_GlassDerived.dropna())
print('Tg =')
print(-1 * ((p[1])/(2*p[0])))
print('variance =')
print(np.diag(c))
print('Sigma =')
print(np.sqrt(np.diag(c)))
temps = np.linspace(155.5, 162, num =100)
plt.plot(FAFP_Q15_Glass['T [K] '], FAFP_Q15_GlassDerived, '^')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]))
plt.show()

#%%
# Glass tranistions of glycerol water mixtures
plt.plot(Q010glass['T [K] '], Q010glass[' dTdt [K/s] '], label = '0.1')
plt.plot(Q023glass['T [K] '], Q023glass[' dTdt [K/s] '], label = '0.23')
plt.plot(Q030glass['T [K] '], Q030glass[' dTdt [K/s] '], label = '0.3')
plt.plot(Q040glass['T [K] '], Q040glass[' dTdt [K/s] '], label = '0.4')
plt.plot(Q050glass['T[K] '], Q050glass[' dTdt [K/s] '], label = '0.5')
plt.plot(Q060glass['T[K] '], Q060glass[' dTdt [K/s] '], label = '0.6')
plt.plot(GlycerolQuenchGlass['T'], GlycerolQuenchGlass['dTdt [K/s]'], label = '0.995')
plt.legend()
plt.title('Glass Tranistions of Quench Cooled Glycerol Water Mixtures')
plt.show()

# %%
#Melting temperatures of glycerol water mixture
#plt.plot(WaterQuenchMelt['T'], WaterQuenchMelt['dTdt [K/s]'], label ='Quench Cooling')
plt.plot(S0047['T [K] '], S0047[' dTdt [K/s] '], label = '0.047')
#plt.plot(Q010Melt['T [K] '], Q010Melt[' dTdt [K/s] '], label = '0.1')
#plt.plot(Q023Melt['T [K] '], Q023Melt[' dTdt [K/s] '], label = '0.23')
plt.legend()
plt.title('Melting temperatures of Quench Cooled Glycerol Water Mixtures')
plt.show()
'''

# %%
#EUTECTIC GRAPH PLOT
#plt.plot(PCCP17['x'], PCCP17[' y'],'^', color = 'b', label = 'DSC (Bachler 16)')
#plt.plot(PCCP18['x'], PCCP18[' y'], '>',  color = 'b', label = 'DSC (Popov 2015)')
#plt.plot(jnoncryst['x'], jnoncryst[' y'], '*',  color = 'b', label = 'Dialectrics (Hayashi 2005)')
plt.plot(MeltingPts['x'], MeltingPts[' y'],'--',  color = 'grey', label = 'Melting Temperatures (Lane 1925)')
plt.axvline(x = .28, color = 'brown', linestyle= '--', label = 'Eutetic point')
#plt.plot(Jensen2018['x'], Jensen2018[' y'],'d',  color = 'b', label = 'TC (Jensen 2018)')
#plt.plot(RelQuenchGlassTemps[:,0], RelQuenchGlassTemps[:,1], '*',  color = 'grey', label = r'$T_g$ Untreated')
plt.plot(QuenchGlassTemps[:,0], QuenchGlassTemps[:,1], '^',  color = 'blue', label = r'$T_g$ (Quench)')
#plt.plot(relSlowGlassTemps[:,0], relSlowGlassTemps[:,1], '*',  color = 'grey', label = r'$T_g$ Untreated')
plt.plot(SlowGlassTemps[:,0], SlowGlassTemps[:,1], 'v',  color = 'orange', label = r'$T_g$ (Slow)')
plt.plot(QuenchMeltTemps[:,0], QuenchMeltTemps[:,1], '+',  color = 'blue', label = r'$T_M$ (Quench)')
plt.plot(SlowMeltTemps[:,0], SlowMeltTemps[:,1], 'x',  color = 'orange', label = r'$T_M$ (Slow)')
#plt.plot(QuenchBUFglassTemps[:,0], QuenchBUFglassTemps[:,1], '^', color = 'blue', label = 'Tg Buffer')
#plt.plot(QuenchBSAglassTemps[:,0], QuenchBSAglassTemps[:,1], '>', color = 'green', label = 'Tg BSA')
#plt.plot(QuenchIAFPglassTemps[:,0], QuenchIAFPglassTemps[:,1], '<', color = 'red', label = 'Tg IAFP')
#plt.plot(SlowBUFglassTemps[:,0], SlowBUFglassTemps[:,1], '^', color = 'blue', label = 'Tg Buffer')
#plt.plot(SlowBSAglassTemps[:,0], SlowBSAglassTemps[:,1], '>', color = 'green', label = 'Tg BSA')
#plt.plot(SlowIAFPglassTemps[:,0], SlowIAFPglassTemps[:,1], '<', color = 'red', label = 'Tg IAFP')
#plt.plot(QuenchBUFmeltTemps[:,0], QuenchBUFmeltTemps[:,1], '^',color = 'blue', label = 'Tm Buffer')
#plt.plot(QuenchBSAmeltTemps[:,0], QuenchBSAmeltTemps[:,1], '>',color = 'green', label = 'Tm BSA')
#plt.plot(QuenchIAFPmeltTemps[:,0], QuenchIAFPmeltTemps[:,1], '<',color = 'red', label = 'Tm IAFP')
#plt.plot(SlowBUFmeltTemps[:,0], SlowBUFmeltTemps[:,1], '^',color = 'blue', label = 'Tm Buffer')
#plt.plot(SlowBSAmeltTemps[:,0], SlowBSAmeltTemps[:,1], '>',color = 'green', label = 'Tm BSA')
#plt.plot(SlowIAFPmeltTemps[:,0], SlowIAFPmeltTemps[:,1], '<',color = 'red', label = 'Tm IAFP')
plt.xlabel(r'$X_{gly}$', fontsize = 12, loc = 'right')
plt.ylabel(r'$T [K]$', rotation = 0, fontsize = 12, loc = 'top')
plt.yticks()
plt.legend(loc = 'upper right', fontsize = 8)
plt.title(r'Observed $T_M$ and $T_g$ for Glycerol-Water Mixtures')
#plt.title(r'Observed $T_M$ for Quench cooled Treated Mixtures below Eutectic')
#plt.title(r'Observed $T_g$ for Slow cooled Treated Mixtures below Eutectic')
plt.show()
# %%
'''
#Eutectic only our work
plt.plot(QuenchGlassTemps[:,0], QuenchGlassTemps[:,1], '^',  color = 'blue', label = 'Tg (Quench Cooling)')
plt.plot(SlowGlassTemps[:,0], SlowGlassTemps[:,1], 'v',  color = 'orange', label = 'Tg (Slow cooling)')
plt.plot(QuenchMeltTemps[:,0], QuenchMeltTemps[:,1], 'x',  color = 'blue', label = 'Tm (Quench Cooling)')
plt.plot(SlowMeltTemps[:,0], SlowMeltTemps[:,1], '+',  color = 'orange', label = 'Tm (Quench Cooling)')
plt.xlabel('Xgly')
plt.ylabel('Temperature [K]')
plt.legend()
plt.title('Phase Diagram of Glycerol-Water')
plt.show()

#%%

#Buffer Eutectic
plt.plot(QuenchMeltTemps[:,0], QuenchMeltTemps[:,1], '--*',  color = 'Grey', label = 'Tm (Quench Cooling)')
plt.plot(SlowMeltTemps[:,0], SlowMeltTemps[:,1], '--',  color = 'Darkgrey', label = 'Tm (Slow Cooling)')
plt.plot(QuenchBUFglassTemps[:,0], QuenchBUFglassTemps[:,1], 'd', color = 'blue', label = 'Tg (Quench)')
#plt.plot(SlowBUFglassTemps[:,0], SlowBUFglassTemps[:,1], 'd', color = 'orange', label = 'Tg (Slow)')
plt.plot(QuenchBUFmeltTemps[:,0], QuenchBUFmeltTemps[:,1], '^',color = 'blue', label = 'Tm (Quench)')
#plt.plot(SlowBUFmeltTemps[:,0], SlowBUFmeltTemps[:,1], '^', color = 'orange', label = 'Tm (Slow)')
plt.xlabel('Xgly')
plt.ylabel('Temperature [K]')
plt.legend()
plt.title('Phase Diagram of Glycerol-Water with Buffer')
plt.show()

# %%
#Buffer Eutectic

plt.plot(QuenchBUFglassTemps[:,0], QuenchBUFglassTemps[:,1], 'd', color = 'blue', label = 'Tg (Quench)')
plt.plot(SlowBUFglassTemps[:,0], SlowBUFglassTemps[:,1], 'd', color = 'orange', label = 'Tg (Slow)')
plt.plot(QuenchBUFmeltTemps[:,0], QuenchBUFmeltTemps[:,1], '^',color = 'blue', label = 'Tm (Quench)')
plt.plot(SlowBUFmeltTemps[:,0], SlowBUFmeltTemps[:,1], '^', color = 'orange', label = 'Tm (Slow)')

plt.xlabel('Xgly')
plt.ylabel('Temperature [K]')
plt.legend()
plt.title('Phase Diagram of Glycerol-Water with Buffer')
plt.show()


# %%

#IAFP Eutectic
plt.plot(QuenchIAFPglassTemps[:,0], QuenchIAFPglassTemps[:,1], 'd', color = 'blue', label = 'Tg (Quench)')
plt.plot(SlowIAFPglassTemps[:,0], SlowIAFPglassTemps[:,1], 'd', color = 'orange', label = 'Tg (Slow)')
plt.plot(QuenchIAFPmeltTemps[:,0], QuenchIAFPmeltTemps[:,1], '^',color = 'blue', label = 'Tm (Quench)')
plt.plot(SlowIAFPmeltTemps[:,0], SlowIAFPmeltTemps[:,1], '^', color = 'orange', label = 'Tm (Slow)')
plt.xlabel('Xgly')
plt.ylabel('Temperature [K]')
plt.legend()
plt.title('Phase Diagram of Glycerol-Water with IAFP')
plt.show()

# %%
###Water Quench and Slow Melting point
plt.plot(WaterQuenchMelt['T'], WaterQuenchMelt['dTdt [K/s]'], label ='Quench Cooling')
plt.plot(WaterSlowMelt['T'], WaterSlowMelt['dTdt [K/s]'], label = 'Slow Cooling')
plt.title("Melting point of Pure Water")
plt.legend()
plt.xlabel('T')
plt.ylabel('dTdt [K/s]')
plt.show()

# %%

###Glycerol Quench and Slow Glass transistion

plt.plot(GlycerolQuenchGlass['T'], GlycerolQuenchGlass['dTdt [K/s]'], label = 'Quench cooling')
plt.plot(GlycerolSlowGlass['T [K]'], GlycerolSlowGlass['dTdt [K/s]'], label = 'Slow Cooling')
plt.xlabel('T')
plt.ylabel('dTdt [K/s]')
plt.legend()
plt.title("Glass transition of pure Glycerol")
plt.show()

# %%

##PLOT OF DIFFERENTIATED Melting temp data for pure water
plt.plot(WaterQuenchMelt['T'], WaterQuenchMeltDiff['dTdt [K/s]'], label = 'Quench Cooling')
plt.plot(WaterSlowMelt['T'], WaterSlowMeltDiff['dTdt [K/s]'], label = 'Slow Cooling')
plt.xlabel('T [K]')
plt.ylabel('Δ(dTdt)')
plt.legend()
plt.title("Δ(dTdt) for Melting point Data- Water")
plt.show()
plt.show()
# %%

#plot of differentiated glass data
plt.plot(GlycerolQuenchGlass['T'], GlycerolQuenchGlassDiff['dTdt [K/s]'], label = 'Quench Cooling')
plt.plot(GlycerolSlowGlass['T [K]'], GlycerolSlowGlassDiff['dTdt [K/s]'], label = 'Slow Cooling')
plt.xlabel('T [K]')
plt.ylabel('Δ(dTdt)')
plt.legend()
plt.title("Δ(dTdt) for Glass Transition Data- Glycerol")
plt.show()

# %%
#Quench melting diffentiated
plt.plot(WaterQuenchMelt['T'], WaterQuenchMeltDerived, label = 0.0)
plt.plot(Q0047Melt['T [K] '], Q0047MeltDerived, label = 0.047)
plt.plot(Q010Melt['T [K] '], Q010MeltDerived, label = 0.1)
plt.plot(Q023Melt['T [K] '], Q023MeltDerived, label = 0.23)
plt.ylabel('Δ(dTdt)')
plt.legend()
plt.title("Δ(dTdt) for melting temperature Data")
plt.show()
# %%
#Quench melting diffentiated
plt.plot(WaterSlowMelt['T'], WaterQuenchMeltDiff['dTdt [K/s]'], label = 0.0)
plt.plot(Q010Melt['T [K] '], Q010MeltDiff[' dTdt [K/s] '], label = 0.1)
plt.plot(Q023Melt['T [K] '], Q023MeltDiff[' dTdt [K/s] '], label = 0.23)
plt.ylabel('Δ(dTdt)')
plt.legend()
plt.title("Δ(dTdt) for melting temperature Data")
plt.show()


# %%
#& (S023['T [K] ']>150) & (S023['T [K] ']<170)
S023warm = S023[(S023[' dTdt [K/s] ']>=0)& (S023['T [K] ']>234.5) & (S023['T [K] ']<237.7)]
S023cool = S023[(S023[' dTdt [K/s] ']<=0) & (S023[' etime [s] ']<1000)]
S023warm = S023warm.rolling(20).mean()
#fitting quadratic function to slow 0.23 xgly glass
p , c = curve_fit(quadratic,S023glass['T [K] '].dropna().iloc[:-1], S023glassDerived.dropna())
temps = np.linspace(156.8, 165, num =100)
Sigma = np.sqrt(np.diag(c))
SigMean= (Sigma[0]+Sigma[1]+Sigma[2])/3
Tg = -1 * ((p[1])/(2*p[0]))

#plt.plot(S023['T [K] '], S023[' dTdt [K/s] '])
#plt.plot(S023warm['T [K] '], S023warm[' dTdt [K/s] '],  label = 'Mixture')
#plt.plot(S023cool['T [K] '], S023cool[' dTdt [K/s] '], color = 'BLUE', label = 'Cooling')
plt.plot(S023glass['T [K] '], S023glassDerived, '^', label = 'Mixture')
plt.plot(temps, quadratic(temps, p[0], p[1], p[2]), label = 'Quadratic Fit')
#plt.plot(S023Melt['T [K] '], S023Melt[' dTdt [K/s] '], '^', label = 'mixture')
#plt.plot(temps, quadratic(temps, p[0], p[1], p[2]), label = 'Quadratic fit')
plt.title("Thermogram of Slow Cooled 0.23 Xgly Mixture")
#plt.axhline(y=0, color = 'Grey', linestyle='--')
#plt.axvline(x=235, color ='Violet', linestyle= '--', label = 'Previous Cut')
#plt.axvline(x=237, color ='Violet', linestyle= '--')
plt.axvspan(Tg-SigMean,Tg+SigMean, alpha = 0.2, color = 'red', label = r'1 $\sigma$ around T_g')
plt.xlabel('$T$ [K]')
plt.yticks(rotation = 45)
#plt.ylabel(r'$\frac{dT}{dt}$',fontsize= 16, rotation = 0)
plt.ylabel(r'$\frac{d(\frac{dT}{dt})}{dT}$',fontsize= 16, rotation = 0)
plt.legend()
plt.show()

# %%
plt.plot(QuenchFAFPglassTemps[:,0], QuenchFAFPglassTemps[:,1], 'v', color = 'blue', label = r'Quench Cooled')
plt.plot(SlowFAFPglassTemps[:,0], SlowFAFPglassTemps[:,1], '^', color = 'orange', label = r'Slow Cooled')
plt.xlabel(r'$x_{AFP}$ [mMol]', loc = 'right', fontsize = 12)
plt.ylabel(r'$T_g$ [K]', loc = 'top', fontsize = 12, rotation = 0)
plt.title(r'$T_g$ for Quench and Slow Cooled FAFP mixtures')
plt.legend()
plt.show()
# %%
plt.plot(QuenchFAFPmeltTemps[:,0], QuenchFAFPmeltTemps[:,1], 'v', color = 'blue', label = r'Quench Cooled')
plt.plot(SlowFAFPmeltTemps[:,0], SlowFAFPmeltTemps[:,1], '^', color = 'orange', label = r'Slow Cooled')
plt.xlabel(r'$x_{AFP}$ [mMol]', loc = 'right', fontsize = 12)
plt.ylabel(r'$T_M$ [K]', loc = 'top', fontsize = 12, rotation = 0)
plt.title(r'$T_M$ for Quench and Slow Cooled FAFP mixtures')
plt.legend()
plt.show()
# %%
'''