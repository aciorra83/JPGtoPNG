from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')

# .thumbnail() method locks the aspect ratio of the image
img.thumbnail((400, 400))

img.save('thumbnail.jpg')
