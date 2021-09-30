url - "https://www.credu.com/?page=" + str(1)
print( url )

f = open("c:\\work\demo.txt","wt" )
f.write("첫번째\n두번째\n세번째\n")
f.close()

f = open("c:\\work\demo.txt","rt" )
result = f.read()
print(result)
print("어디쯤:",f.tell())

f.seek(0)
print( f.readline() )
print( f.readline() )

f.seek(0)

lst = f.readline()
print( lst )
f.close()
