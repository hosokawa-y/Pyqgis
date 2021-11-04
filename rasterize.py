from qgis import processing
import os

files = QgsProject.instance().mapLayers()
resolution = 0.000150
r = str(resolution)
dir_path = "/Users/hosokawa/Map data/geotiff/" + "kanagawa" + "/" + r[2:]
os.mkdir(dir_path)


for index, layer in QgsProject.instance().mapLayers().items():
    if layer.type() != QgsMapLayer.VectorLayer:
        continue

    file_name = layer.name()
    code = file_name[-5:]
    output = f"{dir_path}/{code}.tif"
    # output = f"/Users/hosokawa/Map data/gyouseikuiki/kanto/keiryou_test/{code}-00001.tif" 

    parameters = {
        'INPUT': file_name,
        'BURN': 0.000000,
        'UNITS': 1,
        'WIDTH': resolution,
        'HEIGHT': resolution,
        'EXTENT': file_name,
        'NODATA': "-9999",
        'OUTPUT': output
    }

    result = processing.run("gdal:rasterize", parameters)
    iface.addRasterLayer(output,"")

print("done")
