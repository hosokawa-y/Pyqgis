import processing

input = "/Users/hosokawa/vector_to_raster/2821900.tiff"
style = "/Users/hosokawa/vector_to_raster/regioncode_2722800.qml"

parameters = {
    'INPUT': input,
    'STYLE': style
}


result = processing.run("qgis:setstyleforrasterlayer", parameters)