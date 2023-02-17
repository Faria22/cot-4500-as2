from functions import importData
from nevilles import nevilles
from newtonian import ddt, newtonian
from hermite import hermite
from csplines import csplines

prob1Data = importData('prob1.input')
prob1Result = nevilles(prob1Data[0], prob1Data[1], 3.7)
print(prob1Result, end='\n\n')

prob2Data = importData('prob2.input')
prob2Matrix = ddt(prob2Data[0], prob2Data[1])
for i in range(1, 4):
    print(prob2Matrix[i][i])
print()

prob3Result = newtonian(prob2Matrix, prob2Data[0], 7.3, 3)
print(prob3Result, end='\n\n')

prob4Data = importData('prob4.input')
prob4Result = hermite(prob4Data[0], prob4Data[1], prob4Data[2])
print()

prob5Data = importData('prob5.input')
prob5Result = csplines(prob5Data[0], prob5Data[1])
