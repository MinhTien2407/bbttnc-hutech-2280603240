from PIL import Image

def decode_image(image_path):
    img = Image.open(image_path)
    width, height = img.size

    binary_message = ''
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for color_channel in range(3):
                binary_message += format(pixel[color_channel], '08b')[-1]

    binary_values = [binary_message[i: i+8] for i in range(0, len(binary_message), 8)]

    message = ''
    for binary_value in binary_values:
        if binary_value == '11111111':
            break
        message += chr(int(binary_value, 2))

    return message
