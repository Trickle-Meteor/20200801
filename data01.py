import pandas as pd

a = pd.read_csv('mate.csv')

# name      a.iloc[:,0]
# A cm2     a.iloc[:,1]
#kg/m       a.iloc[:,2]
#I cm4      a.iloc[:,3]
#Z cm3      a.iloc[:,4]

#SS400  Fc = 156 N/mm2
#           N  =  156 N/mm2
#           Q  =  90 N/mm2
#           M  =  156 N/mm2

"""
N = 9.8kg
kN = 9.8t
MPa = N/mm2
"""
#lo = long mm
#N = 1/9.8 kg
lo = 1000
N = 10000
Fa = []
for j in range(10):
    Fa = []
    for i in range(len(a)):
        Fa.append(N/(int(a.iloc[i,1])*100))
    a[N] = pd.Series(Fa) 
    N += 2500

# a.to_csv("NA1t-3t.csv")
