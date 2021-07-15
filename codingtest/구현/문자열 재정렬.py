import time


s = input()

start_time = time.time()

string_list = []
temp = 0

for i in s:
    if i.isalpha():
        string_list.append(i)
    else:
        temp += int(i)

string_list.sort()
string_list.append(str(temp))

end_time = time.time()

for j in string_list:
    print(j, end='')