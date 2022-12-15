def open_file(filepath):
    data = []
    with open(filepath, 'r') as file:
        raw = file.readlines()

        for rule in raw:
            data.append(rule.strip('\n'))

    return data