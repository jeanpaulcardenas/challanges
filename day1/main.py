
with open('./data.txt', mode='r') as data:
    data_list = data.readlines()
    data_list = [(x.replace('\n', '')).split() for x in data_list]
    data_1 = [int(x[0]) for x in data_list]
    data_2 = [int(x[1]) for x in data_list]
    data_1.sort()
    data_2.sort()
    result = sum([abs(a - b) for a, b in zip(data_1, data_2)])
    print(result)

    result_2 = sum([a*data_2.count(a) for a in data_1])
    print(result_2)


