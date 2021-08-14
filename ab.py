import os
import shutil

try:
    os.system("git clone git@github.com:maxall41/apps-no-redis.git")
except:
    print("")

source_dir = './apps-no-redis'
target_dir = 'C:/Users/maxcampbell/'

file_names = os.listdir(source_dir)

for file_name in file_names:
    if (file_name[0] != "."):
        shutil.unpack_archive(os.path.join(source_dir, file_name), target_dir)