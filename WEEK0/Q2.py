from PIL import Image

lena = Image.open("lena.png")
lena_modified = Image.open("lena_modified.png")

w,h = lena.size
for j in range(h):
    for i in range(w):
        if lena.getpixel((i,j)) == lena_modified.getpixel((i,j)):
            print(lena.getpixel((i,j)))
            lena_modified.putpixel((i,j),(255,2,120,0))
            print(lena_modified.getpixel((i,j)))

lena_modified.show()
lena_modified.save("ans_two2.png")