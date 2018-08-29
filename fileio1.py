file=open(r"C:\Users\Parth\Downloads\python-the-complete-python-developer-course\sample.txt")

for line in file:
    if 'jabberwock' in line.lower():
        print(line,end='')

file.close()
print('\n\n\n')

# no we will do file handling in puthonic way
#no need to close the file

with open(r"C:\Users\Parth\Downloads\python-the-complete-python-developer-course\sample.txt") as file:
    for line in file:
        if 'jabberwock' in line.lower():
            print(line, end='')





