#read
#read  returns iterator   of characters
with open(r"C:\Users\Parth\Downloads\python-the-complete-python-developer-course\sample.txt") as file:
    lines=file.read()
for line in lines:
    print(line,end='')
