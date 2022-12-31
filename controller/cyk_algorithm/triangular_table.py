# import the necessary library and framework
import streamlit as st
from view.table import print_table

# empty set symbol
empty = '\u2205'

# prepare the table for cyk algorithm
def create_table(list_of_string):
    # prepare empty list
    table = []
    # for each word in sentence
    for i in range(len(list_of_string)):
        # append empty list as row
        table.append([])
        # for each word in sentence
        for j in range(len(list_of_string)):
            # if i < j append current row with ' ' as column
            if i < j:
                table[i].append(' ')
            # else append current row with empty set as column
            else:
                table[i].append(set())
    
    # return the empty table
    return table


# fill the first iteration
def filling_botton(table, cnf, list_of_string):
    # for every word in list
    for i, word in enumerate(list_of_string):
        # prepar empty set for table cell
        cell = set()
        # for each rule in cnf
        for row in cnf:
            # for each element in rule's body
            for element in row[1]:
                # if current word is equal with current element
                if word.lower() in (x.lower() for x in element):
                    # add it to cell set
                    cell.add(row[0])
                    # break the 
                    break
        
        # fill the diagonal ([i][i]) table with cell set
        table[i][i] = cell


# fill all the filling table, starting from row 1
def filling_all(cnf, table, string, row = 1):
    # if first column in last row is not an empty set [set()]
    if table[len(table) - 1][0] != set():
        # if the start symbol in there
        if 'X' in table[len(table) - 1][0]:
            # show sign that the sentence accepted
            st.success('Sentence accepted.')
            st.balloons()
        else:
            # else show the sign the the sentece not accpted
            st.error('Sentence not accepted.')
            st.snow()
        
        # stop the recursive
        return

    # find the next row to filled with iteration function
    next_row = iteration(cnf, table, string, row)

    # call the filling_all function with updated next_row
    filling_all(cnf, table, string, next_row)


# iteration to fill table's cell
def iteration(cnf, table, input_string, row):
    # descending iteration for columns in current row
    for column in range(len(table) - 1, -1, -1):
        # if the current cell is empty set
        if table[row][column] == set():
            
            # prepare empty list to store the intersection
            list_of_intersect = []
            # iterate row in current cell from row 0
            for i in range(0, row):
                # if the cell in [i][column] is empty set symbol
                if table[i][column] == empty:
                    # append empty set into list_of_intersect
                    list_of_intersect.append(set())
                # else if the cell in [i][column] is not ' ' and not empty set
                elif table[i][column] != ' ' and table[i][column] != set():
                    # append the cell content into list_of_intersect
                    list_of_intersect.append(table[i][column])

            # iterate the column in current cell from current column + 1
            for i in range(column + 1, len(table)):
                # if the cell in [row][i] is empty set symbol
                if table[row][i] == empty:
                    # append empty set into list_of_intersect
                    list_of_intersect.append(set())
                # else if the cell in [row][i] is not ' ' and not empty set
                elif table[row][i] != ' ' and table[row][i] != set():
                    # append the cell content into list_of_intersect
                    list_of_intersect.append(table[row][i])

            # print(list_of_intersect)
            # make combination of the list_of_intersect and store the combination
            result_list = make_combination(list_of_intersect)
            # print(result_list)
            # print()

            # combine all the combination in result_list into a set
            combine_result = combine(result_list)
            # print(combine_result)
            # print()
            
            # find the right cnf rules for the current table's cell
            table[row][column] = find_cnf(combine_result, cnf)
            # print(table[row][column])
            # print("=====================================================================\n")

            # display the updated filling table
            st.write(print_table(table, input_string), unsafe_allow_html=True)

            # increase the row if the next number of row < than total of all row, else back to row number 1
            row = (row + 1) if row + 1 < len(table) else 1
            # return the value of row
            return row

    # increase the row if the next number of row < than total of all row, else back to row number 1
    row = (row + 1) if row + 1 < len(table) else 1
    # return the value of row
    return row


# make the combination of body in current row and column
def make_combination(list_input):
    # count all the element in list_input, than divide by 2
    count = len(list_input) // 2

    # empty list for all the combination
    combination = []

    # iteration as many as count
    for i in range(count):
        # list1 is the i index of list_input
        list1 = list_input[i]
        # list2 is the i + count index of list_input
        list2 = list_input[i + count]

        # append the empty list into combination
        combination.append([])

        # iterate all element in list1
        for element1 in list1:
            # iterate all element in list2
            for element2 in list2:
                # the combination is the tuple of current element1 and current element2, then append it
                combination[i].append(tuple((element1, element2)))
    
    # return the combination
    return combination


# combine all combination to a set
def combine(raw_combination):
    # prepare the empty set
    result_set = set()

    # for each combination in raw_combination
    for x in raw_combination:
        # for each tuple in combination
        for y in x:
            # add the combination into result_set set
            result_set.add(y)

    # return the result_set
    return result_set

# find the right cnf's head to fill the current cell
def find_cnf(combine, cnf):
    # prepare the empty set
    cnf_return = set()

    # iterate all combination
    for com in combine:
        # iterate each rule in cnf
        for row in cnf:
            # if the combination in body of the current rule
            if com in row[1]:
                # add the head of current rule into cnf_return set
                cnf_return.add(row[0])
    
    # if cnf_return is empty set
    if cnf_return == set():
        # return the empty set symbol
        return empty
    else:
        # else return the value of cnf_return
        return cnf_return