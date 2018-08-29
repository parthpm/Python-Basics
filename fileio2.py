
#readline
#readline returns string

with open(r"C:\Users\Parth\Downloads\python-the-complete-python-developer-course\sample.txt") as file:
    line=file.readline()
    print(line)
    while line:
        print(line,end='')
        line=file.readline()


