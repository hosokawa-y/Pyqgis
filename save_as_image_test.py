layer = iface.activeLayer()

extent = layer.extent()
width, height = layer.width(), layer.height()
renderer = layer.renderer()
provider=layer.dataProvider()
crs = layer.crs().toWkt()

pipe = QgsRasterPipe()
pipe.set(provider.clone())
pipe.set(renderer.clone())

file_writer = QgsRasterFileWriter('/Users/hosokawa/vector_to_raster/output3.tif')

file_writer.writeRaster(pipe,
                        width,
                        height,
                        extent,
                        layer.crs())