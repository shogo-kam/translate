import streamlit as st
import streamlit_tags as st_tags_sidebar
import streamlit_tags as st_tags

keywords = st_tags(
    label='# Enter Keywords:',
    text='Press enter to add more',
    value=['Zero', 'One', 'Two'],
    suggestions=['five', 'six', 'seven', 
                'eight', 'nine', 'three', 
                'eleven', 'ten', 'four'],
    maxtags = 4,
    key='1')

keyword = st_tags_sidebar(
    label='# Enter Keywords:',
    text='Press enter to add more',
    value=['Zero', 'One', 'Two'],
    suggestions=['five', 'six', 'seven', 
                'eight', 'nine', 'three', 
                'eleven', 'ten', 'four'],
    maxtags = 4,
    key='2')