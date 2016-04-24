from ftplib import FTP

file = open('arduino.txt', 'wb')  # ftp = FTP('189.216.247.89')
ftp = FTP('192.168.5.161')  # ftp = FTP.connect('189.216.247.89')
ftp.login(user='arduino', passwd='12345678')
ftp.cwd("arduino/")
ftp.retrbinary('RETR cmd.txt', lambda s, w=file.write: w(s+"\n"))
file.close()
ftp.quit()
print("Termino la descarga")
