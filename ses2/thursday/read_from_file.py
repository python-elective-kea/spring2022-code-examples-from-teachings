f = open('bohr.txt', 'r')

text = f.read()

f = open('bohr.txt', 'r')
text2 = f.readline()

f = open('bohr.txt', 'r')
x = f.readlines()

print(x)



f = open('test.txt', 'a+')
f.write('Hello world')
