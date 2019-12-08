with open('input.txt') as f:
    image = f.read().strip()


width = 25
height = 6
layer_count = len(image) // (width * height)
layers = []

min_zero = 2 ** 32
index = -1

for i in range(layer_count):
    row = []
    start = i * width * height
    end = start + width * height
    layer = image[start:end]

    zeroes = layer.count('0')
    if zeroes < min_zero:
        min_zero = zeroes
        index = i

    layers.append(layer)

print(layers[index].count('1') * layers[index].count('2'))
