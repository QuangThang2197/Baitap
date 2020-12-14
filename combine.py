import string,random
List = []
dict = {}
n=random.randint(50,100)
print('so phan tu trong list : ',n)
letters = string.ascii_letters
dict['name'] =''.join(random.choice(letters) for i in range(random.randint(1,10)))
dict["age"] = random.randint(0,100)
print(dict)
list=dict.items()
for i in range(0,n):
    print(list)
