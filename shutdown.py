import os,time
i = "yes"
while i == "yes" :
 x= input("ban co muon tat may ko: ")
 if x == "y":
     os.system('shutdown -s')
 elif x == "n":
     time.sleep(1)
     i = "yes"
 else :
     i = "no"
print('ket thuc')
