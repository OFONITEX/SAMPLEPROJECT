# python tuple
# tuple cannot be updated or deleted; faster processing than list; 
#can be accessed by indexing

t1 = (1, 2, 3) 

#access tuple
print(t1[1])

len(t1)

# python Dictionaries
# define and initialize a dictionary

address = {'Street' : '180 Adams Street',
           'City'   : 'Chicago',
           'State'  : 'IL',   
           'Country' : 'USA'}

print(address['Street'])

# add and update the key-value pair
address['Street'] = '181 Adams Steet'

address['zip'] = '60611'

# delete a key value pair
del address['zip']

# functions and methods on dictionary

# lenth of the dictionary
len(address)

# methods of keys

keys = address.keys()   #appear as adictionary sequence

keys = list(address.keys())
            
# values of the dictionary         
values = list(address.values())
                        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            