import os
a=input("ten thu muc: ")
b=input("ten file: ")
c=input("noi ban muon tai ve: ")
os.chdir(c)
os.mkdir(a)
d= c+a
os.chdir(d)
f= open(b,"w")
f.writelines("Welcome")
f.close()



