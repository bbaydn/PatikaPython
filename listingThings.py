# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 20:33:00 2021

@author: BusraA
"""

differentList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

# We have different elements with different types
# We want to separate these elements from each other and create a new list


this_is_not_a_list = ','.join(str(_) for _ in differentList)

# With 'join', we separate it up to the place where there is a comma

this_will_be_list = this_is_not_a_list.replace("[","")
this_will_be_list = this_will_be_list.replace("]","")
this_will_be_list = this_will_be_list.replace("'","")

# With 'replace', we remove the characters we don't want to use

advanced_different_list = this_will_be_list.split(",")
print(advanced_different_list)
#print(type(new_M))

# With 'split', we create a new, different list and after that we print it

