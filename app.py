from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

genai.configure(api_key=os.getenv("api"))

def get_gemini_response(ques,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([prompt[0],ques])
    return response.text

def get_data(sqls,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sqls)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt=[
    """
    You are an expert in converting English questions to SQL query. 
The SQL database has named as STUDENT has student data of a college containg columns as
student name, their department named as branch, their section is mentioned and 
their score acquired as marks. For example, \n Example 1 - How many students are there in total. The SQL 
command will be something like SELECT COUNT(*) FROM STUDENT \n Example 2 Who is the highest scorer of 
the college. The SQL command will be something like this 
SELECT name from STUDENT where score = (Select max(marks) from STUDENT)
Respond with only the raw SQL query. Do not include explanations, markdown, or extra text and punctuation, symbols like ~,'"""
]



##Streamlit App

st.set_page_config(page_title="I give you SQL query")
st.header("Gemini App to retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

if submit:
    response=get_gemini_response(question,prompt)
    print("*******",response)
    data=get_data(response,"student.db")
    st.subheader("The Response is: ")
    for row in data:
        print(row)
        st.header(row)