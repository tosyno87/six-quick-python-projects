import os

def main():
    i = 0
    path = input("Input a path with png files to rename: ").replace("\\", "/") + "/"
    for filename in os.listdir(path):
        my_dest = f"img_{str(i)}.{filename.rsplit('.')[-1]}"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

main()