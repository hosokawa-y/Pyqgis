for index, layer in QgsProject.instance().mapLayers().items():
    file_name = layer.name()

    if layer.type() != QgsMapLayer.RasterLayer:
        print(f"pass: {file_name}")
        continue
    
    print(file_name)
    extent = layer.extent()
    width, height = layer.width(), layer.height()
    renderer = layer.renderer()
    provider=layer.dataProvider()
    crs = layer.crs().toWkt()

    pipe = QgsRasterPipe()
    pipe.set(provider.clone())
    pipe.set(renderer.clone())
    
    # compressing raster
    opts = ["COMPRESS=DEFLATE", "PREDICTOR=2", "ZLEVEL=9"]

    file_writer = QgsRasterFileWriter(f'/Users/hosokawa/Map data/gyouseikuiki/kanto/output/{file_name}.tif')
    file_writer.setCreateOptions(opts)
    file_writer.writeRaster(pipe,
                            width,
                            height,
                            extent,
                            layer.crs())

print("done")