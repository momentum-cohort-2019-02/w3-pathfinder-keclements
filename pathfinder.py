from PIL import Image, ImageColor

im = Image.new('RGBA', (600, 600))
im.getpixel((0,0))
for x in range(600):
    for y in range(300):
        im.putpixel((x,y), (210,210,210))
# for x in range(100):
#     for y in range(600, 600):

        im.putpixel((x,y), ImageColor.getcolor('darkgray', 'RGBA'))
        im.save('putPixel.png')
#im.save('whiteImage.png')
