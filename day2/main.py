
with open('./data.txt') as data:
    my_data = data.readlines()
    list_of_lists = [list(map(int, x.replace('\n', '').split(' '))) for x in my_data]
    print(list_of_lists)
    result = 0
    for idx, row in enumerate(list_of_lists):
        for idx, v in enumerate(row[0:len(row) - 1]):
            aux_value = v - row[idx + 1]
            if aux_value == 0 or abs(aux_value) > 3:
                break
        else:
            ascending_row = row.copy()
            descending_row = row.copy()
            ascending_row.sort()
            descending_row.sort(reverse=True)
            if row in [ascending_row, descending_row]:
                result += 1

print(list_of_lists)
print(result)
print(len(list_of_lists))
