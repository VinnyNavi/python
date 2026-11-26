#tuple
t=(1,2,3,[True, False])
print(t, type(t))

t1 =t[-1]
print(t1)

#tuple is immutable once defined we cann't change like t[o]= 100 , it will through error we cant assign the element

print(dir(t))

# 'count', 'index'

print(t.index(3))

t=(1,2,3,1,5,6)
print(t.count(1))

#unpacking

t=(1,2)
#t=[1,2]

t1,t2=t
print(t1,t2)