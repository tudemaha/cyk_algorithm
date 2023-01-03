import streamlit as st
from PIL import Image

from controller.open_file import open_file
from controller.raw_conversion import raw_to_cfg
from controller.cyk_algorithm.cyk_parse import parse

def cfg_to_cnf():
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

    # web title
    st.write(f"<h1 style='text-align:center; '>{title}</h1>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(['Syntactic Parsing', 'CFG to CNF Conversion'])

    raw = open_file('model/cnf.txt')
    cnf = raw_to_cfg(raw)

    with tab1:
        colb1, colb2 = st.columns(2, gap='medium')

        with colb1:
            # the input sentence text field
            string_input = st.text_input('Input Sentence')
            # convert sentence into list
            list_string = string_input.split(' ')
            # check button
            button_click = st.button('Check', type='primary')

        with colb2:
            tab3, tab4, tab5 = st.tabs(['Table Filling', 'Parsing Tree', 'Left/Right Most Derivation'])

            with tab3:
                # action if button clicked
                if button_click:
                # show error when no string or just one string entered
                    if len(list_string) <= 1:
                        st.error("Sentence can't be null or a word.")
                    # else, process the filing table
                    elif string_input != '':
                        parse(cnf, string_input.split(' '))
            
            with tab4:
                image = Image.open('mockups/parsing_tree.png')
                st.image(image, use_column_width=True, caption=f'Parsing tree of sentence \"{string_input}\"')
            
            with tab5:
                st.write('#### Left Most Derivation:')
                st.write("""
                <p style="font-family: monospace;">
                X <br>
                ⇒ K Ket<br>
                ⇒ S P Ket<br>
                ⇒ ayah P Ket<br>
                ⇒ ayah Adv9 VP Ket<br>
                ⇒ ayah sedang VP Ket <br>
                ⇒ ayah sedang bekerja Ket <br>
                ⇒ ayah sedang bekerja Prep NP <br>
                ⇒ ayah sedang bekerja di NP <br>
                ⇒ ayah sedang bekerja di kebun
                </p>
                """, unsafe_allow_html=True)

                st.write('#### Right Most Derivation:')
                st.write("""
                <p style="font-family: monospace;">
                X <br>
                ⇒ K Ket<br>
                ⇒ K Prep NP <br>
                ⇒ K Prep kebun <br>
                ⇒ K di kebun <br>
                ⇒ S P di kebun <br>
                ⇒ S Adv9 VP di kebun <br>
                ⇒ S Adv9 bekerja di kebun <br>
                ⇒ S sedang bekerja di kebun <br>
                ⇒ ayah sedang bekerja di kebun
                </p>
                """, unsafe_allow_html=True)


    with tab2:
        cola1, cola2 = st.columns(2, gap='medium')

        with cola1:
            rules  = st.text_area('CFG Rules', value='', height=450)
            convert_button = st.button('Convert!', type='primary')

        with cola2:
            st.write('#### CNF Rules')
            st.write(raw)