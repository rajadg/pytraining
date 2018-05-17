'''
Created on 17-May-2018

@author: dgraja
'''


# declare a list
ls = [0, 1.0, 2, 3, 4, 5, '6', None, -1, 2, 3, 5]

s1 = 's1'
s13 = '''s1 
3'''
s2 = "s2"
s23 = """s2
3"""

ls.append(s1)
ls.append(s2)

list2 = [s13, s23]

final = ls + list2

# print a list
print (final, final.__class__.__name__)
# find length of the list
print (len(final))

# Get first element in list
print (final[0])
print ("last element", final[len(final)-1])
print ("last element", final[-1])
print ("last but one element", final[-2])

# Create a set from an existing list
st = set(final)
print (st, st.__class__.__name__, len(st))

# Declare a set from values
s1 = {1, -2, 3, 4, 3}
print (s1)

# a read only list
print ("tuples: ")
tp = tuple(final)
print (tp, len(tp), tp.__class__.__name__)

tp1 = tp + (1, )
print (tp1, len(tp1), tp1.__class__.__name__)
print (tp, len(tp), tp.__class__.__name__)

print("%r" % s13)
print(str(s13), repr(s13))

