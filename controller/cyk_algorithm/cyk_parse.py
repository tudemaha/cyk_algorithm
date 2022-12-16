import streamlit as st
from pandas import DataFrame

from controller.cyk_algorithm.triangular_table import *

def parse(cnf, list_of_string):
    table = create_table(list_of_string)
    st.table(DataFrame(table, columns=list_of_string))

    filling_botton(table, cnf, list_of_string)
    st.table(DataFrame(table, columns=list_of_string))

    filling_all(cnf, table, list_of_string)