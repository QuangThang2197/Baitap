import smtplib

my_email = input("nhap email cua ban: ")
receive_email = input("nhap email nhan: ")
password = input(str("pass: "))
message = input("nhap noi dung: ")
n = int(input("so lan ban muon gui: "))
for i in range(n):
 sever = smtplib.SMTP('smtp.gmail.com',587)
 sever.starttls()
 sever.login(my_email,password)
 print("thanh cong")
 sever.sendmail(my_email,receive_email,message)
 print("da gui den:",receive_email)
