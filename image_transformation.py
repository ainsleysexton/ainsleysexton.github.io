from PIL import Image

my_image = Image.open("obama.jpg")
image_pixels = my_image.load()

width, height = my_image.size

for i in range(0, width):
    for j in range(0, height):
        blue_component = image_pixels[i,j][0]
        green_component = image_pixels[i,j][1]
        red_component = image_pixels[i,j][2]
        gray_value = (int)(0.07 * blue_component + 0.72 * green_component + 0.21 * red_component)
        image_pixels[i,j] = (gray_value, gray_value, gray_value, 255)
        # navy blue
        if(gray_value <= 51):
            new_color = (0,31,59,255)
        # red
        elif(gray_value <= 102):
            new_color = (147,53,214,255)
        # light blue
        elif(gray_value <= 153):
            new_color = (136,107,160,255)
        # kinda green -> teal
        elif(gray_value <= 190):
            new_color = (158,210,216,255)
        elif(gray_value <= 220):
            new_color = (203,219,213,255)
        # light yellow
        elif(gray_value <= 255):
            new_color = (218,232,227,255)
        image_pixels[i,j] = (new_color[0],new_color[1],new_color[2],255)
my_image.show()
