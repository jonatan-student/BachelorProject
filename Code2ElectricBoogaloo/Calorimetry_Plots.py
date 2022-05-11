# %%
from cProfile import label
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


#------Importing all data for quench spectrum of pure mixtures
Q010 = pd.read_csv('quench010.csv', sep = ';')
Q023 = pd.read_csv('quench023.csv', sep = ';')
Q030 = pd.read_csv('quench030.csv', sep = ';')
Q040 = pd.read_csv('quench040.csv', sep = ';')
Q050 = pd.read_csv('quench050.csv', sep = ';')
Q060 = pd.read_csv('quench060.csv', sep = ';')

#----Importing all data for slow spectrum of pure mixtures
S010 = pd.read_csv('slow010.csv', sep = ';')
S023 = pd.read_csv('slow023.csv', sep = ';')
S030 = pd.read_csv('slow030.csv', sep = ';')
S040 = pd.read_csv('slow040.csv', sep = ';')
S050 = pd.read_csv('slow050.csv', sep = ';')
S060 = pd.read_csv('slow060.csv', sep = ';')


#importing data from sources on eutectic stuff
PCCP17 = pd.read_csv('PCCP17Dielectrics.csv', sep = ',')
PCCP18 = pd.read_csv('PCCP18Dielectrics.csv', sep = ',')
MeltingPts = pd.read_csv('Meltingpoints.csv', sep = ',')
jnoncryst = pd.read_csv('jnoncrystDIelectrics.csv', sep = ',')
Jensen2018 = pd.read_csv('OtherCalorimetry.csv', sep = ',')

#our recorded glass transistion temperatures
QuenchGlassTemps = np.array([
    [0.1, 165.25588],
    [0.23, 158.66368],
    [0.3, 164.19232],
    [0.4, 170.76896],
    [0.5, 174.6105],
    [0.6, 178.4962],
    [0.995, 192.57806]
])

QuenchBUFglassTemps = np.array([
    [0.047, 167.718],
    [0.23, 168.37106],
])

QuenchIAFPglassTemps = np.array([
    [0.047, 149.29744],
    [0.23, 152.62754],
])

SlowGlassTemps = np.array([
    [0.1, 166.6226],
    [0.23, 157.7882],
    [0.3, 163.5615],
    [0.4, 169.96457],
    [0.5, 174.55885],
    [0.6, 178.4962],
    [0.995, 190.9186]
])

SlowBUFglassTemps = np.array([
    [0.047, 167.6755],
    [0.23, 169.67588]
])

SlowIAFPglassTemps = np.array([
    [0.047, 167.3746],
    [0.23, 167.8094]
])

#recorded melting temperatures

QuenchMeltTemps = np.array([
    [0.0, 273.5821],
    [0.1, 259.00216],
    [0.23, 236.96968]
])

QuenchBUFmeltTemps = np.array([
    [0.047, 268.12862],
    [0.23, 260.32991]
])

QuenchIAFPmeltTemps = np.array([
    [0.047, 267.61076],
    [0.23, 258.0819]
])

SlowMeltTemps = np.array([
    [0.0, 272.96392],
    [0.1, 259.48404],
    [0.23, 236.4474]
])

SlowBUFmeltTemps = np.array([
    [0.047, 267.5991],
    [0.23, 260.82549]
])

SlowIAFPmeltTemps = np.array([
    [0.047, 268.47984],
    [0.23, 258.19806]
])


#-----Isolating data around glass transition by cutting the data-
# ----to a range on the x axis and limiting it to above 0 on the y axis
GlycerolQuenchGlass = GlycerolQuench[(GlycerolQuench['T']> 150) & (GlycerolQuench['T']< 210) & (GlycerolQuench['dTdt [K/s]']>0) ]
GlycerolSlowGlass = GlycerolSlow[(GlycerolSlow['T [K]']> 150) & (GlycerolSlow['T [K]']< 210) & (GlycerolSlow['dTdt [K/s]']>0) ]

