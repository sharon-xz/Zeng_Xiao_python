#common python functions

test_str = "ewhfuwihfuuwirhfuirh"
test_list = [1,2,3,2]

len(test_str)
# for loop, don't len(string)-1, automatically -1

null = None

test_list.sort() 

del test_list[1]
#delete an element in a list

for i in range(3):
    print (i,"\n")

for i in range(1,10,2):
    print (i)
#13579

#0,1,2  range(start, stop,step)
    
if (test_str=="yyyy") or (test_str=="fwfr"):
    print("no")
    
#Add an element to a list
test_list.append("3333")
print(test_list)