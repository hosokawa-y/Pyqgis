for index, rlayer in QgsProject.instance().mapLayers().items():
    file_name = rlayer.name()
    
    if rlayer.type() != QgsMapLayer.RasterLayer:
        print(f"pass: {file_name}")
        continue
    
    print(file_name)
    stats = rlayer.dataProvider().bandStatistics(1, QgsRasterBandStats.All)

    # get the minimum and maximum values.

    min = stats.minimumValue
    max = stats.maximumValue

    # create and empty color ramp shader
    fnc = QgsColorRampShader()

    # set type of color ramp we want to use
    fnc.setColorRampType(QgsColorRampShader.Interpolated)

    # define a color scheme

    lst = [QgsColorRampShader.ColorRampItem(min, QColor(255,0,0)),
    QgsColorRampShader.ColorRampItem(max, QColor(255,0,0))]

    fnc.setColorRampItemList(lst)

    # assign the color ramp to a QgsRasterShader

    shader = QgsRasterShader()
    shader.setRasterShaderFunction(fnc)

    # Apply symbology to raster

    renderer = QgsSingleBandPseudoColorRenderer(rlayer.dataProvider(), 1, shader)
    rlayer.setRenderer(renderer)

    # set transparancy
    rlayer.renderer().setOpacity(0.5)
    rlayer.triggerRepaint()