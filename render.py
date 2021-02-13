from PIL import Image

def art(path, symbol='rgb', output='art.txt'):
    image = Image.open(path)
    image.thumbnail((80, 80), Image.ANTIALIAS)

    result = ''

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            color = image.getpixel((y, x))
            if min(color) > 150:
                result += ' '
            else:
                result += symbol[color.index(max(color))%len(symbol)]
        result += '\n'

    with open(output, 'w') as f:
        f.write(result)

    print('art created!')