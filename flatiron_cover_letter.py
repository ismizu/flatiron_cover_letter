import streamlit as st

#Set initial app layout
st.set_page_config(initial_sidebar_state = 'expanded')

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
>[This App's Repository](https://github.com/ismizu/flatiron_cover_letter)
''')

#Main Body Text
st.text('January 19, 2022')
st.title('Dear Hiring Manager,')
st.markdown(
'''
Prior to Flatiron School, I completed a Management Information Systems degree at Rutgers University. \
My initial interest in Data Science was born during this time as I obtained a high-level understanding of \
data analysis and data manipulation. And so, I decided to attend Flatiron School's Data Science Program \
as a means of further elaborating on this understanding.\n

During the time I spent completing my degree I had also been working as an instructor at \
Bergen Community College teaching Logistics and Manufacturing. \
And following my time at Flatiron, I came to realize that while still holding great interest \
in Data Science, I was still deeply enthusiatic about teaching; for this reason, \
I would like to apply as a Coach for Flatiron School's Data Science Program.\n
'''
)

#Create columns to display text aside images
col_text, col_image = st.columns([3, 1.5])

with col_image:
    st.image(
        image = ['images/manufacturing_lab.jpeg', 'images/online_class.png'],
        caption = ['Manufacturing Lab at Bergen Community College', 'Remote Classes during COVID'])

with col_text:
    st.markdown(
    '''
    During my time lecturing, I taught students ranging from late highschool to college students to older adults \
    looking to receive certification. I feel that this range in student age enhanced my ability to \
    communicate ideas in different ways. Particularly in the beginning, I felt like I underwent a crash course \
    (or bootcamp!) in how to state the same thing in ten entirely different ways.\n

    This process, of finding the best way to communicate ideas to another individual was something I found \
    deeply rewarding. When students had the "Aha! moment" and were able to articulate the information \
    back to me, it was just an absolutely wonderful feeling.\n

    Some of my favorite moments have been receiving messages and calls from past students to talk to me about \
    the jobs they received. My most memorable have been my students from a program that taught students \
    with intellectual disabilities. One student received their forklift certification and was able to \
    work as a forklift driver within a logistics facility and another became a manager at UPS!
    ''')

st.markdown(
'''
Overall, I find it greatly gratifying to help other students along the path to their own \
achievements. Post Flatiron, I wrote a few blogposts for a Medium publication, \
[Python in Plain English](https://python.plainenglish.io/) where I gave base explanations \
on [Linear Regression](https://python.plainenglish.io/machine-learning-in-laymans-terms-linear-regression-with-groceries-6a595d1242d), \
[Recommendation Engines](https://python.plainenglish.io/machine-learning-for-beginners-recommendation-engines-with-music-de23905baca2), \
as well as [Streamlit](https://python.plainenglish.io/streamlit-creating-live-applications-with-only-python-629d08084d78). \
I have also been working part-time teaching math at a [teaching center](https://www.mathnasium.com/fortlee) \
over the course of my job search. It is due to this deep interest in teaching that I would like to apply for the \
position of Data Science Coach. \n

Warm Regards, \n
Isana Mizuma
'''
)