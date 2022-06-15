
import qrcode as qr
from PIL import Image
qr = qr.QRCode(version=1,
error_correction=qr.ERROR_CORRECT_H,box_size=18, border=4) 
qr.add_data("https://youtu.be/Jey1GH8CERI")
qr.make(fit=TRUE)
img=qr.make_image(fillcolor="red",bgcolor ="blue" )
img.save("wscube_web.png")