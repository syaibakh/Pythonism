import qrcode

img = qrcode.make("https://example.com/")
img.save("qr.png", "PNG")