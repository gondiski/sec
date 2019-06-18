import PIL
import qrcode

def secured(number):
	queried = int(number)
	qr = qrcode.QRCode(
	    version=1,
	    error_correction=qrcode.constants.ERROR_CORRECT_L,
	    box_size=10,
	    border=4,
	)
	qr.add_data(queried)
	qr.make(fit=True)
	img = qr.make_image(fill_color="white",back_color="black")
	pic = img.save(number+'_tree.jpg')
	return pic
	
# number = "0723347380"
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data(number)
# qr.make(fit=True)

# img = qr.make_image(fill_color="white",back_color="black")
# img.save('tree.jpg')