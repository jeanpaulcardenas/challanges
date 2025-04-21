with open('./data.txt') as data:
    my_data = data.readlines()
    list_of_lists = [list(map(int, x.replace('\n', '').split(' '))) for x in my_data]


def checks(row):

    for idx, v in enumerate(row[0:len(row) - 1]):
        aux_value = v - row[idx + 1]
        if aux_value == 0 or abs(aux_value) > 3:
            return False
    else:
        ascending_row = row.copy()
        descending_row = row.copy()
        ascending_row.sort()
        descending_row.sort(reverse=True)
        if row in [ascending_row, descending_row]:
            return True

        else:
            return False


result = 0
for row in list_of_lists:
    if checks(row):
        result += 1

if __name__ == '__main__':
    print(result)
    print(len(list_of_lists))
