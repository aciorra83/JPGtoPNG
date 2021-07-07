from PIL import Image, ImageFilter


img = Image.open('/home/alex/Desktop/ZTM/image_playground/pokadex/pikachu.jpg')

filtered_img = img.convert('L')  # converts to greyscale

# cropping:
box = (100, 100, 400, 400)
region = filtered_img.crop(box)

# resize = filtered_img.resize((300, 300))

region.save('grey.png', 'png')

# opens up the file in a new window
