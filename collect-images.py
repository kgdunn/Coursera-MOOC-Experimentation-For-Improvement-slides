import os
from shutil import copyfile


destination = '/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/images'
imagedir = '/Users/kevindunn/Dropbox/figures-master'
latex_file = '/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/CourseraMOOC-class-all.tex'
base_dir, filename = os.path.split(latex_file)
mooc_dir = '/Users/kevindunn/Dropbox/Coursera/Media'
with open(latex_file,'r') as f:
    for line_idx, line in enumerate(f.readlines()):
        if line.strip().startswith('%'):
            continue


        idx = line.find(r'\includegraphics')
        if idx >=0:

            filename = line[idx:].split('{')[1]
            if filename.startswith(r'\imagedir'):
                filename = filename.split('}')[0].split(r'\imagedir')[1].strip(os.sep)
                src = os.path.join(imagedir, filename)
                assert os.path.exists(src)

                dst = os.path.join(destination, filename)
                os.makedirs(os.path.dirname(dst), exist_ok=True)

                copyfile(src, dst)

            else:
                filename = filename.split('}')[0].split(r'\moocimages')[1].strip(os.sep)
                src = os.path.abspath(os.path.join(mooc_dir, filename))
                assert os.path.exists(src)

                dst = os.path.abspath(os.path.join(destination, filename))
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                copyfile(src, dst)