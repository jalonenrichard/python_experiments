filename = "textfile.txt"

with open(filename) as f:
    content=f.readlines()

print(content)

infile = open(filename, 'r')
data = infile.read()
infile.close()

print(data)
