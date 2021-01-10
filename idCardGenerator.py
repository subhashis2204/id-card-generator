print('\n\t\t\t-----------welcome to the id card generator-----------\n')
print('you will find the Readme.txt file which contains the specifics of using the program code\n')
print('Please put all the employee images in the images folder.\n\nThe code will automatically generate a file named "resize_images" \nwhich will contain all the resized images and the final id card will be generated and stored in the "id" folder\n')
print('please make sure that there are atleast one image in the image folder otherwise the \ncode will not create any id\'s\n')

print('enter the details of the employees one by one\n')

from PIL import Image, ImageDraw, ImageFont
import random
import os
import qrcode


idlist = []


def randomid():
    rid = random.randint(1000000000, 9999999999)
    if rid in idlist:
        while rid not in idlist:
            rid = random.randint(1000000000, 9999999999)
    idlist.append(rid)
    return rid


def fontfinder(fname, size):
    return ImageFont.truetype(fname, size)


fname = 'resize_images'
textFontSize = 28
imagepath = os.path.join(os.getcwd(), 'images')
newImagePath = os.path.join(os.getcwd(), fname)
size_200 = (125, 150)

if not os.path.isdir(os.path.join(os.getcwd(), fname)):
    os.mkdir(fname)  # to store the resized images


for employee_image in os.listdir(imagepath):
    if employee_image.endswith(('.jpg', '.png', '.jpeg')):
        i = Image.open(os.path.join(imagepath, employee_image))
        fn, text = os.path.splitext(employee_image)
        i = i.resize(size_200)
        i.save(os.path.join(newImagePath, '{}_150{}'.format(fn, text)))

for employee_image in os.listdir(fname):
    if employee_image.endswith(('.jpg', '.png', '.jpeg')):
        image = Image.new('RGB', size=(600, 400), color=(200, 200, 200))
        draw = ImageDraw.Draw(image)

        draw.text((200, 0), 'ID Card', (0, 0, 0),
                  font=fontfinder('times.ttf', 50))

        id = randomid()
        draw.text((20, 100), 'ID: {}'.format(id), (0, 0, 0),
                  font=fontfinder('arial.ttf', textFontSize))

        name = input('enter the name: ').upper()
        draw.text((20, 140), 'Name: {}'.format(name),
                  (0, 0, 0), font=fontfinder('arial.ttf', textFontSize))

        dob = input('enter the date of birth in the format dd-mm-yyyy: ')
        draw.text((20, 180), 'D.O.B: {}'.format(dob),
                  (0, 0, 0), font=fontfinder('arial.ttf', textFontSize))

        bgroup = input('enter the blood group: ')
        draw.text((20, 220), 'Blood gp.: {}'.format(bgroup),
                  (0, 0, 0), font=fontfinder('arial.ttf', textFontSize))

        mno = input('enter the mobile number: ')
        draw.text((20, 260), 'M.no: {}'.format(mno),
                  (0, 0, 0), font=fontfinder('arial.ttf', textFontSize))

        add = input('enter the address: ')
        draw.text((20, 300), 'Address: {}'.format(add),
                  (0, 0, 0), font=fontfinder('arial.ttf', textFontSize))

        dir = os.getcwd()
        path = os.path.join(dir, 'ids', str(id) + '.png')

        string = {'ID': id, 'name': name, 'dob': dob,
                  'blood gr.': bgroup, 'm.no': mno, 'address': add}
        qr = qrcode.QRCode(box_size=2)
        qr.add_data(string)
        qr.make(fit=True)
        img = qr.make_image()

        image.paste(img, (415, 250))
        f = Image.open(os.path.join(newImagePath, employee_image))
        image.paste(f, (400, 70))
        image.save(path)
