import glob
import csv
import re
import os

path = "/Users/hosokawa/Desktop/simplify_test/csv4/"
files = glob.glob(path + "*.csv")

# file = "/Users/hosokawa/Desktop/temp3.csv"
new_dir = "/Users/hosokawa/Desktop/simplify_test/csv"
pattern = '(MULTIPOLYGON \(\(\(|\)\)\))'

for file in files:
    file_name = os.path.split(file)[1]
    new_file = f"{new_dir}/{file_name}"

    with open(new_file, "w") as new_file:
        writer = csv.writer(new_file)

        with open(file) as f:
            reader = csv.reader(f)
            for index, column in enumerate(reader):
                if index == 0:  # ヘッダー行は無視
                    continue
                wkt = column[0]
                area = column[-1]

                if float(area) < 50000.0:  # 小さいエリアは無視
                    continue

                result = re.sub(pattern, '', wkt)  # wktを加工
                st = ''
                templist = result.split(',')
                for v in templist:
                    val = v.split(' ')
                    swapped = f"[{val[1]},{val[0]}],"
                    st += swapped
                multipolygon = f"{st[:-1]}"
                print(multipolygon)
                row = [multipolygon]
                writer.writerow(row)