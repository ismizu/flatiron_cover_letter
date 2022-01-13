import streamlit as st
from time import sleep

#Set initial app layout
st.set_page_config(layout = 'wide', initial_sidebar_state = 'expanded')

#----- Set max width -----#
st.markdown(
        """
<style>
    .reportview-container .main .block-container{
        max-width: 1440px;
    }
</style>
""",
        unsafe_allow_html=True,
    )

#Instantiate Sidebar
intro_sidebar = st.sidebar

#Contact Information
intro_sidebar.markdown(body = '<h1 style = "text_align: center;"> Isana Mizuma </h1>', unsafe_allow_html = True)
intro_sidebar.image(image = 'images/profile_picture.png')

intro_sidebar.markdown(
'''
>[LinkedIn](https://www.linkedin.com/in/isana-mizuma/)\n
>[GitHub](https://github.com/ismizu)\n
>[Blog](https://ismizu.medium.com/)\n
>[App Repository](https://github.com/ismizu/flatiron_cover_letter)
''')

#Main Body Text
st.text('January 12, 2020')
st.title('Dear Hiring Manager,')
st.markdown(
'''

'''
)