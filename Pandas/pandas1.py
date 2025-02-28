import pandas as pd
import numpy as np

dFrameEmt = pd.DataFrame()
print(dFrameEmt)
print(dFrameEmt.empty)

array1 = np.array([10, 20, 30])
array2 = np.array([100,200,300])
array3 = np.array([-10,-20,-30, -40])

#dFrame4 = pd.DataFrame(array1)
#print(dFrame4)
#print(dFrame4.empty)

#dFrame5 = pd.DataFrame([array1, array3, array2], columns=[ 'A', 'B', 'C', 'D'])
#print(dFrame5)
#print(dFrame5.empty)

#listDict = [{'a':10, 'b':20}, {'a':5, 'b':10, 'c':20}]
#dFrame6 = pd.DataFrame(listDict)
#print(dFrame6)
#print(dFrame6.empty)

#dictForest = {'State': ['Assam', 'Delhi', 'Kerala'], 'GArea': [78438, 1483, 38852] , 'VDF' : [2797, 6.72,1663]}
#dFrame7 = pd.DataFrame(dictForest)
#dFrame7 = pd.DataFrame(dictForest, columns=['VDF', 'GArea', 'State'])
#print(dFrame7)
#print(dFrame7.empty)

#seriesA = pd.Series([1,2,3,4,5], index = ['a', 'b', 'c', 'd', 'e'])
#seriesB = pd.Series ([1000,2000,-1000,-5000,1000], index = ['a', 'b', 'c', 'd', 'e'])
#seriesC = pd.Series([10,20,-10,-50,100], index = ['z', 'y', 'a', 'c', 'e'])
#dFrame8 = pd.DataFrame([seriesA, seriesB, seriesC])
#dFrame9 = dFrame8.fillna(0)
#print(dFrame9)
#print(dFrame9.empty)

ResultSheet={
'Arnab': pd.Series([90, 91, 97],index=['Maths','Science','Hindi']),
    'Ramit': pd.Series([92, 81, 96],index=['Maths','Science','Hindi']),
    'Samridhi': pd.Series([89, 91, 88],index=['Maths','Science','Hindi']),
    'Riya': pd.Series([81, 71, 67],index=['Maths','Science','Hindi']),
    'Mallika': pd.Series([94, 95, 99],index=['Maths','Science','Hindi'])}
#print(ResultSheet)
ResultDF = pd.DataFrame(ResultSheet)
ResultDF['Wicho']=[90,90,91]
ResultDF['Elias']=[100,100,100]
ResultDF['Riya']=[90,90,91]
#ResultDF[:]=100

#ResultDF.loc['SI']=[70,70,70,70,70,70,70]
ResultDF.loc['SI']=95
ResultDF.loc['edith']=100

ResultDF = ResultDF.drop('SI', axis=0)
ResultDF = ResultDF.drop('Science', axis=0)
ResultDF = ResultDF.drop('Elias', axis=1)

print(ResultDF)

print(ResultDF.index)
print(ResultDF.index.tolist())

print(type(ResultDF.columns))
print(ResultDF.columns.tolist())

print(ResultDF.dtypes)
print(ResultDF.values)
print(type(ResultDF.values))

L = ResultDF.values.tolist()
print(len(L))
print(L)
print(L[1])

for i in L:
    print(i)

print(ResultDF.shape)
print(ResultDF.size)

#ResultDF.to_csv('DataFrame.csv', sep=',', header=False, index=False)
ResultDFNuevo = pd.read_csv('DataFrame.csv')
print(ResultDFNuevo)

exit()

seriesTenTwenty=pd.Series(np.arange( 10, 20, 1 ))
seriesTenTwenty2=pd.Series(np.arange( 10, 25, 1 ))
#print(seriesTenTwenty)
#print(seriesTenTwenty.count())
#print(seriesTenTwenty.head(3))
#print(seriesTenTwenty.tail(2))

#print(seriesTenTwenty2)
#print(seriesTenTwenty2 + seriesTenTwenty)

print(seriesTenTwenty.add(seriesTenTwenty2, fill_value=0))

exit()

#Serie = pd.Series([10,20,30])
#Serie = pd.Series(["Marco","Fide","Said", "Machucho"], index=[2,1,3,0])
Serie = pd.Series([50,90,70,100], index=["Marco","Fide","Said", "Machucho"])
#Serie = pd.Series([["Marco", "ITI"],"Fide","Said", "Machucho"])
#Serie = pd.Series([True,False,True])
#Serie = pd.Series([True,"False",10])

#print(type(Serie))
#print(Serie)

for i in range (4):
    #print(Serie[i])
    print(Serie.iloc[i])

#print("Valor de Marco: ", Serie["Marco"])

array = np.array([1,2,3,4])
Serie3 = pd.Series(array)
#print(Serie3)

dict1 = {'India': 'NewDelhi', 'UK': 'London', 'Japan': 'Tokyo', 'Mexico': 'Victoria'}
Serie4 = pd.Series(dict1)
#print(Serie4)
#print("valor: ..", Serie4["Mexico"])
#print(Serie4.iloc[[0,1]])
#print(Serie4[['Mexico','Mexico','Mexico']])

#print(Serie4['UK':'Mexico'])
#print(Serie4[::-1])

seriesAlph = pd.Series(np.arange(10,16,1),
index = ['a', 'b', 'c', 'd', 'e', 'f'])

seriesAlph.name = "Calificaciones"
seriesAlph.index.name = "Letras"
print(seriesAlph)
print(seriesAlph.values)
print(type(seriesAlph.values))
print(seriesAlph.size)
print(seriesAlph.empty)

#print(seriesAlph['c':'f'])


exit()