#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('hello world')


# In[2]:


y = 6
print(y)


# In[5]:


y = []
item = ([20, 40, 'man'])
item.append(item)


# In[3]:


x = 20
x


# In[4]:


x = 20*2
x


# In[5]:


name = ('my name is a girl')
name


# In[6]:


print(y + x)


# In[8]:


print(x + x % y)
print(x + y*x)


# In[12]:


# PHYTON FUNCTIONS

def add_numbers(x,y):
    return (x + y)


# In[13]:


add_numbers(6,40)


# In[15]:


def subtract_numbers(a,b):
    return(a - b)


# In[2]:


def multiply_numbers(a,b):
    return(a * b)
multiply_numbers(20,20)


# In[16]:


subtract_numbers(90,30)


# In[3]:


def add_numbers(d,f):
    return(d + f)
add_numbers(10,10)


# In[17]:


def devide ( d, a):
    return(d / a)


# In[18]:


devide(20,2)


# In[20]:


#  PHYTON IF, ELSE STATEMENT
x = 10
if(x > 5):
    print('x is greater than 5')
else:
    print('x is less than 5')
    


# In[4]:


y = 20
if(y > 16):
    print('y is greater than 16')
else:
    print(' y is less than 16')


# In[23]:


b = 10
if(b <40):
    print('b is greater than 40')
else:
    print('b is less than 40')


# In[24]:


# PHYTON DATA TYPES (STRING, INTERGER, NONETYPE, FLOAT)
type('i am a girl')


# In[5]:


type(30)
type('man')


# In[25]:


type(20)


# In[26]:


type(3.0)


# In[28]:


type(None)


# In[29]:


# DATA COLLECTION IN PHYTON 
# LIST,TUPLE AND DICTIONARY.

# TUPLE; This are imutable data structures and they 9can not be altered)

a = (4, "man", 6.2)
a


# In[30]:


# SLICING A TURPLE
# IN PHYTON NUMBERS STARTS FROM 0-9 SO IN SLICING A TURPLE THE FIRST NUMBER IS ASSIGNED 0,1,2,3 ETC
# INDEXING IN DATA COLLECTION IN PHYTON STARTS FROM 0

a[0]


# In[6]:


y = (20, 70, 'egg')
y


# In[ ]:





# In[31]:


a[1]


# In[32]:


a[2]


# In[35]:


print(a[0])
print(a[1])
print(a[2])


# In[40]:


# LIST

# A LIST ARE MUTABLE DATA STRUCTURES. A LIST CAN CONTAIN ANY TYPE OF DATA

x = [2, 30,"girl",2.0, "man"]


# In[42]:


type(x)


# In[43]:


x


# In[48]:


# HOW TO ADD TO AN EXISTING LIST IN PHYTON.
#     WE USE (.APPEND) TO ADD A VALUE TO AN EXISTING LIST.

x.append(6)
print(x)


# In[49]:


x.append(22)
print(x)


# In[50]:


# FOR LOOP: PHYTON PROGRAMMING
#     LOOPING MEANS (ITERATION) GOING OVER A CERTAIN NUMBER OF DATA STRUTURES 
#     OR OPERATIONS TO PERFORM A TASK ON THEM AGAIN.
#        TO WRITE A LOOP.
        
for item in x:
    print(item)


# In[55]:


y = [2, 5, 8, 4, 22]

for item in y:
    print(item + 2)


# In[57]:


a = [ 20, 4, 6,"man"]

for item in a:
    print(item * 3)


# In[58]:


#   OPERATIONS ON A LIST
# you can add 2 list by simply performing the operations below

[y] + [a]


# In[59]:


# YOU CAN MULTIPLY A LIST BY PERFORMING THE OPERATIONS BELOW

[a]*4


# In[62]:


[y]*3


# In[63]:


#   SLICING INDEXING IN A LIST
x = [20, 3, 5, 8]
x


# In[65]:


# PHYTON INDEXING STARTS FROM 0-9, SO THEREFORE 0 IS THE FIRST VALUE OF ANY LIST
print(x[0]) #first character

# WE CAN DO INDEXING IN PHYTON USING A RANGE
print(x[0:1])

# when setting a range in phyton subtract the last number by 1
print(x[0:2])

# this will print the first 2 character after subtrscting 1
#   TO PRINT THE LAST CHARACTER IN THE LIST USE THE - SIGN
print(x[-1])

# TO PRINT THE SECOND TO THE LAST NUMBER USE
print(x[-2]) 
# INSTEAD OF print(x[3])


# In[66]:


x[0:2]


# In[67]:


x[:2]


# In[ ]:




