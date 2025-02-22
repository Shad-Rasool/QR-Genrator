import qrcode as qr
link=input("Enter link:    ")
qr=qr.make(link)
x=input("Enter Qr name:    ")
y=".jpg"
Qrname=x+y
qr.save(Qrname)
