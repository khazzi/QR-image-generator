import qrcode

def qr_generator(text):
    #creat an instance of the qrcode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    #add data to the qr code
    qr.add_data(text)
    qr.make(fit=True)

    #generate an image from the qrcode
    img = qr.make_image(fill_color="black", back_color="white")

    #save the image file
    filename = input("Enter the file name to save as, don't forget to add '.png' at the back:")
    img.save(filename)
    print(f"QR code saved as {filename}")

url = input("Enter the url:")
qr_generator(url)