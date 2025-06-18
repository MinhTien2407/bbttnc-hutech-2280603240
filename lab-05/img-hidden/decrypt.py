import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size

    binary_data = ''
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for color_channel in pixel[:3]:  # R, G, B
                binary_data += format(color_channel, '08b')[-1]

    # Tìm vị trí kết thúc: '1111111111111110'
    end_marker = '1111111111111110'
    end_index = binary_data.find(end_marker)

    if end_index != -1:
        binary_data = binary_data[:end_index]  # Cắt bỏ phần sau kết thúc

    # Tách chuỗi nhị phân thành từng byte (8 bit)
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ''.join([chr(int(byte, 2)) for byte in all_bytes])

    print("✅ Message decoded from image:")
    print(message)

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]
    decode_image(encoded_image_path)

if __name__ == "__main__":
    main()
