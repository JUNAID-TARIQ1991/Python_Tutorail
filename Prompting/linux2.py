#!/usr/bin/env python3
import os
os.system('pwd')
os.system('ls')



path='/home/junaid/POWHEG-BOX-V2/W/WOrigional/'
os.chdir(path)
import shutil
shutil.copytree(path,'/home/junaid')