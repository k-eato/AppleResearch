from PIL import Image, ImageFilter
import random
import xml_maker as xml


Im2 = Image.open("belt.jpg")

for m in range(200,202):
    apples = random.randint(1,7)
    output = Im2.copy()
    arr = [[0]*4]*apples
    for i in range(apples):
        conflict = True
        ImageNum = random.randint(1, 6)
        file = "apple" + str(ImageNum) + ".jpg"
        Im = Image.open(file)
        newSize = random.randint(40, 125-10*apples)
        Im = Im.resize((newSize, newSize))
        rot = random.randint(0, 3) * 90
        Im = Im.rotate(rot, Image.NEAREST, expand = 1)
        while conflict:
            Xcoord = random.randint(0, 299)
            Ycoord = random.randint(0, 124)
            if i == 0:
                conflict = False
                break
            k = i - 1
            j = 0
            while j <= k:
                check1 = False
                if Xcoord <= arr[j][0] <= Xcoord + newSize:
                    check1 = True
                elif arr[j][0] <= Xcoord and Xcoord + newSize <= arr[j][1]:
                    check1 = True
                elif Xcoord <= arr[j][1] <= Xcoord + newSize:
                    check1 = True

                if check1:
                    if Ycoord <= arr[j][2] <= Ycoord + newSize:
                        conflict = True
                        break
                    elif arr[j][2] <= Ycoord and Ycoord + newSize <= arr[j][3]:
                        conflict = True
                        break
                    elif Ycoord <= arr[j][3] <= Ycoord + newSize:
                        conflict = True
                        break
                else:
                    conflict = False
                j = j + 1

        output.paste(Im, (Xcoord, Ycoord))
        arr[i] = [Xcoord, Xcoord + newSize, Ycoord, Ycoord + newSize]

    print(m)
    xml.makeXML(m,arr)
    outFile = "Data/" + str(m) + ".jpg"
    output = output.filter(ImageFilter.SMOOTH)
    output = output.filter(ImageFilter.SHARPEN)
    output.save(outFile, quality=95)
