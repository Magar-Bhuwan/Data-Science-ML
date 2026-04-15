#break & continue in for loop
a = [2,3,1,5,9,8]
search_num = 1
for element in a:
    if element == search_num:
        print("Element found")
        break

#continue in for loop
voters_age = [18,19,20,21,22,23,24]
for age in voters_age:
    if age >= 18:
        print("Voter id is being generated")
        continue
    print("not a voter")
    print("Voter id isnot being generated")
    remaining_age = 18-age
    print(f'{remaining_age}' + ' years remaining')