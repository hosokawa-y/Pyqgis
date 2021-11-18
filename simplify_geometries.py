from qgis import processing
import os

dir_path = "/Users/hosokawa/Desktop/simplify_test/"

for index, layer in QgsProject.instance().mapLayers().items():
    if layer.type() != QgsMapLayer.VectorLayer:
        continue

    file_name = layer.name()
    print(file_name)
    code = file_name[-5:]
    output = f"{dir_path}/{code}.shp"
    
    print("add area")
    calc_params = {
        'INPUT': layer,
        'FIELD_NAME': 'AREA',
        'FIELD_TYPE': 0,
        'NEW_FIELD': True,
        'FORMULA': '$area',
        'OUTPUT': 'memory:'
    }
    
    output1= processing.run("qgis:fieldcalculator", calc_params)
    
    print("simplify geom")

    parameters = {
        'INPUT': output1['OUTPUT'],
        'METHOD': 2,
        'TOLERANCE': 0.006,
        'OUTPUT': output
    }

    processing.run("native:simplifygeometries", parameters)
    iface.addVectorLayer(output, "", 'ogr')

    layer_options = ['GEOMETRY=AS_WKT','SEPARATOR=COMMA']

    vlayer = QgsVectorLayer(output, "", "ogr")
    QgsVectorFileWriter.writeAsVectorFormat(vlayer, f"{dir_path}/original/{code}.csv", "utf-8",layer.crs(), "CSV", layerOptions=layer_options)