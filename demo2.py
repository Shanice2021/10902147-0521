from PIL import Image
from PIL import ImageFilter

img1 = Image.open("chepai.jpg")
img2 = img1.filter(ImageFilter.SHARPEN) #銳利化
img2.save("chepai/out1.jpg")
img3 = img2.filter(ImageFilter.DETAIL) #細緻
img3.save("chepai/out2.jpg")
img4 = img3.filter(ImageFilter.SHARPEN) #銳利化
img4.save("chepai/out3.jpg")
img5 = img4.filter(ImageFilter.DETAIL) #細緻
img5.save("chepai/out4.jpg")
img6 = img5.filter(ImageFilter.SHARPEN) #銳利化
img6.save("chepai/out5.jpg")
img7 = img6.filter(ImageFilter.DETAIL) #細緻
img7.save("chepai/out6.jpg")
img8 = img7.filter(ImageFilter.SHARPEN) #銳利化
img8.save("chepai/out7.jpg")
img9 = img8.filter(ImageFilter.DETAIL) #細緻
img9.save("chepai/out8.jpg")
img10 = img9.filter(ImageFilter.SHARPEN) #銳利化
img10.save("chepai/out9.jpg")








