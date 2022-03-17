l = ['Hans', 'Tove', 'Claus', 'Hannah']


def last_letter_in_name(x):
    return x[-1]


x = sorted(l, key=last_letter_in_name )

print(x)


print(l)
l.sort()
print(l)
