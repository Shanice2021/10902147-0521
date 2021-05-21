from PIL import Image
from PIL import ImageFilter

img1 = Image.open("orange.jpg")
img2 = img1.filter(ImageFilter.BLUR) #模糊
img2.save("orange/out1.jpg")
img3 = img1.filter(ImageFilter.CONTOUR) #輪廓
img3.save("orange/out2.jpg")
img4 = img1.filter(ImageFilter.DETAIL) #細緻
img4.save("orange/out3.jpg")
img5 = img1.filter(ImageFilter.EDGE_ENHANCE) #邊緣增強
img5.save("orange/out4.jpg")
img6 = img1.filter(ImageFilter.EDGE_ENHANCE_MORE) #邊緣增強+
img6.save("orange/out5.jpg")
img7 = img1.filter(ImageFilter.EMBOSS) #浮雕
img7.save("orange/out6.jpg")
img8 = img1.filter(ImageFilter.FIND_EDGES) #找出邊緣(線也算邊緣)
img8.save("orange/out7.jpg")
img9 = img1.filter(ImageFilter.SMOOTH) #圓滑
img9.save("orange/out8.jpg")
img10 = img1.filter(ImageFilter.SHARPEN) #銳利化
img10.save("orange/out9.jpg")