#quench tests at glass transition
Q010glass = Q010[(Q010['T [K] '] > 150) & (Q010['T [K] '] < 210) & (Q010[' dTdt [K/s] '] > 0)]
Q023glass = Q023[(Q023['T [K] '] > 150) & (Q023['T [K] '] < 210) & (Q023[' dTdt [K/s] '] > 0)]
Q030glass = Q030[(Q030['T [K] '] > 150) & (Q030['T [K] '] < 210) & (Q030[' dTdt [K/s] '] > 0)]
Q040glass = Q040[(Q040['T [K] '] > 150) & (Q040['T [K] '] < 210) & (Q040[' dTdt [K/s] '] > 0)]
Q050glass = Q050[(Q050['T[K] '] > 150) & (Q050['T[K] '] < 210) & (Q050[' dTdt [K/s] '] > 0) & (Q050[' dTdt [K/s] '] < 0.35)]
Q060glass = Q060[(Q060['T[K] '] > 150) & (Q060['T[K] '] < 210) & (Q060[' dTdt [K/s] '] > 0)]

#slow tests at glass transition time is also a cutting factor here as crystalization in cooling makes for messy data
S010glass = S010[(S010['T [K] '] > 150) & (S010['T [K] '] < 200) & (S010[' dTdt [K/s] '] > 0) & (S010[' etime [s] '] > 1000)]
S023glass = S023[(S023['T [K] '] > 150) & (S023['T [K] '] < 200) & (S023[' dTdt [K/s] '] > 0) & (S023[' etime [s] '] > 1000)]
S030glass = S030[(S030['T [K] '] > 150) & (S030['T [K] '] < 200) & (S030[' dTdt [K/s] '] > 0) & (S030[' etime [s] '] > 1000)]
S040glass = S040[(S040['T [K] '] > 150) & (S040['T [K] '] < 200) & (S040[' dTdt [K/s] '] > 0) & (S040[' etime [s] '] > 1000)]
S050glass = S050[(S050['T [K] '] > 150) & (S050['T [K] '] < 200) & (S050[' dTdt [K/s] '] > 0) & (S050[' etime [s] '] > 1000)]
S060glass = S060[(S060['T [K] '] > 150) & (S060['T [K] '] < 200) & (S060[' dTdt [K/s] '] > 0) & (S010[' etime [s] '] > 1000)]

#Quench tests glasses for mixtures with stuff added
BUF_Q023glass = BUFQ023[(BUFQ023['T [K] '] > 140) & (BUFQ023['T [K] '] < 200) & (BUFQ023[' dTdt [K/s] '] > 0)]
IAFP_Q023glass = IAFPQ023[(IAFPQ023['T [K] '] > 140) & (IAFPQ023['T [K] '] < 200) & (IAFPQ023[' dTdt [K/s] '] > 0)]
BSA_Q023glass = BSAQ023[(BSAQ023['T [K] '] > 140) & (BSAQ023['T [K] '] < 200) & (BSAQ023[' dTdt [K/s] '] > 0)]

BUF_Q0047glass = BUFQ0047[(BUFQ0047['T [K] '] > 140) & (BUFQ0047['T [K] '] < 200) & (BUFQ0047[' dTdt [K/s] '] > 0)]
IAFP_Q0047glass = IAFPQ0047[(IAFPQ0047['T [K] '] > 140) & (IAFPQ0047['T [K] '] < 200) & (IAFPQ0047[' dTdt [K/s] '] > 0)]
#BSA_Q0047glass = BSAQ0047[(BSAQ0047['T [K] '] > 140) & (BSAQ0047['T [K] '] < 200) & (BSAQ0047[' dTdt [K/s] '] > 0)]



