#import libraries
import streamlit as st
import pandas as pd


st.set_page_config(page_title="AI Voice Assistant", page_icon='🎙️', layout="wide")
st.title("Voice Assistant App")
st.subheader("Hands On  Python Workshop")
st.write('''The AI voice assistant is created as " part of the Hands 
on python workshop 2021-2022" for high-school students in U.A.E  to train on python language starting from basics to advanced topics which is 
used to develop The chatbot''')

st.subheader("Objectives")
st.markdown("""
1. Understand python basics.
2. Learn to write and test Python 3 code.
3. Dive into more advanced topics of python 3.
4. Build voice recognition application using the integrated knowledge 
""")

st.subheader("Requirements")
st.markdown("""
1. Internet Connection
2 .Min Windows version : 10
3. Min python version : 3.7.12
4. Visual Studio Code
""")


st.subheader("Benefits")
st.markdown("""
Get Certified by Artificial Intelligence Research Center (AIRC-AU)
""")


st.subheader("Workshop Description")
st.markdown("""
Python is a language with a simple syntax and a powerful set of libraries and opens up the path to establishing machine learning and data analytics careers. As an aspiring python programmer, it provides several job opportunities and promises high growth with huge salary prospects in big companies such as Facebook, Amazon, Netflix, Google, and NASA.

This workshop aims to teach python language to students without prior programming experience in just 2 weeks and deliver the basic programming principles such as operations, control structures, data types, etc. Also, it covers advanced topics in python such as dictionaries and list manipulation, creating and calling functions, and file manipulation. Our workshop includes practice and debugging sessions to enrich the students' knowledge, and grasp of python and enhance their problem-solving skills. Finally, applying the knowledge of the course content in an innovative voice assistant  application and in-class competition. 

At the end of this workshop, students will have a comprehensive understanding of python and implement practical and innovative speech assistant project.
""")

st.subheader("Workshop Agenda")
data = {"Time":["10 min","30 min", "10 min", "20 min","30 min", "30 min","30 min","50 min","20 min","30 min","50 min","30 min","20 min","6 hours"],
        "Topic":["Workshop Overview", "Project Demo", "Introduction to Python", "Starting with Python Editor", "Comment and Print", "Variables and Simple data types", "String Manipulation", "Data Types and String Manipulation tutorial", "If Statement", "Loops","Conditional Statement and iterative loops tutorial", "Functions", "Exception Handling","Final Python Project: Voice Assistant App" ],
        "Instructor":["Dr.Sharif Makhadmeh", "Eng. Lamees Dalbah","Eng. Lamees Dalbah", "Eng. Shaimaa Kouka","Eng. Lamees Dalbah","Eng. Shaimaa Kouka","Eng. Shaimaa Kouka" ,"Eng. Shaimaa Kouka","Eng. Lamees Dalbah","Eng. Lamees Dalbah","Eng. Lamees Dalbah","Eng. Shaimaa Kouka","Eng. Shaimaa Kouka","Eng. Shaimaa Kouka"  ]}
df = pd.DataFrame(data)
st.table(df)

#14 row

#sidebar
#st.sidebar.success("select one of the above")
# with st.sidebar:
#     st.header("AI Voice Assistant")
#     st.subheader("User Manual")
#     st.subheader("Test the Product")
#     st.subheader("About")
#     st.subheader("Contact")
#     st.subheader("Location")
#     #st.write("done")



