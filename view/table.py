# function to create table in html
def print_table(table_data, column_name):
    # prepare the table's style
    table = """
    <style>
    table {
    border-collapse: collapse;
    width: 100%;
    }

    th {
    background-color: #C7332A;
    color: white;
    }
    </style>
    """

    # <table> opening tag
    table += "<table>"

    # create row for header
    table += "<tr>"
    # iterate words
    for name in column_name:
        # add word to the header
        table += f"<th>{name}</th>"
    # row closing tag
    table += "</tr>"

    # for every row in list
    for row in table_data:
        # create row for data
        table += "<tr>"
        # for every colum in row
        for column in row:
            # create column
            table += f"<td>{column}</td>"
        # row closing tag
        table += "</tr>"
    # table closing tag
    table += "</table><br>"

    # return the html table
    return table