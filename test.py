import streamlit

streamlit.title("Something")
grades = [i for i in "abcdefg".upper()]

option = streamlit.selectbox("What is your grade little boy?", grades)
streamlit.write(f"Your grade is {option}")


