import os

print("Files in current directory:")
for f in os.listdir("."):
    print(f)
    if os.path.isdir(f):
        print(f"--- Dir {f} contents: ", os.listdir(f)[:5])
