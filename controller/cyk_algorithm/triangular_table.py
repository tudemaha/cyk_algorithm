import streamlit as st
from pandas import DataFrame

empty = '\u2205'

def create_table(list_of_string):
    table = []
    for i in range(len(list_of_string)):
        table.append([])
        for j in range(len(list_of_string)):
            if i < j:
                table[i].append(' ')
            else:
                table[i].append(set())
    
    return table

def filling_botton(table, cnf, list_of_string):
    for i, word in enumerate(list_of_string):
        cell = set()
        for row in cnf:
            for element in row[1]:
                if word in element:
                    cell.add(row[0])
                    break

        table[i][i] = cell


def filling_all(cnf, table, string, row = 1):
    if table[len(table) - 1][0] != set():
        if 'X' in table[len(table) - 1][0]:
            st.write('Accepted')
        else:
            st.write('Not accept')

        return

    next_row = iteration(cnf, table, string, row)

    filling_all(cnf, table, string, next_row)


def iteration(cnf, table, input_string, row):
    for column in range(len(table) - 1, -1, -1):
        if table[row][column] == set():

            list_of_intersect = []
            for i in range(0, row):
                if table[i][column] == empty:
                    list_of_intersect.append(set())
                elif table[i][column] != ' ' and table[i][column] != set():
                    list_of_intersect.append(table[i][column])

            for i in range(column + 1, len(table)):
                if table[row][i] == empty:
                    list_of_intersect.append(set())
                elif table[row][i] != ' ' and table[row][i] != set():
                    list_of_intersect.append(table[row][i])

            # print(list_of_intersect)

            result_list = make_combination(list_of_intersect)
            print(result_list)

            combine_result = combine(result_list)
            # print(combine_result)

            table[row][column] = find_cnf(combine_result, cnf)

            st.table(DataFrame(table, columns=input_string))

            row = (row + 1) if row + 1 < len(table) else 1
            return row
        
    row = (row + 1) if row + 1 < len(table) else 1
    return row


def make_combination(list_input):
    count = len(list_input) // 2

    combination = []

    for i in range(count):
        list1 = list_input[i]
        list2 = list_input[i + count]

        combination.append([])

        for element1 in list1:
            for element2 in list2:
                combination[i].append(tuple((element1, element2)))
    
    return combination

def combine(raw_combination):
    result_set = set()

    for x in raw_combination:
        for y in x:
            result_set.add(y)

    return result_set

def find_cnf(combine, cnf):
    cnf_return = set()

    for com in combine:
        for row in cnf:
            if com in row[1]:
                print(row[0], com)
                cnf_return.add(row[0])
    
    if cnf_return == set():
        return empty
    else:
        return cnf_return