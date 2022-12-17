import streamlit as st

from controller.open_file import open_file
from controller.raw_conversion import raw_to_cfg
from controller.cyk_algorithm.cyk_parse import parse

def run_streamlit():
    title = 'Syntactic Parsing of Indonesian Sentences Using CYK Algorithm'

    st.set_page_config(layout='wide', page_title=title, menu_items={
        'About': f"""
        ### {title}
        Made with :heart: by Group 3 in Class A  
        Language and Automata Theory Subject  
        GitHub: https://github.com/tudemaha/cyk_algorithm
        """
    })
    
    raw_cfg = open_file('model/cnf.txt')
    cnf = raw_to_cfg(raw_cfg)

    # st.title(title)
    st.write(f"<h1 style='text-align:center; '>{title}</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap='small')

    with col1:
        st.write("### CNF Rules:")
        st.write(raw_cfg)

    with col2:
        string_input = st.text_input('Input Sentence')
        button_click = st.button('Check', type='primary')
        if button_click and string_input != '':
            st.write('<br><p>Filling Table:</p>', unsafe_allow_html=True)
            parse(cnf, string_input.split(' '))

    


    