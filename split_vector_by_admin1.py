# coding: utf-8
from qgis import processing
import os
import glob
import shutil

"""
処理内容
1. ローカルのベクタファイルをQGISに追加
2. 属性でベクタを分割
3. 分割したベクタをローカルに保存
"""

# working directory
working_dir = "/Users/hosokawa/Desktop/country/working/"
files = glob.glob(working_dir + "*.geojson")
counties = []

# 処理が終了したファイルの移動先
done_dir = "/Users/hosokawa/Desktop/country/00done/"
os.makedirs(done_dir, exist_ok=True)

# geojsonをvectorレイヤとして読み込み 
for file in files:
    file_name = file.replace(working_dir, "")
    print(file_name)
    iface.addVectorLayer(file, "", "ogr")

# 属性でベクタを分割
for index, layer in QgsProject.instance().mapLayers().items():
    if layer.type() != QgsMapLayer.VectorLayer:
        continue

    admin = layer.name().replace("admin_", "").replace(" ", "_")
    print(admin)
    counties.append(admin)

    dir_path = f'/Users/hosokawa/Desktop/country/{admin}'
    os.makedirs(dir_path, exist_ok=True)
    print(dir_path)

    params = {
        "INPUT": layer,
        "FIELD": "iso_3166_2",
        "FILE_TYPE": 8,  # geojsonで出力
        "OUTPUT": dir_path
    }
    processing.run("native:splitvectorlayer", params)

    # 処理が終わったファイルを移動
    previous_file_name = f"{layer.name()}.geojson"
    previous_file_path = f"{working_dir}{previous_file_name}"
    next_file_path = f"{done_dir}{previous_file_name}"
    shutil.move(previous_file_path, next_file_path)

print(counties)

# 読み込んだvectorレイヤを削除
QgsProject.instance().clear()
print('done')
