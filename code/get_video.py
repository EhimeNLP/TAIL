# 動画をダウンロードするコード

import requests, sys

input_txt = sys.argv[1]
input_dir = sys.argv[2]

with open(input_txt, mode='r') as f:
    data = f.readlines()
    
for line in data:
    part = line.strip().split('\t')

    url = part[4]
    id = part[1]

    #確認用
    print(id)

    if not url.startswith("http"):
        break
    
    response = requests.get(url)

    name = '{0}/{1}.mp4'.format(input_dir, id)

    with open(name, 'wb') as saveFile:
        saveFile.write(response.content)
