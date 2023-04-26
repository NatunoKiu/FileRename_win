# -*- encoding: utf-8 -*-
import os
import glob

flist = glob.glob('Kanane_Mari 10*')
print(flist)
for f in flist:
    ft = f.replace('Kanane_Mari ','Kanane_Mari 2021')
    os.rename(f, ft)
    