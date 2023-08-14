from pathlib import Path
path = Path("/home/junaid/Desktop")
print(path.exists())
# path.mkdir()
# print(path.iterdir())

for p in path.iterdir():
    pass
    # print(p)

paths = [p for p in path.iterdir()]
# print(paths)

# directory path
dir_path = [p for p in path.iterdir() if p.is_dir()]
# print(dir_path)

# glob function
py_files = [p for p in path.glob("*.py")]
# print(py_files)

py_files = [p for p in path.rglob("*.py")]

print(py_files)
