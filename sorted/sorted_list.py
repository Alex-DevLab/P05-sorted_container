from sortedcontainers import SortedList, SortedKeyList

sorted_list = SortedList()
sorted_list.add(50)
sorted_list.add(20)
sorted_list.add(20)
sorted_list.add(10)
sorted_list.add(30)

print(sorted_list)

sorted_list2 = SortedList()
sorted_list2.add('abcd')
sorted_list2.add('aBc')
sorted_list2.add('AbCd')
sorted_list2.add('ac')
sorted_list2.add('bdc')

print(sorted_list2)

sorted_list3 = SortedKeyList(key=str.casefold)  # case insensitive comparison
sorted_list3.add('abcd')
sorted_list3.add('aBc')
sorted_list3.add('AbCd')
sorted_list3.add('ac')
sorted_list3.add('bdc')

print(sorted_list3)
