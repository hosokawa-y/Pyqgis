import glob

s = "/Users/hosokawa/Map data/gyouseikuiki/kanto/N03-20210101_14_GML_kanagawa/vector/"
files = glob.glob(s + "*.shp")
for file in files:
    print(file)
    file_name = file.replace(s, "")
    print(file_name)
    iface.addVectorLayer(file, "", 'ogr')

print("done")