from PIL import Image

with open('input.txt') as f:
    transmission = f.read().strip()


width = 25
height = 6
layer_count = len(transmission) // (width * height)
layers = []

for i in range(layer_count):
    row = []
    start = i * width * height
    end = start + width * height
    layer = transmission[start:end]

    layers.append(layer)

image = [2 for x in range(width * height)]

for layer in layers:
    for i, c in enumerate(layer):
        if image[i] == 2:
            image[i] = int(c)


img = Image.new('1', [25, 6])
img.putdata(image)

img.save('message.png')
