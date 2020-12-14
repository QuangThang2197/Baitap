import os
list1=list()
list2=list()
for (root,dirs,files) in os.walk('C:'):  # os.walk de truy cap o dia minh chon
    print("thu muc o dia C:",root)  # root la thu muc can chon
    print("thu muc con",dirs)  # dirs la cac thu muc con
    print("tap tin ",files)  # files la cac tap tin
for (root,dirs,files) in os.walk('C:'):
    for i in files:
        list1.append(i)
    for x in dirs:
        list2.append(x)
print("list tap tin ",list1)
print("list thu muc con ",list2)