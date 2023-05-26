import os
import samplecreate

# パスの取得&リスト作成　
path = r'C:\Users\pengi\OpenCVProject\cv\ok\dog'  # ポジティブ画像があるファイルのフルパス
files = os.listdir(path)

for dir in files:
    samplecreate.main(dir)
