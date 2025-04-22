import re


def read_input(file_path: str, filter_do_dont: bool):
    """Reads doc in filepath. obtains target numbers following instructions of 'enunciado.txt'
    returns a list of tupless of ints """
    with open(file_path, mode='r') as d:
        memory = d.read()

    if filter_do_dont:
        filtered = re.split("(do\(\))|don't\(\)", memory)  # returns list: [ txt, seperator, txt, ... ]
        print(filtered)
        result = [filtered[0]] + \
                 [value
                  for idx, value
                  in enumerate(filtered[2:len(filtered):2])
                  if filtered[2 * idx + 1] == "do()"
                  ]

        memory = ''.join(result)

    return memory


def find_valid_mul(memory):
    list_tuples = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', memory)

    for idx, elem in enumerate(list_tuples):
        list_tuples[idx] = [int(x) for x in elem]
    return list_tuples


# I'm not downloading numpy for a single simple function. Creating my own
def multiply_loft(data: list[tuple]):
    """multiply a list of tuples of ints and add them. tuples can have any args
    e.g: [(1, 2, 3), (3, 4, 5)] returns 1 * 2 * 3 + 3 * 4 * 5 = 66"""
    result = 0
    for my_tuple in data:
        aux = 1
        for num in my_tuple:
            aux *= num
        result += aux
    return result


read_memory = read_input('./data.txt', True)
my_tuples = find_valid_mul(read_memory)
solution = multiply_loft(my_tuples)
print(solution)
