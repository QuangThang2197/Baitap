import os
import codecs
import requests

# ham tao thu muc
def tao_thu_muc(name):
    os.mkdir(name)
    os.chdir(name)

# Hàm Lưu file
# Truyền vào url cần lưu và Số thứ tự để đặt tên file cần lưu
def luu_file(url, stt):
    file = codecs.open('file' + str(stt) + '.html', 'w', encoding = 'utf-8')
    file.write(requests.get(url).text)
    file.close()


# Hàm lưu tất cả các url đã tim được
def luu_tat_ca_file(history, so_luong_trang):
    stt = 0
    for url_con in history:
        if stt >= so_luong_trang:
            break
        luu_file(url_con, stt)
        print(f'{stt} {url_con}')
        stt += 1
