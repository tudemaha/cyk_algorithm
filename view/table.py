def print_table(table_data, column_name):
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

    table += "<table>"

    table += "<tr>"
    for name in column_name:
        table += f"<th>{name}</th>"
    table += "</tr>"

    for row in table_data:
        table += "<tr>"
        for column in row:
            table += f"<td>{column}</td>"
        table += "</tr>"
    table += "</table><br>"

    return table