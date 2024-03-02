My_List = [1, 2, 3, 4, 5]
iremove = 5

inlen = len(My_List)
new_len = inlen
itcount = My_List.count(itremove)

while len(My_List) != new_len:
    My_List.remove(itremove)
    new_len = len(My_List)

print("تعداد 5 های حذف شده: {itcount}")
print("لیست کلی:", My_List)
#leylanajafi
