#! python3
# Scans all subdirectories and creates CBZ from files in them
# Subdirectories must contain valid image files

# @author Stephane Duguay // binarez

import os
import zipfile

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

subdirs = get_immediate_subdirectories(os.getcwd())
for subdir in subdirs:
	cbz_filename = subdir + '.cbz'
	zipf = zipfile.ZipFile( cbz_filename, 'w', zipfile.ZIP_DEFLATED)
	zipdir(subdir, zipf)
	zipf.close()
	print('Created : ' + subdir + '.cbz')