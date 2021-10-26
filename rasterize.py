from qgis import processing

files = QgsProject.instance().mapLayers()

for index, layer in QgsProject.instance().mapLayers().items():
    if layer.type() != QgsMapLayer.VectorLayer:
        continue

    file_name = layer.name()

    parameters = {
        'INPUT': file_name,
        'BURN': 0.000000,
        'UNITS': 1,
        'WIDTH': 0.000050,
        'HEIGHT': 0.000050,
        'EXTENT': file_name,
        'NODATA': "-9999",
        'OUTPUT': "/Users/hosokawa/vector_to_raster/" + file_name + ".tiff"
    }

    result = processing.run("gdal:rasterize", parameters)