#Slow Test glasses for mixtures with stuff added
BUF_S023glass = BUFS023[(BUFS023['T [K] '] > 140) & (BUFS023['T [K] '] < 200) & (BUFS023[' dTdt [K/s] '] > 0) & (BUFS023[' etime [s] '] > 1000)]
IAFP_S023glass = IAFPS023[(IAFPS023['T [K] '] > 140) & (IAFPS023['T [K] '] < 200) & (IAFPS023[' dTdt [K/s] '] > 0) & (IAFPS023[' etime [s] '] > 1000)]
BSA_S023glass = BSAS023[(BSAS023['T [K] '] > 140) & (BSAS023['T [K] '] < 200) & (BSAS023[' dTdt [K/s] '] > 0) & (BSAS023[' etime [s] '] > 1000)]

BUF_S0047glass = BUFS0047[(BUFS0047['T [K] '] > 160) & (BUFS0047['T [K] '] < 180) & (BUFS0047[' dTdt [K/s] '] > 0) & (BUFS0047[' etime [s] '] > 1000)]
IAFP_S0047glass = IAFPS0047[(IAFPS0047['T [K] '] > 140) & (IAFPS0047['T [K] '] < 200) & (IAFPS0047[' dTdt [K/s] '] > 0) & (IAFPS0047[' etime [s] '] > 1000)]
#BSA_S0047glass = BSAS0047[(BSAS0047['T [K] '] > 140) & (BSAS0047['T [K] '] < 200) & (BSAS0047[' dTdt [K/s] '] > 0) & (BSAS0047[' etime [s] '] > 1000)]


#-----Isolating data around Melting temperature
#pure
WaterQuenchMelt = WaterQuench[(WaterQuench['T']> 265) & (WaterQuench['dTdt [K/s]'] > 0)]
WaterSlowMelt = WaterSlow[(WaterSlow['T']> 265) & (WaterSlow['dTdt [K/s]'] > 0) & (WaterSlow['etime [s]']> 1000)]

#quench melting temperatures
Q010Melt = Q010[(Q010['T [K] '] > 200) & (Q010['T [K] '] < 280) & (Q010[' dTdt [K/s] '] > 0) & (Q010[' etime [s] ']> 500)]
Q023Melt = Q023[(Q023['T [K] '] > 200) & (Q023['T [K] '] < 280) & (Q023[' dTdt [K/s] '] > 0) & (Q023[' etime [s] ']> 500)]
Q030Melt = Q030[(Q030['T [K] '] > 200) & (Q030['T [K] '] < 280) & (Q030[' dTdt [K/s] '] > 0) & (Q030[' etime [s] ']> 500)]
Q040Melt = Q040[(Q040['T [K] '] > 200) & (Q040['T [K] '] < 280) & (Q040[' dTdt [K/s] '] > 0) & (Q040[' etime [s] ']> 500)]
Q050Melt = Q050[(Q050['T[K] '] > 200) & (Q050['T[K] '] < 280) & (Q050[' dTdt [K/s] '] > 0) & (Q050[' etime [s] ']> 500)]
Q060Melt = Q060[(Q060['T[K] '] > 200) & (Q060['T[K] '] < 280) & (Q060[' dTdt [K/s] '] > 0) & (Q060[' etime [s] ']> 500)]

#Slow melting temperatures
S010Melt = S010[(S010['T [K] '] > 200) & (S010['T [K] '] < 280) & (S010[' dTdt [K/s] '] > 0)  & (S010[' etime [s] ']> 1000)]
S023Melt = S023[(S023['T [K] '] > 200) & (S023['T [K] '] < 280) & (S023[' dTdt [K/s] '] > 0)  & (S023[' etime [s] ']> 1000)]
S030Melt = S030[(S030['T [K] '] > 200) & (S030['T [K] '] < 280) & (S030[' dTdt [K/s] '] > 0)  & (S030[' etime [s] ']> 1000)]
S040Melt = S040[(S040['T [K] '] > 200) & (S040['T [K] '] < 280) & (S040[' dTdt [K/s] '] > 0)  & (S040[' etime [s] ']> 1000)]
S050Melt = S050[(S050['T [K] '] > 200) & (S050['T [K] '] < 280) & (S050[' dTdt [K/s] '] > 0)  & (S050[' etime [s] ']> 1000)]
S060Melt = S060[(S060['T [K] '] > 200) & (S060['T [K] '] < 280) & (S060[' dTdt [K/s] '] > 0)  & (S060[' etime [s] ']> 1000)]


