# import necessary library and framework
import streamlit as st

# import the triangular table process
from controller.cyk_algorithm.triangular_table import *
from view.table import print_table

# parse the sentence with cyk algorithm
def parse(cnf, list_of_string):
    # prepare the table filling
    table = create_table(list_of_string)
    # display it to web
    st.write(print_table(table, list_of_string), unsafe_allow_html=True)

    # fill the first iteration (botom row in filling table)
    filling_botton(table, cnf, list_of_string)
    # display it to web
    st.write(print_table(table, list_of_string), unsafe_allow_html=True)

    # fill all the filling table and show the acceptance status
    filling_all(cnf, table, list_of_string)