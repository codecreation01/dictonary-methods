#clear() method

thedict={1:"cherry",2:"blossom"}
thedict.clear()
print(thedict)

#copy() method

thedict={'I':1,'II':2,'III':3,'IV':'4'}
newromannumber= thedict.copy()
print("original dictonary:",thedict)
print("copied dictonary:",newromannumber)

#fromkey() method

keys={'a','e','i','o','u'}
value='vowel'
vowels=dict.fromkeys(keys, values)
print(vowels)

#get() method

thedict={1:"cherry",2:"blossom"}
fruit=thedict.get()
print(fruit)

#pop() method

thedict={1:"cherry",2:"blossom"}
print(thedict)
thedict.pop(2)
print(thedict)


#popitem() method

thedict={1:"cherry",2:"blossom"}
print(thedict)
thedict.popitem()
print(thedict)

#setdefault() method

car={ "brand":"ford"
      "model": "mustang"
     "year" : 1964}

x= car.setdefault("model":"bronco")
print(x)


#dictonary.items()

dict1={'A':'geeks';'B':'god'}
print(dictonary items)
print(dictonary1 items)
