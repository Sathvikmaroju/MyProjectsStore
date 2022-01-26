import qrcode
import qrcode.image.svg

def get_svg(data,filename):
    factory = qrcode.image.svg.SvgPathImage
    svg_img=qrcode.make(data,image_factory=factory)
    svg_img.save(f"{filename}.svg")

def regularQR(data,filename):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=2)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black',back_color='white')
    img.save(f'{filename}.png')
    
fileName = input("Enter the file name: ")
Data = input("Enter the data: ")
choice = input("Enter '0' to get a regular qrcode(.png format) \n\t\tor\nEnter'1' to get the qrcode in svg format:\t")
valid_entries = ['0','1']
while choice not in valid_entries:
        print("\nInvalid!")
        print("Enter '0' to get a regular qrcode \n\t\tor\nEnter'1' to get the qrcode in svg format:\t")
        choice = input()

if choice=='0':
    regularQR(Data,fileName)
else:
    get_svg(Data,fileName)

print("The selected file is saved within the same directory as the program")