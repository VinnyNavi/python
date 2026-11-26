#List

""" l= [1,2,3,"abc","xyz",20,30,40,[11,12,"abc", True]]           
print(l, type(l))
print(l[3])                                                                             #it adds list inside nesed list append method
print(l[8][0])   #nested list

print( l[-1][0])   #fist list last index, 2nd list 0th position index value

print(l[len(l)-1][0])  #other way of last index position 

print(dir(l)) """

""" append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort' """

""" l.append([True, False])   #adding element into the list like [1,2,3,"abc","xyz",[True,False]]
l.insert(0,"xyz")  #if you want to add element perticular position so we need to use insert method
print(l) """

""" l= [1,2,3,"abc","xyz"]
l.extend([True, False])
print(l)        #[1, 2, 3, 'abc', 'xyz', True, False] extend method extends the individual list
 """
l=[3,2,1]
#l.sort()
l1=sorted(l)
print(l,l1)
