rlayer = iface.activeLayer()
print(rlayer.name())

# get statistics for the raster band so we can properly stretch a color ramp. 
# The number 1 is the raster band we are getting stats for.

stats = rlayer.dataProvider().bandStatistics(1, QgsRasterBandStats.All)

# get the minimum and maximum values.

min = stats.minimumValue
max = stats.maximumValue


# create and empty color ramp shader
fnc = QgsColorRampShader()

# set type of color ramp we want to use
fnc.setColorRampType(QgsColorRampShader.Exact)

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
rlayer.renderer().setOpacity(0.3)
rlayer.triggerRepaint()