#melting for mixtures with stuff added
#Quench melts
BUF_Q023Melt = BUFQ023[(BUFQ023['T [K] '] > 200) & (BUFQ023['T [K] '] < 280) & (BUFQ023[' dTdt [K/s] '] > 0)]
IAFP_Q023Melt = IAFPQ023[(IAFPQ023['T [K] '] > 200) & (IAFPQ023['T [K] '] < 280) & (IAFPQ023[' dTdt [K/s] '] > 0)]
BSA_Q023Melt = BSAQ023[(BSAQ023['T [K] '] > 200) & (BSAQ023['T [K] '] < 280) & (BSAQ023[' dTdt [K/s] '] > 0)]

BUF_Q0047Melt = BUFQ0047[(BUFQ0047['T [K] '] > 200) & (BUFQ0047['T [K] '] < 280) & (BUFQ0047[' dTdt [K/s] '] > 0)]
IAFP_Q0047Melt = IAFPQ0047[(IAFPQ0047['T [K] '] > 200) & (IAFPQ0047['T [K] '] < 280) & (IAFPQ0047[' dTdt [K/s] '] > 0)]
#Slow melts
BUF_S023Melt = BUFS023[(BUFS023['T [K] '] > 200) & (BUFS023['T [K] '] < 280) & (BUFS023[' dTdt [K/s] '] > 0) & (BUFS023[' etime [s] '] > 1000)]
IAFP_S023Melt = IAFPS023[(IAFPS023['T [K] '] > 200) & (IAFPS023['T [K] '] < 280) & (IAFPS023[' dTdt [K/s] '] > 0) & (IAFPS023[' etime [s] '] > 1000)]
BSA_S023Melt = BSAS023[(BSAS023['T [K] '] > 200) & (BSAS023['T [K] '] < 280) & (BSAS023[' dTdt [K/s] '] > 0) & (BSAS023[' etime [s] '] > 1000)]

BUF_S0047Melt = BUFS0047[(BUFS0047['T [K] '] > 200) & (BUFS0047['T [K] '] < 280) & (BUFS0047[' dTdt [K/s] '] > 0) & (BUFS0047[' etime [s] '] > 1000)]
IAFP_S0047Melt = IAFPS0047[(IAFPS0047['T [K] '] > 200) & (IAFPS0047['T [K] '] < 280) & (IAFPS0047[' dTdt [K/s] '] > 0) & (IAFPS0047[' etime [s] '] > 1000)]



#-------reduction of noise by rolling average
n=50

#___glasses__
#quench
Q010glass = Q010glass.rolling(n).mean()
Q023glass = Q023glass.rolling(n).mean()
Q030glass = Q030glass.rolling(n).mean()
Q040glass = Q040glass.rolling(n).mean()
Q050glass = Q050glass.rolling(n).mean()
Q060glass = Q060glass.rolling(n).mean()
GlycerolQuenchGlass = GlycerolQuenchGlass.rolling(n).mean()

#slow
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
#BSA_Q0047glass = BSA_Q0047glass.rolling(n).mean()

#slow+stuff
BUF_S023glass = BUF_S023glass.rolling(n).mean()
IAFP_S023glass = IAFP_S023glass.rolling(n).mean()
#BSA_S023glass = BSA_S023glass.rolling(n).mean()

BUF_S0047glass = BUF_S0047glass.rolling(n).mean()
IAFP_S0047glass = IAFP_S0047glass.rolling(n).mean()
#BSA_S0047glass = BSA_S0047glass.rolling(n).mean()

