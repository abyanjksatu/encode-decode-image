import base64
with open("my_image.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
print(my_string)

imgdata = base64.b64decode(my_string)
filename = 'new_image.jpg'
with open(filename, 'wb') as f:
    f.write(imgdata)