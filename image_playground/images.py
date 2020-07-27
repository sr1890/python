from PIL import Image, ImageFilter 

img = Image.open('./charmander.jpg')

# filtered_img = img.filter(ImageFilter.BLUR)

filtered_img = img.convert('L')

# print (img.format)

filtered_img.save("charmander_grey.png",'png')