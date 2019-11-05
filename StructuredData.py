import numpy as np

name = ['Alice','Bob','Cathy','Doug']
age = [25,45,37,19]
weight = [55, 85.5, 68, 61.5]
# x = np.zeros(4, dtype=int)
data = np.zeros(4, dtype={'names':('name','age','weight'),'formats':('U10','i4','f8')})
#data

Out: array([('', 0, 0.), ('', 0, 0.), ('', 0, 0.), ('', 0, 0.)],
      dtype=[('name', '<U10'), ('age', '<i4'), ('weight', '<f8')])


data['name']=name
data['age']=age
data['weight']=weight
print(data)

Out: [('Alice', 25, 55. ) ('Bob', 45, 85.5) ('Cathy', 37, 68. )
 ('Doug', 19, 61.5)]
