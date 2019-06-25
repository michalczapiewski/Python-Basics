luckey_numbers=[4,8,9,18,42,56]
friends=["Kevin","Jack","Jane","Oscar","Toby"]
print(friends)
print(luckey_numbers)
#2
friends.extend(luckey_numbers)
print(friends)
3#

luckey_numbers=[4,8,9,18,42,56]
friends=["Kevin","Jack","Jane","Oscar","Toby"]
#5
friends.append("Olek")
print(friends)
#5

friends.insert(1, "Aleksander")
print(friends)

#6

friends.remove("Olek")
print(friends)

#7
friends.clear()
print(friends)

#8
luckey_numbers=[4,8,9,18,42,56]
friends=["Kevin","Jack","Jane","Oscar","Toby"]
#9
friends.pop()
print(friends)

#10
print(friends.index("Jane"))

#11
print(friends.count("Jim"))

#12
friends.sort()
luckey_numbers.sort()
#13
friends.reverse()
luckey_numbers.reverse()
#14
friends2=friends.copy()
print(friends2)