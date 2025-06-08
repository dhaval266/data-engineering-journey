import qrcode

data = input("Enter the data to encode in the QR code: ").strip()
filename = input("Enter the filename to save the QR code (e.g., qr_code.png): ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)

print(f"QR code generated and saved as {filename}.")