# -*- encoding: utf-8 -*-
import os
import glob

flist = glob.glob('Rokutosei_particle 1224.mp4*')
print(flist)
for f in flist:
    ft = f.replace('Rokutosei_particle 1224.mp4','')
    os.rename(f, ft)
    