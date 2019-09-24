from PIL import Image
import os


def create_monochrome(input_file, output_file, scale=1):
    my_dir = os.path.dirname(os.path.realpath(__file__)) + '/'
    with open(my_dir + input_file, 'r') as f:
        data = f.read().replace('\n', ',').replace(' ', '').replace(',,', ',')
    seperated_lines = data.split(',')[:-1]

    number_system = input_file[-3:]
    height = len(seperated_lines)*scale
    length = len(seperated_lines[0])
    if number_system == 'hex':
        length*=4
    put_list = []

    for line in seperated_lines:
        row = []
        if number_system == 'hex':
            line = format(int(line, 16), f'0{length}b')

        for char in line:
            if char == '0':
                for i in range(scale):
                    row.append((0x00, 0x00, 0x00))
            elif char == '1':
                for i in range(scale):
                    row.append((0xff, 0xff, 0xff))

        for i in range(scale):
            for color in row:
                put_list.append(color)

    img = Image.new('RGB', (length*scale, height))
    img.putdata(put_list)
    img.save(my_dir + output_file)

def create_color(input_file, output_file, scale=1, type='rgb'):
    my_dir = os.path.dirname(os.path.realpath(__file__)) + '/'
    with open(my_dir + input_file, 'r') as f:
        data = f.read().replace('\n', ',').replace(' ', '').replace(',,', ',')
    seperated_lines = data.split(',')[:-1]

    height = len(seperated_lines)*scale
    length = len(seperated_lines[0])//6
    put_list = []

    for line in seperated_lines:
        row = []
        for index in range(length):
            chunk = line[index*6:index*6+6]

            for i in range(scale):
                if type == 'rgb':
                    row.append((int(chunk[0:2], 16), int(chunk[2:4], 16), int(chunk[4:6], 16)))
                elif type == 'bgr':
                    row.append((int(chunk[4:6], 16), int(chunk[2:4], 16), int(chunk[0:2], 16)))

        for i in range(scale):
            for color in row:
                put_list.append(color)

    img = Image.new('RGB', (length*scale, height))
    img.putdata(put_list)
    img.save(my_dir + output_file)


create_monochrome('monochrome_img.bin', 'image.png', 100)
create_color('flower-16x16.hex', 'image.png', 100, 'bgr')
