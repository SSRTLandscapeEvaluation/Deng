# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 17:06:06 2018

@author: Ao
"""

def placemark_KML(jsonFilePath,kmlPath):
    f = open(jsonFilePath,'r')
    jsonDecides=json.load(f)
    coordi=[]
    for value in jsonDecides:
        converCoordiGCJ = cc.bd09togcj02(value['location']['lng'],value['location']['lat'])
        converCoordiGPS84=cc.gcj02towgs84(converCoordiGCJ[0],converCoordiGCJ[1])
        coordi.append((converCoordiGPS84[0],converCoordiGPS84[1],value['name']))
    f.close()
#    print(coordi)
    folderKML=KML.Folder(KML.Placemark(KML.name(coordi[0][2]),KML.Point(KML.coordinates(str(coordi[0][0]+','+str(coordi[0][1])+',0')))))        
    for i in range(1,len(coordi)):
        folderKML.append(KML.Placemark(KML.name(coordi[0][2]),KML.Point(KML.coordinates(str(coordi[0][0]+','+str(coordi[0][1])+',0')))))
    content=etree.tostring(etree.ElementTree(folderKML),encoding='unicode',pretty_print=True)
    Print(content)
    with codecs.open(kmlPath,'w','UTF-8') as kp:
        kp.write(content)