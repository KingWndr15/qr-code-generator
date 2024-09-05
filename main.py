import qrcode

data = "i am joshua"


qr = qrcode.QRCode(
    # The size of the QR Code
    version=8,
    #the error correction used for the QR Code
    # Controls how many pixels each “box” of the QR code is
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    # Controls how many boxes thick the border should be (the default is 4)
    border=4,
)

# Add data to the QR Code
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("qrcode.png")
