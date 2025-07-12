import qrcode

def generate_qr_code(url, filename='biox_qr_code.png'):
    # Create QR Code object
    qr = qrcode.QRCode(
        version=1,  # controls size of the QR code (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    
    # Add data (URL) to the QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Generate image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save image
    img.save(filename)
    print(f"✅ QR Code saved as: {filename}")

# Example usage:
if __name__ == "__main__":
    user_url = input("Enter the URL to generate QR Code for: ")
    generate_qr_code(user_url)
