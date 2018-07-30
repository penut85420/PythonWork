import os
import re
import sys
import xml.dom.minidom as MINIDOM
import xml.etree.cElementTree as ET

dir_in = "zhwiki_sub_seg_fix_small_sub\\"
dir_out = "zhwiki_simple\\"
fid = 1
for dirPath, dirNames, fileNames in os.walk(dir_in):
    for file_path in fileNames:
        print("Parsing %s%s" % (dir_in, file_path))
        tree = ET.ElementTree(file=dir_in + file_path)
        new_root = ET.Element("pageset")

        root = tree.getroot()
        for c in root.iter(tag='page'):
            new_page = ET.SubElement(new_root, "page")
            new_preserve = ET.SubElement(new_page, "preserve")
            # new_before = ET.SubElement(new_preserve, "before")
            # new_after = ET.SubElement(new_preserve, "after_")
            
            title = c[0].text
            content = c[1].text
            content = content.replace("\n", " ")
            content = content.replace("  ", " ")
            content = content.strip()
            # print("Befor[%s]" %(content))
            # new_before.text = content
            content = content.replace("、", "和")
            seg = content.strip().split(" ")
            isTitle = False
            isIs = False
            isOf = False
            for i in range(len(seg)):
                if seg[i] == title:
                    isTitle = True
                elif seg[i] == "是":
                    isIs = True
                elif seg[i] == "的":
                    isOf = True
                elif seg[i] == "，":
                    if not isIs or not isOf:
                        seg[i] = ""
                    else: 
                        seg[i] = "。"
                        seg = seg[:i+1]
                        break
                
            content = ""
            seg = list(filter(None, seg))
            for s in seg:
                content += s + " "
            content = content.strip()
            # print("After[%s]" % (content))
            # new_after.text = content
            new_preserve.text = content
        new_tree = ET.ElementTree(new_root)
        new_tree.write("%szhwikiSimple%.4d.xml"%(dir_out, fid), encoding='UTF-8')
        d = MINIDOM.parse("%szhwikiSimple%.4d.xml"%(dir_out, fid))
        with open("%szhwikiSimple%.4d.xml" % (dir_out, fid), "wb") as fout:
            fout.write(d.toprettyxml(encoding='UTF-8'))
        fid += 1
