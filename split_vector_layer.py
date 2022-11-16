from qgis import processing
import os

## split vector layer by attribute

layer = iface.activeLayer()


# split vector layer
dir_path = f'/Users/hosokawa/Desktop/country/'
os.makedirs(dir_path, exist_ok=True)

params = {
    'INPUT':QgsProcessingFeatureSourceDefinition(
        layer, 
        selectedFeaturesOnly=False,
        featureLimit=-1, 
        flags=QgsProcessingFeatureSourceDefinition.FlagOverrideDefaultGeometryCheck,
        geometryCheck=QgsFeatureRequest.GeometrySkipInvalid
        ),    # input layer name
    'FIELD':'admin',   # Field to use for splitting
    'FILE_TYPE':'8',  # export to GeoJSON
    'OUTPUT':dir_path
    }

processing.run("native:splitvectorlayer", params)

print('done')