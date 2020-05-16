import glob, os
from PIL import Image
os.chdir("C:/Users/kenea/Documents/PycharmProjects/Data_Creator/Data2/train_rotten")
count = 0
for file in glob.glob("*.jpg"):
    Im = Image.open(file.title())
    for k in range(1,4):
        Im2 = Im.rotate(90*k, Image.NEAREST, expand=1)
        name = "C:/Users/kenea/Documents/PycharmProjects/Data_Creator/Data2/train_rotten/" + str(count) + ".jpg"
        Im2.save(name, quality=95)
        count = count + 1