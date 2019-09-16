from PIL import Image

page_path = # path to the pages
image_list = []
image_one = Image.open(page_path + str(1) + '.png') 

for i in range(2, 791):
    image = Image.open(page_path + str(i) + '.png')
    image.load()
    image_list.append(image)

image_one.load()
image_one.save('xxxxx.pdf', 'PDF', resolution=100.0, save_all=True, append_images=image_list) # output file