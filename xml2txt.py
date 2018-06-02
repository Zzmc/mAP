from xml.etree import ElementTree as ET
import os

xml_path = "/home/zmc/Documents/mAP/Annotations/"
xml_files = os.listdir(xml_path)
for file_ in xml_files:
    temp = []
    per = ET.parse(xml_path+file_)
    p = per.findall("./object")
    for object in p:
        for child in object.getchildren():
            temp_info = []
            if child.tag == "name":
                res_name = child.text
                temp_info.append(res_name)
            elif child.tag == "bndbox":
                for cchild in child.getchildren():
                    if cchild.tag == "xmin":
                        xmin = " "+cchild.text
                        temp_info.append(xmin)
                    elif cchild.tag == "ymin":
                        ymin = " "+cchild.text
                        temp_info.append(ymin)
                    elif cchild.tag == "xmax":
                        xmax = " "+cchild.text
                        temp_info.append(xmax)
                    elif cchild.tag == "ymax":
                        ymax = " "+cchild.text+"\n"
                        temp_info.append(ymax)
            temp.append(temp_info)
    txt_file_name = file_.split(".")[0]+".txt"
    ground_truth = open("./ground-truth/"+txt_file_name, "wr")
    for box_info in temp:
        for info in box_info:
            ground_truth.write(info)
    ground_truth.close()
    print("Saving ... ...")
print("Done ... ...")
