import random
List = []
List2 = []
n=random.randint(50,1000)
List.append(n)
print('gia tri cua list: ',List)
x = random.sample(range(-1000,1000),n)
print ('List n so nguyen random la : ',(x))
for i in range(0,n):
    x = round(random.uniform(-1000.0, 1000.0), 1)
    List2.append(x)
print('list n so thuc random la: ',List2)
