from PIL import Image, ImageFilter

before = Image.open("http.png")
after = before.filter(ImageFilter.BLUR)
after.save("out.png")