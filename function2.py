def intersect(prelist, postlist):
    retList = []
    for x in prelist:
        if x in postlist and x not in retList:
            retList.append(x)
    return retList


print( intersect("HAM", "SPAM") )

def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result


print( union("HAM","EGG") )
print( union("HAM","EGG","SPAM") )




a = 1.2
print( id(a) )
a = 2.3
print( id(a) )



lst = [1,2,3]
print( id(lst) )
lst.append(4)
print( id(lst) )



g = lambda x,y:x*y
print( g(3,4) )
print( (lambda x:x*x)(3) )

print( globals() )
