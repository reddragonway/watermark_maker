# Скрипт добавляет водяные знаки на видеозаписи 

# импортируем библиотеки
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

# открываем файл с данными клиента, считываем данные
sfile = open("client.txt", encoding="UTF-8")
data = sfile.read()
sdata = data.split(":")
sname = sdata[0]    # имя
sphone = sdata[1]   # телефон
sdog = sdata[2]     # номер договора
shttp = sdata[3]    # адрес сайта организации
sfile.close

# рисуем водный знак для видео
myimg = Image.new("RGB", (1280, 1024), (255, 255, 255))
font = ImageFont.truetype("arial.ttf", 60)
draw = ImageDraw.Draw(myimg)
draw.text((10, 25), sname, font=font, fill=(0, 0, 0))
draw.text((10, 900), sphone, font=font, fill=(0, 0, 0))
draw.text((750, 900), sdog, font=font, fill=(0, 0, 0))
draw.text((1050, 25), shttp, font=font, fill=(0, 0, 0))

# сохраняем водный знак
myimg.save("watermark.gif", "GIF", transparency=0)

# для каждого видеофайла (в текущей папке) с форматом mp4 добавляем водный знак, после чего удаляем исходный файл
# для корректной работы необходимо установить ffmpeg в систему и прописать его в PATH
vfiles = os.listdir()
for el in vfiles:
    if el[-4:] == ".mp4":
        os.system(f'ffmpeg -i {el} -i watermark.gif -filter_complex "overlay=x=(main_w-overlay_w)/2:y=(main_h-overlay_h)/2"  {el[:-4]}_new.mp4')
        filename = f'{el[:-4]}_new.mp4'
        os.system(f'del {el}')