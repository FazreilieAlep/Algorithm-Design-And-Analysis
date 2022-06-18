import pandas as pd
import numpy
import array as arr


short_value =[8336.093073178992, 1956.409536989422,  4441.871589199802, 1393.8438162817981,  11945.13488495779]
countryList = ['JP','KR','MY','FR','MX']
aveWCGW=[0.09944245730683163, 0.10207193367167473, 0.09085258827543861, 0.08717207791864387, 0.09827785592611003]

"""for country in countryList:
    print(country)

print(len(short_value))"""


for i in range(len(countryList)):
    print((aveWCGW[i]/sum(aveWCGW))/(1-(short_value[i]/sum(short_value))))
