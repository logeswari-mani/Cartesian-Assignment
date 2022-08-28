#!/usr/bin/env python
# coding: utf-8

# # Reverse the words in a string

# In[1]:


def wordReverse(str):
    i = len(str)-1
    start = end = i+1
    result = ''
 
    while i >= 0:
        if str[i] == ' ':
            start = i+1
            while start != end:
                result += str[start]
                start += 1
            result += ' '
            end = i
        i -= 1
    start = 0
    while start != end:
        result += str[start]
        start += 1
    return result
 

str = "This declaration represents a political commitment among declaration partners to advance a positive vision for the Internet in this era of a united europe";
print(wordReverse(str))


# In[2]:


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(word_count("This declaration represents a political commitment among declaration partners to advance a positive vision for the Internet in this era of a united europe"))


# ## Alter method

# In[3]:


string = "This declaration represents a political commitment among declaration partners to advance a positive vision for the Internet in this era of a united europe";
words = string.split()
words = list(reversed(words))
print(" ".join(words))


# In[4]:


from collections import Counter
Counter = Counter(words)


# In[5]:


most_occur = Counter.most_common(2)


# In[6]:


print(most_occur)

