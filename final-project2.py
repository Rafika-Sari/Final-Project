# FINAL PROJECT
# Basic Python Course
# Rafika Sari (rafikasari2909@gmail.com)

# Buatlah sebuah program yang dapat mengirimkan email kepada beberapa penerima.
# Daftar penerima email dimasukkan ke dalam file receiver_list.txt
# Pastikan setiap email yang dikirim memiliki subjek
# Boleh menambahkan fitur lain dalam program tersebut (misal: gambar atau file)

# (2) Membuat Email dengan Lampiran (tanpa file receiver_list.txt)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "rafika.sari@dsn.ubharajaya.ac.id"
toaddr = "rafikasari2909@gmail.com"

msg = MIMEMultipart()

msg['From'] = fromaddr 
msg['To'] = toaddr
msg["Subject"] = "Tes Kirim Email Via Python dengan Lampiran"

body = " Assalamu'alaikum, Apa kabar sis? Mohon Maaf Lahir Batin - Selamat Menunaikan Ibadah Ramadhan"

msg.attach(MIMEText(body, 'plain'))

# Lampiran, sesuaikan nama filename dengan nama di attachment
filename = "SS_HasilKirimEmail.docx"
attachment = open("C:\\Users\\user\\My Documents\\AI Mentorship 2021\\Basic Python\\SS_HasilKirimEmail.docx", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "ikahopesjannah")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

# referensi: https://www.pythonindo.com/cara-mengirim-email-menggunakan-python/