#__MELTING__

#quench
WaterQuenchMelt = WaterQuenchMelt.rolling(n).mean()
Q010Melt = Q010Melt.rolling(n).mean()
Q023Melt = Q023Melt.rolling(n).mean()
Q030Melt = Q030Melt.rolling(n).mean()
Q040Melt = Q040Melt.rolling(n).mean()
Q050Melt = Q050Melt.rolling(n).mean()
Q060Melt = Q060Melt.rolling(n).mean()

#slow
WaterSlowMelt = WaterSlowMelt.rolling(n).mean()
S010Melt = S010Melt.rolling(n).mean()
S023Melt = S023Melt.rolling(n).mean()
S030Melt = S030Melt.rolling(n).mean()
S040Melt = S040Melt.rolling(n).mean()
S050Melt = S050Melt.rolling(n).mean()
S060Melt = S060Melt.rolling(n).mean()

#quench+stuff
BUF_Q023Melt = BUF_Q023Melt.rolling(n).mean()
IAFP_Q023Melt = IAFP_Q023Melt.rolling(n).mean()
BSA_Q023Melt = BSA_Q023Melt.rolling(n).mean()

BUF_Q0047Melt = BUF_Q0047Melt.rolling(n).mean()
IAFP_Q0047Melt = IAFP_Q0047Melt.rolling(n).mean()
#BSA_Q0047Melt = BSA_Q0047Melt.rolling(n).mean()

#slow+stuff
BUF_S023Melt = BUF_S023Melt.rolling(n).mean()
IAFP_S023Melt = IAFP_S023Melt.rolling(n).mean()
BSA_S023Melt = BSA_S023Melt.rolling(n).mean()

BUF_S0047Melt = BUF_S0047Melt.rolling(n).mean()
IAFP_S0047Melt = IAFP_S0047Melt.rolling(n).mean()
#BSA_S0047Melt = BSA_S0047Melt.rolling(n).mean()

#------Differentiating the data

#quench tests
Q010glassDiff = Q010glass.diff(axis = 0, periods= 1)
Q023glassDiff = Q023glass.diff(axis = 0, periods= 1)
Q030glassDiff = Q030glass.diff(axis = 0, periods= 1)
Q040glassDiff = Q040glass.diff(axis = 0, periods= 1)
Q050glassDiff = Q050glass.diff(axis = 0, periods= 1)
Q060glassDiff = Q060glass.diff(axis = 0, periods= 1)
Q010MeltDiff = Q010Melt.diff(axis = 0, periods = 1)
Q023MeltDiff = Q023Melt.diff(axis = 0, periods = 1)
Q030MeltDiff = Q030Melt.diff(axis = 0, periods = 1)
Q040MeltDiff = Q040Melt.diff(axis = 0, periods = 1)
Q050MeltDiff = Q050Melt.diff(axis = 0, periods = 1)
Q060MeltDiff = Q060Melt.diff(axis = 0, periods = 1)

#Slow tests
S010glassDiff = S010glass.diff(axis = 0, periods= 1)
S023glassDiff = S023glass.diff(axis = 0, periods= 1)
S030glassDiff = S030glass.diff(axis = 0, periods= 1)
S040glassDiff = S040glass.diff(axis = 0, periods= 1)
S050glassDiff = S050glass.diff(axis = 0, periods= 1)
S060glassDiff = S060glass.diff(axis = 0, periods= 1)
S010MeltDiff = S010Melt.diff(axis = 0, periods = 1)
S023MeltDiff = S023Melt.diff(axis = 0, periods = 1)
S030MeltDiff = S030Melt.diff(axis = 0, periods = 1)
S040MeltDiff = S040Melt.diff(axis = 0, periods = 1)
S050MeltDiff = S050Melt.diff(axis = 0, periods = 1)
S060MeltDiff = S060Melt.diff(axis = 0, periods = 1)


