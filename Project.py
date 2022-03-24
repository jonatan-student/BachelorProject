from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.function_base import linspace
from numpy.lib.polynomial import poly, polyval
import pandas as pd
from scipy.optimize import curve_fit

##Import Data into Pandas Data-Frames
#Base tests
WaterQuench = pd.read_csv('CSVs\Watertest1.csv', sep = ';')
WaterSlow = pd.read_csv('CSVs\Watertest2.csv', sep = ';')
GlycerolQuench = pd.read_csv('CSVs\Glyceroltest1.csv', sep = ';')
GlycerolSlow = pd.read_csv('CSVs\Glyceroltest2.csv', sep = ';')

#glycerol concentrations alone
Q020 = pd.read_csv()
Q030 = pd.read_csv()
Q040 = pd.read_csv()
Q050 = pd.read_csv('CSVs\quench050.csv', sep = ';')
Q050warm = Q050[(Q050[' etime [s] '] > 70)]
Q050cool = Q050[(Q050[' etime [s] '] < 70)] *-1
Q060 = pd.read_csv('CSVs\quench060.csv', sep = ';')
S020 = pd.read_csv()
S030 = pd.read_csv()
S040 = pd.read_csv()
S050 = pd.read_csv('CSVs\slow050.csv', sep = ';')
S060 = pd.read_csv('CSVs\slow060.csv', sep = ';')

##-----data Manipulation----##
#_data around glass temperature_#
#-quench-#
Q020glass = Q020[(Q020[' etime [s] '] > 550) & (Q020[' etime [s] ']<900)]
Q030glass = Q030[(Q030[' etime [s] '] > 550) & (Q030[' etime [s] ']<900)]
Q040glass = Q040[(Q040[' etime [s] '] > 550) & (Q040[' etime [s] ']<900)]
Q050glass = Q050[(Q050[' etime [s] '] > 550) & (Q050[' etime [s] ']<900)]
Q060glass = Q060[(Q060[' etime [s] '] > 300) & (Q060[' etime [s] ']<700)]
#-slow-#
S020glass = S020[(S020[' etime [s] '] > 550) & (S020[' etime [s] ']<900)]
S030glass = S030[(S030[' etime [s] '] > 550) & (S030[' etime [s] ']<900)]
S040glass = S040[(S040[' etime [s] '] > 550) & (S040[' etime [s] ']<900)]
S050glass = S050[(S050[' etime [s] '] > 550) & (S050[' etime [s] ']<900)]
S060glass = S060[(S060[' etime [s] '] > 300) & (S060[' etime [s] ']<700)]



#reducion of noise by rolling average
#quench
Q020glass = Q020glass.rolling(7).mean()
Q030glass = Q030glass.rolling(7).mean()
Q040glass = Q040glass.rolling(7).mean()
Q050glass = Q050glass.rolling(7).mean()
Q060glass = Q060glass.rolling(7).mean()
#slow
S020glass = S020glass.rolling(7).mean()
S030glass = S030glass.rolling(7).mean()
S040glass = S040glass.rolling(7).mean()
S050glass = S050glass.rolling(7).mean()
S060glass = S060glass.rolling(7).mean()

#differentiated data
#quench
Q020glassDiff = Q020glass.diff(axis = 0, periods= 1)
Q030glassDiff = Q030glass.diff(axis = 0, periods= 1)
Q040glassDiff = Q040glass.diff(axis = 0, periods= 1)
Q050glassDiff = Q050glass.diff(axis = 0, periods= 1)
Q060glassDiff = Q060glass.diff(axis = 0, periods= 1)
#slow
S020glassDiff = S020glass.diff(axis = 0, periods= 1)
S030glassDiff = S030glass.diff(axis = 0, periods= 1)
S040glassDiff = S040glass.diff(axis = 0, periods= 1)
S050glassDiff = S050glass.diff(axis = 0, periods= 1)
S060glassDiff = S060glass.diff(axis = 0, periods= 1)

#producing glass transition temperature by local minima
def glasstransition():
    #quench
    print(Q020glass['T[K] '].get(Q020glassDiff[' dTdt [K/s] '].idxmin()))
    print(Q030glass['T[K] '].get(Q030glassDiff[' dTdt [K/s] '].idxmin()))
    print(Q040glass['T[K] '].get(Q040glassDiff[' dTdt [K/s] '].idxmin()))
    print(Q050glass['T[K] '].get(Q050glassDiff[' dTdt [K/s] '].idxmin()))
    print(Q060glass['T[K] '].get(Q060glassDiff[' dTdt [K/s] '].idxmin()))
    #slow
    print(S020glass['T[K] '].get(S020glassDiff[' dTdt [K/s] '].idxmin()))
    print(S030glass['T[K] '].get(S030glassDiff[' dTdt [K/s] '].idxmin()))
    print(S040glass['T[K] '].get(S040glassDiff[' dTdt [K/s] '].idxmin()))
    print(S050glass['T[K] '].get(S050glassDiff[' dTdt [K/s] '].idxmin()))
    print(S060glass['T[K] '].get(S060glassDiff[' dTdt [K/s] '].idxmin()))


