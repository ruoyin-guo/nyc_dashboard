

# df = pd.read_csv(
#     'D:\McGill\COMP598\hw4\submission_template\data\data_limit.csv', low_memory=False)

import csv
path = "/mnt/d/McGill/COMP598/hw4/submission_template/data/nyc_311_limit.csv"
path2 = "/mnt/d/McGill/COMP598/hw4/submission_template/data/trim_data.csv"
csv_data = []
with open(path, 'r', encoding='utf-8') as f:
    csvreader = csv.reader(f)
    for line in csvreader:
        if "/2020" in line[1]:
            csv_data += [line]
f.close()

with open(path2, 'w', encoding='utf-8') as wf:
    writer = csv.writer(wf)
    writer.writerows(csv_data)
wf.close()
