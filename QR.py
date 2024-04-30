import qrcode

def QR(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    # Example data for QR code
    data = "Akshan Khanna"

    # Generate QR code image
    generate_qr_code(data, "qrcode.png")
