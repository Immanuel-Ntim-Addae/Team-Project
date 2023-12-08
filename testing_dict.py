initial_dict = {'foo':['A','B','C'],'bar':['Q','Z','D']}

new_dict = {'foo':{'Hello':97}}

append_attempt = initial_dict['foo'].append(new_dict['foo']) #this format works. 

print(initial_dict)
#final dict = {'foo':[['A','B','C'],'Hello'], 'bar':[['Q','Z','D'], 'Man']}

a =['j',97,'k']
print(type(a))
#how to get a value out of a dictionary

print(initial_dict['foo'])

#testing category
li = [20.5,21,30,50,99,45,21,90,23,45,67,34,89]

for number in li:
    if number>20 and number<30:
        print(number)

strx = ["Hello", "My", "name" ,"is"]
for word in strx:
    print(word)