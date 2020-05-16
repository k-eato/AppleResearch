import glob, os
from PIL import Image, ImageEnhance
os.chdir("C:/Users/kenea/Documents/PycharmProjects/Data_Creator/Data2/test_healthy")
count = 0
for file in glob.glob("*.jpg"):
    Im = Image.open(file.title())
    enhancer = ImageEnhance.Brightness(Im)
    for k in range(1,3):
        factor = 0.4 * k * k
        Im2 = enhancer.enhance(factor)
        name = "C:/Users/kenea/Documents/PycharmProjects/Data_Creator/Data2/test_healthy/A" + str(count) + ".jpg"
        Im2.save(name, quality=95)
        count = count + 1