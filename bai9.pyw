import os,time
i = "true"
while i == "true" :
 x= input("Ban co muon tat may ko y/n :")
 if x == "y" :
     os.system('shutdown -s')
 elif x == "n":
     time.sleep(30)
     i = "true"
 else :
     i = "false"
print("Ket thuc")





