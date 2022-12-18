# convert raw rules into readable by Python
def raw_to_cfg(raw):
    # prepare empty list
    cfg = []

    # for each line in rules, split it by ' -> ', then append into cfg list
    for line in raw:
        cfg.append(line.split(' -> '))

    # for each body in rules, split the body by ' | ' then convert into set
    for rule in cfg:
        rule[1] = set(rule[1].split(' | '))

    # for each line in rules
    for rule in cfg:
        # prepare the empty set
        new_body = set()
        # for every element in body
        for element in rule[1]:
            # convert each body (variable and terminal) into tuple by splitting it by ' '
            element_to_tuple = tuple(element.split(' '))
            # append the tupple into new_body set
            new_body.add(element_to_tuple)
        # change the old body with new body format
        rule[1] = new_body

    # return the readable rules
    return cfg

# create rules in html format
def create_html(raw):
    # starting by <p> tag
    html_raw = '<p>'
    # for every rule in raw rules
    for line in raw:
        # append the rule to html_raw then end by <br>
        html_raw += f'{line}<br>'
    # end the html_raw by </p> tag
    html_raw += '</p>'

    # return the raw html rules
    return html_raw