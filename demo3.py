from PIL import Image, ImageDraw

newImg = Image.new("RGBA", (300, 300), "#aaaaaa") #(透明度?, 大小, 顏色)
drawObj = ImageDraw.Draw(newImg)
for x in range(100, 200, 3):
    for y in range(100, 200, 3):
        drawObj.point([(x,y)], fill = "red")

drawObj.line([(30, 30), (270, 30), (270, 270), (30, 270), (30, 30)], fill="#00ff00")
drawObj.line([(20, 20), (280, 20), (280, 280), (20, 280), (20, 20)], fill="#ff0000")
drawObj.line([(10, 10), (290, 10), (290, 290), (10, 290), (10, 10)], fill="#0000ff")

for i in range(10, 300, 10):
    drawObj.line([(i, 0), (300,i-150)], fill="#ff00ff")
    drawObj.line([(i-150, 300), (0, i)], fill="#ff00ff")
    drawObj.line([(150-i, 0), (0, i)], fill="#ff00ff")    
    drawObj.line([(i+150,300), (300,300-i)], fill="#ff00ff")   


newImg.save("test.png")