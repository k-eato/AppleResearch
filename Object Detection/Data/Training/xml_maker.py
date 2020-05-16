import xml.etree.cElementTree as ET

def makeXML(count, array):
    annotation = ET.Element('annotation')
    folder = ET.SubElement(annotation, 'folder')
    folder.text = 'myapplepics'
    filename = ET.SubElement(annotation, 'filename')
    filename.text = str(count) + '.jpg'
    path = ET.SubElement(annotation, 'path')
    path.text = "/home/keato/labelImg/myapplepics/" + str(count) + '.jpg'
    source = ET.SubElement(annotation, 'source')
    database = ET.SubElement(source, 'database')
    database.text = "Unknown"
    size = ET.SubElement(annotation, 'size')
    width = ET.SubElement(size, 'width')
    width.text = "400"
    height = ET.SubElement(size, 'height')
    height.text = "225"
    depth = ET.SubElement(size, 'depth')
    depth.text = "3"
    segmented = ET.SubElement(annotation, 'segmented')
    segmented.text = '0'

    for element in array:
        object = ET.SubElement(annotation, 'object')
        name = ET.SubElement(object, 'name')
        name.text = 'Apple'
        pose = ET.SubElement(object, 'pose')
        pose.text = 'Unspecified'
        truncated = ET.SubElement(object, 'truncated')
        truncated.text = '0'
        difficult = ET.SubElement(object, 'difficult')
        difficult.text = '0'
        bndbox = ET.SubElement(object, 'bndbox')
        xmin = ET.SubElement(bndbox, 'xmin')
        xmin.text = str(element[0])
        ymin = ET.SubElement(bndbox, 'ymin')
        ymin.text = str(element[2])
        xmax = ET.SubElement(bndbox, 'xmax')
        xmax.text = str(element[1])
        ymax = ET.SubElement(bndbox, 'ymax')
        ymax.text = str(element[3])

    mydata = ET.ElementTree(annotation)
    file = "Data/" + str(count) + ".xml"
    mydata.write(file)