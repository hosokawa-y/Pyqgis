import glob
import csv
import re
import os
from typing import Tuple
import shutil

city = 'kanagawa'
# path = f'/Users/hosokawa/Desktop/simplify_test/{city}/original/'
path = f'/Users/hosokawa/Desktop/need_retry/{city}/'
new_dir = f'/Users/hosokawa/Desktop/simplify_test/{city}/result'
need_retry_folder = f'/Users/hosokawa/Desktop/need_retry/{city}'

def main():
    files = glob.glob(path + '*.csv')
    need_retry_csv = []
    need_check_areas = []

    # 作成したCSVの置き場所作成
    if not os.path.exists(new_dir): 
        os.mkdir(new_dir)
    
    # リトライ用CSVの置き場所作成
    if not os.path.exists(need_retry_folder): 
        os.mkdir(need_retry_folder)

    for file in files:
        file_name = os.path.split(file)[1]
        new_file = f'{new_dir}/{file_name}'
        print(f'\n start: {file_name}')

        with open(new_file, 'w') as new_file:
            writer = csv.writer(new_file)
            rows = []

            with open(file) as f:
                reader = csv.reader(f)
                for index, column in enumerate(reader):
                    if index == 0:  # ヘッダー行は無視
                        continue
                    wkt = column[0]
                    area = column[-1]

                    if float(area) < 50000.0:  # 小さいエリアは無視
                        continue

                    polygon_list, need_check = extract_polygon(wkt)  # wktをポリゴン単位で分割                    
                    rows.extend(polygon_list)
                    if need_check:
                        need_check_areas.append(file_name)

                writer.writerows(rows)
                
                if not len(rows):
                    print('\n This csv have some trouble. Please check data.')
                    need_retry_csv.append(file_name)
                    shutil.copy(file, need_retry_folder)
                else:
                    print("done")
            
    print("Need retry: ")
    print(need_retry_csv)
    print("need check: ")
    print(need_check_areas)


def extract_polygon(wkt: str) -> Tuple[list, bool]:
    m_pattern = 'MULTIPOLYGON ('
    p_pattern = '(\(\([0-9., ]+\)\))'
    d_pattern = '[0-9., ]+'
    result = []
    need_check = False

    # MULTIPOLYGONを削除
    delete_prefix = wkt.replace(m_pattern, '')
    # 1ポリゴンずつ座標群を取得
    m = re.findall(p_pattern, delete_prefix)
    print(f'total {len(m)} polygons in this row')

    # まだ入れ子構造が残っている場合はログに残す
    for i, item in enumerate(m):
        points = re.findall(d_pattern, item)
        print(f'found nesting...{len(points)} areas in this points.')
        if len(points) > 1:
            print('\n please check!!!!!!!!! \n')
            print(f'{i}: {item}')
            need_check = True
        
        swapped = swap_xy(points)
        result.append(swapped)
            
    return result, need_check


def swap_xy(points: list) -> list:
    st = ''
    # 経度緯度を入れ替え
    for index, p in enumerate(points):
        templist = p.split(',')

        for v in templist:
            val = v.split(' ')
            swapped = f'[{val[1]},{val[0]}],'
            st += swapped

        points[index] = f'{st[:-1]}'  # 末尾のカンマを削除
    
    return points

if __name__ == '__main__':
    main()