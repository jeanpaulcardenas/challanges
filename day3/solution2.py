import re


def read_input(file_path: str, filter_do_dont: bool):
    """Reads doc in filepath. obtains target numbers following instructions of 'enunciado.txt'
    returns a list of sets of ints """
    with open(file_path, mode='r') as d:
        first_data = d.read()

    if filter_do_dont:
        filtered = re.split("do\(\)|(don't\(\))", first_data)  # returns list: [ txt, seperator, txt, ... ]

        result = [value
                  for idx, value
                  in enumerate(filtered[2:len(filtered):2])
                  if filtered[2*idx + 1] != "don't()"
                  ]

        first_data = ''.join(result)

    list_sets = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', first_data)
    # r' -> define as raw string
    # \( and \) finds the actual symbol '('  and ')'
    # () returns value or values
    # \d digit
    # {1,3} from 1 to 3 characters -> so from 0 to 999

    for idx, elem in enumerate(list_sets):
        list_sets[idx] = {int(x) for x in elem}

    return list_sets


# I'm not downloading numpy for a single simple function. Creating my own
def multiplt_lofs(data: list[set]):
    """multiply a list of sets of ints and add them. sets can have any args
    e.g: [(1, 2, 3), (3, 4, 5)] returns 1 * 2 * 3 + 3 * 4 * 5 = 66"""
    result = 0
    for my_set in data:
        aux = 1
        for num in my_set:
            aux *= num
        result += aux
    return result


my_list_of_sets = read_input('./data.txt', True)
# part1:
sol_1 = multiplt_lofs(my_list_of_sets)
print(sol_1)