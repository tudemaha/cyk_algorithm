# open the cnf rule files
def open_file(filepath):
    # prepare the empty list
    data = []
    # open txt with read mode
    with open(filepath, 'r') as file:
        # read rule line by line
        raw = file.readlines()

        # append each rule into data list while remove the new line
        for rule in raw:
            data.append(rule.strip('\n'))

    # return the raw cnf rules
    return data