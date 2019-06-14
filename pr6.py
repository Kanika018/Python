
f=open("file.txt","r")
"""print(f.read())


for line in f:
    print(line.strip()+"$")

count=1
for line in f:
    print(str(count)+line.strip())
    count+=1

"""

i=5
for line in f:
    if line.strip()!="":
        print(str(i)+"."+line.strip())
        i+=1
