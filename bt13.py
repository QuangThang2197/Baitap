import os.path

path = 'C:\\Users\\DELL'
x = os.listdir(path)
print("cac thu muc trong o dia C: ")
print(x)

list1 = next(os.walk(path))[1]
print("cac thu muc: ")
print(list1)

list2 = next(os.walk(path))[2]
print("cac tap tin: ")
print(list2)
