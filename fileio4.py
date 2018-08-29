#readlines
#readlines returns list of strings
with open(r"C:\Users\Parth\Downloads\python-the-complete-python-developer-course\sample.txt") as file:
    lines=file.readlines()
print(lines)
for line in lines:
    print(line,end='')

