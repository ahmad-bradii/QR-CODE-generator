
import os
"""
This script generates a QR code for a specified website link and saves it as an image file in a designated folder.
Modules:
    qrcode: A module to generate QR codes.
    os: A module to interact with the operating system.
Functions:
    os.getcwd(): Returns the current working directory.
    os.makedirs(name, mode=0o777, exist_ok=False): Creates a directory named 'name' with specified mode. If the directory already exists, it does nothing if 'exist_ok' is True.
Variables:
    website_link (str): The URL to be encoded in the QR code.
    qr (qrcode.QRCode): An instance of the QRCode class with specified version, box size, and border.
    img (PIL.Image.Image): The generated QR code image.
    current_directory (str): The current working directory.
    folder_path (str): The path to the folder where the QR code image will be saved.
"""
import qrcode

website_link = input('put yout url here : ')

qr = qrcode.QRCode(version=7, box_size=5, border=2)
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color='black', back_color='white')

# Specify the folder path
current_directory = os.getcwd()


folder_path = f"{current_directory}\\QR CODE generator\\QR CODES"
os.makedirs(folder_path, exist_ok=True)



# Extract the name from the website link
name = website_link.split('//')[-1].split('/')[0].replace('.', '_')
file_name = f"{name}.png"
# Save the image in the specified folder
img.save(os.path.join(folder_path, file_name))