import pyqrcode
import png


address = input("Please enter the url you want the QR code to be generated for: ")
file_name = input("Please enter the file name under which you want the QR code to be saved: ")
url = pyqrcode.create(address)

url.png(f"{file_name}.png", scale=8)