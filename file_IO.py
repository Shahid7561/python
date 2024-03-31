# you can read from file, you can write in file or you can append in file 

# Reading from file - it will give error if file is not there
# with open("notes.txt","r") as f:
    # print(f.read()) read whole file
    # print(f.readline()) read first line of file
    # print(f.readlines()) read line by line from file

# Writing in files - it will create new file if file is not there
# with open("demo.txt","w") as w:
#     w.write("Hello i am writing in file using file IO of python")

# Appending in files - it will create new file if file is not there and if it is there it will append the text to it
with open("demo.txt","a") as a:
    a.write("Appending in file through File IO")