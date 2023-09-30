def load_numbers(file):
    data_list = []
    with open(file) as file:
        for line in file:
            data_list.append(int(line))
    
    return data_list
