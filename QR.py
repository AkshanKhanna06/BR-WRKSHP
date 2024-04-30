import qrcode

def generate_qr_code(text, filename):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to QR code
    qr.add_data(text)
    qr.make(fit=True)

    # Generate QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save QR code image as PNG
    img.save(filename)
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    # Input the text you want to encode into the QR code
    text = input("NO ZONE AREA: ")

    # Specify the filename to save the QR code image
    filename = "output_qr_code.png"

    generate_qr_code(text, filename)
