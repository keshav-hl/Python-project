import qrcode as qr
img = qr.make("https://github.com/keshav-hl")
img.save("keshav-github.jpg")