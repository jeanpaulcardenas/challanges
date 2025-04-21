from solution1 import list_of_lists as lofl, checks


result = 0
for row in lofl:
    if checks(row):
        result += 1

    else:
        print(row)
        for idx, item in enumerate(row):
            new_row = row.copy()
            new_row.pop(idx)
            print(new_row)
            if checks(new_row):
                result += 1
                print('solved')
                break
            else:
                new_row.insert(idx, item)


print(result)
