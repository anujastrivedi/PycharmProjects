from PIL import Image

one = Image.open("1.jpg")
zero = Image.open("0.jpg")

r1, g1, b1 = one.split()
r2, g2, b2 = zero.split()


one_merge = Image.merge("RGB", (r2, g1, b1))

one_merge.show()



