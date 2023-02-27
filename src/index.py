from pathlib import Path
import csv

# path = pathlib.Path(r"C:\root\media\private\me.jpeg")
# path1 = pathlib.Path(r"C:\Users\USER\Pictures\Saved Pictures")
# print(path.is_absolute())
# print(path.exists())
# path2 = path.home() / "new_dir" / "names.txt"
# path3 = path.cwd()
# print(path1.is_absolute())
# print(path2.is_absolute())
# print(path3.is_absolute())
# print(path2.exists())
# print(path3.exists())
# print(path.name)
# print(path.suffix)
# print(path.stem)
# print(path.anchor)
# print(path.parent.parent)

# print(list(path.parents))


# path2.touch()
# cwd = pathlib.Path.cwd()

# dir = [
#   pathlib.Path.cwd() / "new_directory1",
#    pathlib.Path.cwd() / "new_directory2",
#   pathlib.Path.cwd() / "new_directory3",
#   pathlib.Path.cwd() / "new_directory4",
# ]

# for path in dir:
#    path.mkdir(exist_ok=True)

# for dir in cwd.iterdir():
# for dir in cwd.glob("**/*"):
#   print(dir)
#   for dir in cwd.rglob("new_directory[1234]"):
#      print(dir)

# source = pathlib.Path.cwd() / "new_directory" / "dir_2" / "unknown.txt"
# print(source.exists())

# destination = pathlib.Path.cwd() / "new_directory1" / "unknown.txt"
# source.replace(destination)
#
# path = pathlib.Path.cwd() / "new_directory" / "lovestory.txt"
# path.touch()
#
# numbers = [
#     [29, 23, 61, 26, 32],
#     [80, 70, 50, 40, 60],
#     [53, 42, 72, 45, 46]
# ]
#
# with path.open(encoding="utf-8", mode="w") as file:
#     for number in numbers:
#         file.write(f"{number[0]}")
#         for num in number[1:]:
#             file.write(f",{num}")
#         file.write("\n")
#
#     print(file.readlines())
#   print(file.read())

#  file.write("Hello Yemi,\n")
#  file.write("I really miss you. I will join you during break")
# file.close()
# print(file)

# path.touch()

# destination = pathlib.Path.cwd() / "new_directory2" / "femi.txt"
#new_path = pathlib.Path.cwd() / "new_directory2"
# shutil.rmtree(new_path)
# new_path.rmdir()

#
# numbers = [
#     [29, 23, 61, 26, 32],
#     [80, 70, 50, 40, 60],
#     [53, 42, 72, 45, 46]
# ]
# def decoode(string):
#     lst = string.split(",")
#     print([int(num) for num in lst])
#
# with open(path, encoding="utf_8",mode="r") as file:
#     lines = file.readline()
#     for line in lines:
#         decoode(line)

# with open(path, encoding="utf_8", mode="r") as file:
#     file.read() ((((gitkatas,goodfirst issues)))

# path = Path.cwd() / "new_directory" / "consensus.csv"
path = Path("C:/Users/USER/PycharmProjects/pythonProject/src") / "new_directory" / "consensus.csv"
path.touch()

census = [
    {"name": "Timmy",
     "isSingle": False,
     "cohort": 15,
     "status": "COMPLICATED"
     },
    {"name": "Rid",
     "isSingle": True,
     "cohort": 15,
     "status": "UNKNOWN"
     },
    {"name": "Ned",
     "isSingle": True,
     "cohort": 15,
     "status": "UNDISCLOSED"
     },
]
with open(path, encoding="utf-8", mode="r+") as file:
    # writer = csv.writer(file)
    # writer.writerows(numbers)
    writer = csv.DictWriter(file, fieldnames=["name", "isSingle", "cohort", "status"])
    writer.writeheader()
    writer.writerows(census)