#--23 with stuff
#glasss
BUF_Q023glassDiff = BUF_Q023glass.diff(axis = 0, periods= 1)
IAFP_Q023glassDiff = IAFP_Q023glass.diff(axis = 0, periods= 1)
BSA_Q023glassDiff = BSA_Q023glass.diff(axis = 0, periods= 1)

BUF_S023glassDiff = BUF_S023glass.diff(axis=0, periods=1)
IAFP_S023glassDiff = IAFP_S023glass.diff(axis=0, periods=1)
BSA_S023glassDiff = BSA_S023glass.diff(axis=0, periods=1)

BUF_Q0047glassDiff = BUF_Q0047glass.diff(axis = 0, periods= 1)
IAFP_Q0047glassDiff = IAFP_Q0047glass.diff(axis = 0, periods= 1)
#BSA_Q0047glassDiff = BSA_Q0047glass.diff(axis = 0, periods= 1)

BUF_S0047glassDiff = BUF_S0047glass.diff(axis=0, periods=1)
IAFP_S0047glassDiff = IAFP_S0047glass.diff(axis=0, periods=1)
#BSA_S0047glassDiff = BSA_S0047glass.diff(axis=0, periods=1)

#melting
BUF_Q023MeltDiff = BUF_Q023Melt.diff(axis = 0, periods= 1)
IAFP_Q023MeltDiff = IAFP_Q023Melt.diff(axis = 0, periods= 1)
BSA_Q023MeltDiff = BSA_Q023Melt.diff(axis = 0, periods= 1)

BUF_S023MeltDiff = BUF_S023Melt.diff(axis=0, periods=1)
IAFP_S023MeltDiff = IAFP_S023Melt.diff(axis=0, periods=1)
BSA_S023MeltDiff = BSA_S023Melt.diff(axis=0, periods=1)

BUF_Q0047MeltDiff = BUF_Q0047Melt.diff(axis = 0, periods= 1)
IAFP_Q0047MeltDiff = IAFP_Q0047Melt.diff(axis = 0, periods= 1)
#BSA_Q0047MeltDiff = BSA_Q0047Melt.diff(axis = 0, periods= 1)

BUF_S0047MeltDiff = BUF_S0047Melt.diff(axis=0, periods=1)
IAFP_S0047MeltDiff = IAFP_S0047Melt.diff(axis=0, periods=1)
#BSA_S0047MeltDiff = BSA_S0047Melt.diff(axis=0, periods=1)

#--pure stuff
WaterQuenchMeltDiff= WaterQuenchMelt.diff(axis = 0, periods = 1)
WaterSlowMeltDiff= WaterSlowMelt.diff(axis = 0, periods = 1)

GlycerolQuenchGlassDiff = GlycerolQuenchGlass.diff(axis = 0, periods=1)
GlycerolSlowGlassDiff = GlycerolSlowGlass.diff(axis=0, periods=1)

# %%

#Finding Glass transition temperatures for quench tests
print('Q010')
print(Q010glass['T [K] '].get(Q010glassDiff[' dTdt [K/s] '].idxmin()))
print('Q023')
print(Q023glass['T [K] '].get(Q023glassDiff[' dTdt [K/s] '].idxmin()))
print('Q030')
print(Q030glass['T [K] '].get(Q030glassDiff[' dTdt [K/s] '].idxmin()))
print('Q040')
print(Q040glass['T [K] '].get(Q040glassDiff[' dTdt [K/s] '].idxmin()))
print('Q050')
print(Q050glass['T[K] '].get(Q050glassDiff[' dTdt [K/s] '].idxmin()))
print('Q060')
print(Q060glass['T[K] '].get(Q060glassDiff[' dTdt [K/s] '].idxmin()))
print('Quench pure Glycerol')
print(GlycerolQuenchGlass['T'].get(GlycerolQuenchGlassDiff['dTdt [K/s]'].idxmin()))
print('BUF Q023')
print(BUF_Q023glass['T [K] '].get(BUF_Q023glassDiff[' dTdt [K/s] '].idxmin()))
print('BSA Q023')
print(BSA_Q023glass['T [K] '].get(BSA_Q023glassDiff[' dTdt [K/s] '].idxmin()))
print('IAFP Q023')
print(IAFP_Q023glass['T [K] '].get(IAFP_Q023glassDiff[' dTdt [K/s] '].idxmin()))
print('BUF-0047')
print(BUF_Q0047glass['T [K] '].get(BUF_Q0047glassDiff[' dTdt [K/s] '].idxmin()))
#print('BSA Q0047')
#print(BSA_Q0047glass['T [K] '].get(BSA_Q0047glassDiff[' dTdt [K/s] '].idxmin()))
print('IAFP Q0047')
print(IAFP_Q0047glass['T [K] '].get(IAFP_Q0047glassDiff[' dTdt [K/s] '].idxmin()))

