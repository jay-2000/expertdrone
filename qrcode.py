import qrcode

img = qrcode.make("https://github.com/jay-2000")

img.save("github.jpg")