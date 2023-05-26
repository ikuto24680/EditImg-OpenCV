import glob

ngcatfile = open('ng/ngcatlist.txt', 'a')
# ngfile = open('ng/nglist.txt', 'a')
# okfile = open('ok/dog/okdoglist.txt', 'a')

print("開始")

# files = glob.glob("ng/hiramasa/*")
# for file in files:
#     ngfile.write(".\""+file+"\n")
#     print(file)

# Oks = glob.glob("ok\dog\*")
# for ok in Oks:
#     okfile.write(".\\"+ok+"\n")
#     print(ok)

files = glob.glob("ng\cat\*")
for file in files:
    ngcatfile.write(".\cv\\"+file+"\n")
    print(file)

ngcatfile.close()
# ngfile.close()
# okfile.close()
