import os

START = os.getcwd()
#print(START)
LIST = os.listdir(START)
md_folders = []

for item in LIST:
    if (os.path.isdir(item) == True):
        if item == ".git":
            pass
        else:
            md_folders.append(item)
            #print(item + ' is a directory')
    else:
        pass

#print(sorted(md_folders))
f = open("exports/export-command.txt", "a")
f.write("pandoc -o exports/collection.md ")
f.close()
for folder in sorted(md_folders):
    files = sorted(os.listdir(folder))
    for file in files:
        if file.endswith('.md'):
            line = folder+"/"+file+" "
            print(line)
            f = open("exports/export-command.txt", "a")
            f.write(line)
            f.close()
        else:
            pass
print("done writing batch file.")


f = open("exports/export-command.txt", "r")
command = f.read()
print command
os.system(command)
print("done export!")

# TODO:
# ignore files without XX- formatting > "store.md", etc.
# open exports/collection.md
# remove all "------------------------------------------------------------------------"
# export final pdf file
