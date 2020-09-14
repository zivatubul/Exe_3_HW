from PIL import Image, ImageDraw
#exe3_1 and exe3_2
try:
   a=1/0
except ZeroDivisionError:
    print("You can't divide by zero")



print("continue")

#exe3_3
# code legal

try :
    x = 1
finally :
    print("finally")

#exe3_4
# we can caught all type of exceptions

#exe3_5
# We will catch all kinds of exception this can bring many possible problems. For example, the behavior inside the exception
#will not correspond to the actual exception.

#exe3_6

#except IOError - input \output error
#except ZeroDivisionError - error for divid by zero

#exe3_7_8_9


file = open("words.txt", "w+")
file.write("ziva\n")
file.seek(0)
print(file.read())
file.close()

file = open ("words.txt" ,"a+", encoding='utf-8')
file.write("\nזיוה")
file.seek(0)
print(file.read())




img = Image.new('RGBA', (100, 100), (255, 0, 0, 0))

draw = ImageDraw.Draw(img)
draw.ellipse((25, 25, 75, 75), fill=(255, 0, 0))

img.save('test.png', 'PNG')

