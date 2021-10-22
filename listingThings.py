'''
The first task:

Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]


'''

differentList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

# There are different elements with different types
# The task is, separating these elements from each other and creating a new list


this_is_not_a_list = ','.join(str(_) for _ in differentList)

# With 'join', separate it up to the place where there is a comma

this_will_be_list = this_is_not_a_list.replace("[","")
this_will_be_list = this_will_be_list.replace("]","")
this_will_be_list = this_will_be_list.replace("'","")

# With 'replace', remove the unwanted characters 

advanced_different_list = this_will_be_list.split(",")
print(advanced_different_list)


# With 'split', create a new, different list and after that print it


'''
The second task is:
    
Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]

    

'''



firstVersion = [[1, 2], [3, 4], [5, 6, 7]]

#Firstly, a list created

secondVersion = reversed(firstVersion)

#Reversed it, the output of this [[5,6,7],[3,4],[1,2]]


reversedVersion = [e[::-1] for e in secondVersion]

#That reverses a list within a list

print(reversedVersion)


