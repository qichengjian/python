from pathlib import Path

path = Path("path")
print(path.exists())

print(Path("path2").exists())




path= Path()
for file in path.glob("*.py"):
    print(file)

###Path对象常用方法
###exists mkdir rmdir glob(遍历当前目录, 搜索文件)