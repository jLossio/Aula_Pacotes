import qrcode 
#criar um código
qr = qrcode.QRCode(version=1, box_size=10, border =5)
#adicionar daddos ao código QR
data = "https://pypi.org/project/pandas/"
qr.add_data(data)
qr.make(fit=True)

#criar imagem do código QR
img =  qr.make_image(fill_color="black", back_color="white")
#salvar imagem em um arquivo
img.save("qr_code.png")