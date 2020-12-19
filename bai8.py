import smtplib
my_email = input('Nhập email của bạn: ')
receive_email = input('Nhập email nhận: ')
password = input(str('Mật khẩu: '))
message = input('Nội dung: ')
n = int(input('Số lần bạn muốn gửi: '))
for i in range(n):
 sever = smtplib.SMTP('smtp.gmail.com',587)
 sever.starttls()
 sever.login(my_email,password)
 print('Thành công')
 sever.sendmail(my_email,receive_email,message)
 print('Đã gửi đến:',receive_email)
