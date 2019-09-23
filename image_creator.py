from PIL import Image
import os


def create_monochrome(input_file, output_file, scale=1):
    bit_string = ''
    my_dir = os.path.dirname(os.path.realpath(__file__)) + '/'
    with open(my_dir + input_file, 'r') as f:
        height = 0
        for line in f:
            row = ''
            for char in line:
                if ((char == '0') or (char == '1')):
                    row+=char*scale
            bit_string+=row*scale
            height+=1*scale
    img = Image.new('RGB', (len(bit_string)//height, height))
    put_list = []
    for bit in bit_string:
        if bit == '1':
            put_list.append((0xff, 0xff, 0xff))
        else:
            put_list.append((0x00, 0x00, 0x00))
    img.putdata(put_list)
    img.save(my_dir + output_file)


def create_color(input_file, output_file, scale=1, type='rgb'):
    color_list = []
    my_dir = os.path.dirname(os.path.realpath(__file__)) + '/'
    with open(my_dir + input_file, 'r') as f:
        height = 0
        for line in f:
            clean = line.replace(' ', '')
            clean = clean.replace(',', '')
            print(clean)
            row = []
            for index in range(len(clean)//6):
                chunk = clean[index*6:index*6+6]
                for i in range(scale):
                    if type == 'rgb':
                        row.append((int(chunk[0:2], 16), int(chunk[2:4], 16), int(chunk[4:6], 16)))
                    elif type == 'bgr':
                        row.append((int(chunk[4:6], 16), int(chunk[2:4], 16), int(chunk[0:2], 16)))

            for i in range(scale):
                for color in row:
                    color_list.append(color)
            height+=1*scale
    img = Image.new('RGB', (len(color_list)//height, height))
    img.putdata(color_list)
    img.save(my_dir + output_file)


# create_monochrome('monochrome_img.bin', 'image.png', 100)
create_color('mario-16x16.hex', 'image.png', 100, 'bgr')