###plots
#plotting of glass transition temperatures
def GTplots():
    plt.plot(Q020glass['T[K] '], Q020glass[' dTdt [K/s] '], label = '0.2')
    plt.plot(Q030glass['T[K] '], Q030glass[' dTdt [K/s] '], label = '0.3')
    plt.plot(Q040glass['T[K] '], Q040glass[' dTdt [K/s] '], label = '0.4')
    plt.plot(Q050glass['T[K] '], Q050glass[' dTdt [K/s] '], label = '0.5')
    plt.plot(Q060glass['T[K] '], Q060glass[' dTdt [K/s] '], label = '0.6')
    plt.legend()
    plt.show()

    plt.plot(S020glass['T[K] '], S020glass[' dTdt [K/s] '], label = '0.2')
    plt.plot(S030glass['T[K] '], S030glass[' dTdt [K/s] '], label = '0.3')
    plt.plot(S040glass['T[K] '], S040glass[' dTdt [K/s] '], label = '0.4')
    plt.plot(S050glass['T[K] '], S050glass[' dTdt [K/s] '], label = '0.5')
    plt.plot(S060glass['T[K] '], S060glass[' dTdt [K/s] '], label = '0.6')
    plt.legend()
    plt.show()

#plotting differentiated data
def DiffGT():
    plt.plot(Q020glass['T[K] '], Q020glassDiff[' dTdt [K/s] '], label = '0.2')
    plt.plot(Q030glass['T[K] '], Q030glassDiff[' dTdt [K/s] '], label = '0.3')
    plt.plot(Q040glass['T[K] '], Q040glassDiff[' dTdt [K/s] '], label = '0.4')
    plt.plot(Q050glass['T[K] '], Q050glassDiff[' dTdt [K/s] '], label = '0.5')
    plt.plot(Q060glass['T[K] '], Q060glassDiff[' dTdt [K/s] '], label = '0.6')
    plt.legend()
    plt.title("Derived")
    plt.show()

    plt.plot(S020glass['T[K] '], S020glassDiff[' dTdt [K/s] '], label = '0.2')
    plt.plot(S030glass['T[K] '], S030glassDiff[' dTdt [K/s] '], label = '0.3')
    plt.plot(S040glass['T[K] '], S040glassDiff[' dTdt [K/s] '], label = '0.4')
    plt.plot(S050glass['T[K] '], S050glassDiff[' dTdt [K/s] '], label = '0.5')
    plt.plot(S060glass['T[K] '], S060glassDiff[' dTdt [K/s] '], label = '0.6')
    plt.legend()
    plt.title("Derived")
    plt.show()

#plotting full dataset
def fullSetQuench():
    plt.plot(WaterQuench['T'], WaterQuench['dTdt [K/s]'], label = "pure water")
    plt.plot(GlycerolQuench['T'], GlycerolQuench['dTdt [K/s]'], label = 'pure glycerol')
    plt.plot(Q020['T[K] '], Q020[' dTdt [K/s] '], label = '0.2 concentration')
    plt.plot(Q030['T[K] '], Q030[' dTdt [K/s] '], label = '0.3 concentration')
    plt.plot(Q040['T[K] '], Q040[' dTdt [K/s] '], label = '0.4 concentration')
    plt.plot(Q050cool['T[K] '], Q050cool[' dTdt [K/s] '], label = '0.5 concentration')
    plt.plot(Q050warm['T[K] '], Q050warm[' dTdt [K/s] '], label = '0.5 concentration')
    plt.plot(Q060['T[K] '], Q060[' dTdt [K/s] '], label = '0.6 concentration')
    plt.title('Quench cooling for full set')
    plt.legend()
    plt.xlabel('T[K]')
    plt.ylabel('dTdt [K/s]')
    plt.show()

def fullSetSlow():
    plt.plot(WaterSlow['T'], WaterSlow['dTdt [K/s]'], label = "pure water")
    plt.plot(GlycerolSlow['T'], GlycerolSlow['dTdt [K/s]'], label = 'pure glycerol')
    plt.plot(Q020['T[K] '], S020[' dTdt [K/s] '], label = '0.2 concentration')
    plt.plot(Q030['T[K] '], S030[' dTdt [K/s] '], label = '0.3 concentration')
    plt.plot(Q040['T[K] '], S040[' dTdt [K/s] '], label = '0.4 concentration')
    plt.plot(S050['T[K] '], S050[' dTdt [K/s] '], label = '0.5 concentration')
    plt.plot(S060['T[K] '], S060[' dTdt [K/s] '], label = '0.6 concentration')
    plt.title('Slow cooling for full set')
    plt.legend()
    plt.xlabel('T[K]')
    plt.ylabel('dTdt [K/s]')
    plt.show()


def baseplots():
    plt.plot(GlycerolQuench['T'], GlycerolQuench['dTdt [K/s]'])
    plt.plot(WaterQuench['T'], WaterQuench['dTdt [K/s]'])
    plt.title("Quench cooling glycerol vs water")
    plt.xlabel('T')
    plt.ylabel('dTdt [K/s]')
    plt.show()

    plt.plot(GlycerolSlow['T [K]'], GlycerolSlow['dTdt [K/s]'])
    plt.plot(WaterSlow['T'], WaterSlow['dTdt [K/s]'])
    plt.xlabel('T')
    plt.ylabel('dTdt [K/s]')
    plt.title("Slow cooling glycerol vs water")
    plt.show()

##------CALORIMETRY------##
baseplots()
#only gly-water
fullSetQuench()
fullSetSlow()
GTplots()
glasstransition()

##----Dialectrics----##
#only Gly-water

#gly-water buffer

#gly-water + afp