# %%

#Finding and returning Tg for slow tests
print('S010')
print(S010glass['T [K] '].get(S010glassDiff[' dTdt [K/s] '].idxmin()))
print('S023')
print(S023glass['T [K] '].get(S023glassDiff[' dTdt [K/s] '].idxmin()))
print('S030')
print(S030glass['T [K] '].get(S030glassDiff[' dTdt [K/s] '].idxmin()))
print('S040')
print(S040glass['T [K] '].get(S040glassDiff[' dTdt [K/s] '].idxmin()))
print('S050')
print(S050glass['T [K] '].get(S050glassDiff[' dTdt [K/s] '].idxmin()))
print('S060')
print(S060glass['T [K] '].get(S060glassDiff[' dTdt [K/s] '].idxmin()))
print('Slow pure Glycerol')
print(GlycerolSlowGlass['T [K]'].get(GlycerolSlowGlassDiff['dTdt [K/s]'].idxmin()))
print('BUF S023')
print(BUF_S023glass['T [K] '].get(BUF_S023glassDiff[' dTdt [K/s] '].idxmin()))
print('BSA S023')
print(BSA_S023glass['T [K] '].get(BSA_S023glassDiff[' dTdt [K/s] '].idxmin()))
print('IAFP S023')
print(IAFP_S023glass['T [K] '].get(IAFP_S023glassDiff[' dTdt [K/s] '].idxmin()))
print('BUF S0047')
print(BUF_S0047glass['T [K] '].get(BUF_S0047glassDiff[' dTdt [K/s] '].idxmin()))
#print('BSA S0047')
#print(BSA_S0047glass['T [K] '].get(BSA_S0047glassDiff[' dTdt [K/s] '].idxmin()))
print('IAFP S0047')
print(IAFP_S0047glass['T [K] '].get(IAFP_S0047glassDiff[' dTdt [K/s] '].idxmin()))

# %%
#Quench meltings
print('Melting temperatures:')
print('Q000')
print(WaterQuenchMelt['T'].get(WaterQuenchMeltDiff['dTdt [K/s]'].idxmax()))
print('Q010')
print(Q010Melt['T [K] '].get(Q010MeltDiff[' dTdt [K/s] '].idxmax()))
print('Q023')
print(Q023Melt['T [K] '].get(Q023MeltDiff[' dTdt [K/s] '].idxmax()))
print('BUF Q023')
print(BUF_Q023Melt['T [K] '].get(BUF_Q023MeltDiff[' dTdt [K/s] '].idxmax()))
print('BSA Q023')
print(BSA_Q023Melt['T [K] '].get(BSA_Q023MeltDiff[' dTdt [K/s] '].idxmax()))
print('IAFP Q023')
print(IAFP_Q023Melt['T [K] '].get(IAFP_Q023MeltDiff[' dTdt [K/s] '].idxmax()))
print('BUF Q0047')
print(BUF_Q0047Melt['T [K] '].get(BUF_Q0047MeltDiff[' dTdt [K/s] '].idxmax()))
#print('BSA Q0047')
#print(BSA_Q0047Melt['T [K] '].get(BSA_Q0047MeltDiff[' dTdt [K/s]'].idxmax()))
print('IAFP Q0047')
print(IAFP_Q0047Melt['T [K] '].get(IAFP_Q0047MeltDiff[' dTdt [K/s] '].idxmax()))

