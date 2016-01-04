all_files = [
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-1A.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-1B.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-1C.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-1D.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-2A.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-2B.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-2C.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-2D.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-3A.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-3B.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-3C.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-3D.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-4A.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-4B.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-4C.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-4D.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-4E.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-4F.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-4G.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-4H.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-5A.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-5B.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-5C.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-5D.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-5E.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-5F.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-5G.tex',
'/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-6.tex']

output = '/Users/kevindunn/Dropbox/Coursera/Media/All-course-slides/classes/CourseraMOOC-class-all.tex'

out = file(output, 'wt')

for fname in all_files:
    with file(fname, 'r') as fobj:
        out.writelines(['\n\n',
                        '% {0}'.format(fname),
                        '\n\n'])
        out.writelines(fobj.readlines())



out.close()