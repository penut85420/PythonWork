from PIL import Image, ImageDraw

offset = 25
rw = 35
ffc = 100
ff = [(255, 255, 255, 255), (ffc, ffc, ffc, 255)]
bc = 0
b = (bc, bc, bc, 255)
w = 4
gap = 9
ww = offset * 2 + rw * 3 - 2
img = Image.new('RGBA', (ww, ww), (255, 255, 255, 255))
draw = ImageDraw.Draw(img)

fillmap = [
    [0, 1, 0],
    [1, 1, 1],
    [1, 1, 1],
]

vline = [
    [1, 0, 1],
    [0, 1, 0],
]

hline = [
    [1, 0],
    [0, 0],
    [0, 1],
]

def drawline(draw, xy, fill, width):
    for i in range(width):
        draw.line([xy[0]+i, xy[1], xy[2]+i, xy[3]], fill)

def drawblock(draw, xy, fill, width):
    pass

# drawline(draw, [5, 5, 9, 9], ff[1], 10)
draw.line([5, 5, 10, 10], ff[1], width=10)
draw.rectangle([20, 20, 25, 25], ff[1])

for i in range(3):
    for j in range(3):
        pass

img.save('tmp.png')

"""
[offset]
[w]
[offset][w][fill][w][fill][w][fill][w][offset]
[w]
[offset][w][fill][w][fill][w][fill][w][offset]
[w]
[offset][w][fill][w][fill][w][fill][w][offset]
[w]
[offset]
"""