#%%

#Slow meltings
print('S000')
print(WaterSlowMelt['T'].get(WaterSlowMeltDiff['dTdt [K/s]'].idxmax()))
print('S010')
print(S010Melt['T [K] '].get(S010MeltDiff[' dTdt [K/s] '].idxmax()))
print('S023')
print(S023Melt['T [K] '].get(S023MeltDiff[' dTdt [K/s] '].idxmax()))
print('BUF S023')
print(BUF_S023Melt['T [K] '].get(BUF_S023MeltDiff[' dTdt [K/s] '].idxmax()))
print('IAFP S023')
print(IAFP_S023Melt['T [K] '].get(IAFP_S023MeltDiff[' dTdt [K/s] '].idxmax()))
print('BUF S0047')
print(BUF_S0047Melt['T [K] '].get(BUF_S0047MeltDiff[' dTdt [K/s] '].idxmax()))
#print('BSA Q0047')
#print(BSA_Q0047Melt['T [K] '].get(BSA_Q0047MeltDiff[' dTdt [K/s]'].idxmax()))
print('IAFP S0047')
print(IAFP_S0047Melt['T [K] '].get(IAFP_S0047MeltDiff[' dTdt [K/s] '].idxmax()))




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
plt.plot(WaterQuenchMelt['T'], WaterQuenchMelt['dTdt [K/s]'], label ='Quench Cooling')
plt.plot(Q010Melt['T [K] '], Q010Melt[' dTdt [K/s] '], label = '0.1')
plt.plot(Q023Melt['T [K] '], Q023Melt[' dTdt [K/s] '], label = '0.23')
plt.legend()
plt.title('Melting temperatures of Quench Cooled Glycerol Water Mixtures')
plt.show()


# %%
#EUTECTIC GRAPH PLOT


plt.plot(PCCP17['x'], PCCP17[' y'],'^', color = 'b', label = 'DSC (Bachler 16)')
plt.plot(PCCP18['x'], PCCP18[' y'], '>',  color = 'b', label = 'DSC (Popov 2015)')
plt.plot(jnoncryst['x'], jnoncryst[' y'], '*',  color = 'b', label = 'Dialectrics (Hayashi 2005)')
plt.plot(MeltingPts['x'], MeltingPts[' y'],'x',  color = 'b', label = 'Melting Temperatures (Lane 1925)')
plt.plot(Jensen2018['x'], Jensen2018[' y'],'d',  color = 'b', label = 'TC (Jensen 2018)')
plt.plot(QuenchGlassTemps[:,0], QuenchGlassTemps[:,1], 'h',  color = 'r', label = 'TC [Quench] (Our work)')
plt.plot(SlowGlassTemps[:,0], SlowGlassTemps[:,1], 'o',  color = 'r', label = 'TC [Slow] (Our work)')
plt.plot(QuenchMeltTemps[:,0], QuenchMeltTemps[:,1], '+',  color = 'r', label = 'Melting Temperatures (Our work)')
plt.xlabel('Xgly')
plt.ylabel('Temperature [K]')
plt.legend()
plt.title('Phase Diagram of Glycerol-Water')
plt.show()
# %%


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
plt.plot(WaterQuenchMelt['T'], WaterQuenchMeltDiff['dTdt [K/s]'], label = 0.0)
plt.plot(Q010Melt['T [K] '], Q010MeltDiff[' dTdt [K/s] '], label = 0.1)
plt.plot(Q023Melt['T [K] '], Q023MeltDiff[' dTdt [K/s] '], label = 0.23)
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
