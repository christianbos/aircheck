from ftplib import FTP

file = open('iArduino.txt', 'wb')  # ftp = FTP('189.216.247.89')
ftp = FTP('ftp.habilita.com.mx')  # ftp = FTP.connect('189.216.247.89')
ftp.login(user='habilita', passwd='8AB77tu6yi')
ftp.cwd("/public_html/")
ftp.retrbinary('RETR iArduino.txt', lambda s, w=file.write: w(s+"\n"))
file.close()
ftp.quit()
