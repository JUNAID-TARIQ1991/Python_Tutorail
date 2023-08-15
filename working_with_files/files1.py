from pathlib import Path
from time import ctime
import shutil
import os

path = Path("/home/junaid/Desktop/PYTHON3/sample.txt")
destination = Path("/home/junaid/Desktop")
print(path.exists())
print(path.stat())
print(path.stat().st_ctime)
print(ctime(path.stat().st_ctime))

# read a file
# print(path.read_bytes())
# print(path.read_text())
# write to a file
# path.write_text("Ok this is new line using Path")
# path.write_bytes(b"Ok bytes here")
print(path.absolute())

# copying file content
shutil.copy(path, destination)
print(os.listdir(destination))
