# FINAL PROJECT
# Basic Python Course
# Rafika Sari (rafikasari2909@gmail.com)

# Buatlah sebuah program yang dapat mengirimkan email kepada beberapa penerima.
# Daftar penerima email dimasukkan ke dalam file receiver_list.txt
# Pastikan setiap email yang dikirim memiliki subjek
# Boleh menambahkan fitur lain dalam program tersebut (misal: gambar atau file)

# (1) Membuat Email Tanpa Lampiran & Tanpa file receiver_list.txt

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "rafika.sari@dsn.ubharajaya.ac.id"
toaddr = "rafikasari2909@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr 
msg['To'] = toaddr
msg["Subject"] = "Tes Kirim Email Via Python"

body = " Assalamu'alaikum, Apa kabar sis?"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "ikahopesjannah")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

# referensi: https://www.pythonindo.com/cara-mengirim-email-menggunakan-python/