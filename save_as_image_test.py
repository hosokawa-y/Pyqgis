layer = iface.activeLayer()

extent = layer.extent()
width, height = layer.width(), layer.height()
renderer = layer.renderer()
provider=layer.dataProvider()
crs = layer.crs().toWkt()

pipe = QgsRasterPipe()
pipe.set(provider.clone())
pipe.set(renderer.clone())

file_name = layer.name()

opts = ["COMPRESS=DEFLATE", "PREDICTOR=2", "ZLEVEL=9"]

file_writer = QgsRasterFileWriter(f'/Users/hosokawa/Map data/gyouseikuiki/kanto/keiryou_test/{file_name}-save12.tif')
file_writer.setCreateOptions(opts)

file_writer.writeRaster(pipe,
                        width,
                        height,
                        extent,
                        layer.crs())