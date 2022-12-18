# import streamlit as front end framework
import streamlit as st

# import necessary functions
from controller.open_file import open_file
from controller.raw_conversion import raw_to_cfg
from controller.cyk_algorithm.cyk_parse import parse

# prepare the web view
def run_streamlit():
    # title for the web
    title = 'Syntactic Parsing of Indonesian Sentences Using CYK Algorithm'

    # setup the web configuration
    st.set_page_config(layout='wide', page_title=title, menu_items={
        'About': f"""
        ### {title}
        Made with :heart: by Group 3 in Class A  
        Language and Automata Theory Subject  
        GitHub: https://github.com/tudemaha/cyk_algorithm
        """
    })
    
    # prepare the cnf rules
    raw_cfg = open_file('model/cnf.txt')
    # convert the raw cnf rules into readable format for Python
    cnf = raw_to_cfg(raw_cfg)

    # web title
    st.write(f"<h1 style='text-align:center; '>{title}</h1>", unsafe_allow_html=True)

    # split web into two columns, left column displays the cnf rule, right column displays the filling table
    col1, col2 = st.columns(2, gap='small')

    # prepre the left column
    with col1:
        st.write("### CNF Rules:")
        st.write(raw_cfg)

    # prepare the right column
    with col2:
        # the input sentence text field
        string_input = st.text_input('Input Sentence')
        # convert sentence into list
        list_string = string_input.split(' ')
        # check button
        button_click = st.button('Check', type='primary')

        # action if button clicked
        if button_click:
            # show error when no string or just one string entered
            if len(list_string) <= 1:
                st.error("Sentence can't be null or a word.")
            # else, process the filing table
            elif string_input != '':
                st.write('<br><p>Filling Table:</p>', unsafe_allow_html=True)
                parse(cnf, string_input.split(' '))