# ex 2
def sort_cons(s):
    for i in ['a', 'e', 'i', 'o', 'u', 'y', ' ']:
        s = s.lower().replace(i,'')
    
    return sorted(s)

print(sort_cons('Hello world'))

# Ex 3: Sort a list
# sort a list

# Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])
 names = [‘Claus’, ‘Ib’, ‘Per’]

# Sort this list by using the sorted() build in function.
sorted_names = sorted(names)

#  Sort the list in reversed order.
sorted_names_reversed = sorted(names, reverse=True)

# Sort the list on the lenght of the name.
length = sorted(names, key=len)

# Sort the list based on the last letter in the name.
def last(s):
    return s[-1]

sorted(names, key=last)

#  Sort the list with the names where the letter ‘a’ is in the name first.
def a_in(s):
    if 'a' in s.lower():
        return True
    return False

sorted(names, key=a_in)

# Ex 4: Files
# Create a file and call it lyrics.txt (it does not need to have any content)

open('lyrics.txt', 'w')

# Create a new file and call it songs.docx and in this file write 3 lines of text to it.

f = open('songs.docx' 'w')
f.writeline('Hello')
f.writeline('World')
f.writeline('And you')

#open and read the content and write it to your terminal window. 
* you should use both the read(), readline(), and readlines() methods for this. (so 3 times the same output).

f = open('songs.docx', 'r')
print(f.read())

f = open('songs.docx', 'r')
line = f.readline()
while line:
    print(line)
    line = f.readline()


f = open('songs.docx', 'r')
for i in f.readlines():
    print(i)


# Ex 5: Sort a list of tuples
# 1. Based on this list of tuples: [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]

lt = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3,1)]

# 2. Sort the list so the result looks like this: [(2, 1), (3, 1), (10, 1), (1, 2), (2, 2), (2, 2), (3, 2), (10, 4), (1, 5)] 

def last_then_first(x):
    return (x[1], x[0])

sorted(lt, key=last_then_first)

