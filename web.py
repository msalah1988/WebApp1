import streamlit as st
from streamlit import session_state

from modules import functions as func
######################################
###Sequance of the objects in the code represent the same
###sequance in the Web App interface
######################################
filepath = "todos.txt"
todos = func.update_todos(txt_file=filepath,
                          mode='r',
                          todos_p='')

def add_todo_web():
    new_todo = st.session_state["new_todo"]  + '\n' ###Reading the current to-do from the runtime
    todos.append(new_todo)
    func.update_todos(txt_file=filepath,
                      mode='w',
                      todos_p=todos)
    st.session_state["new_todo"] = '' ###Clear Input Field After submission

st.title('My Tasklist')
st.text('Todos App to improve your productivity')
st.subheader('Current to do(s):')

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,
                         key=todo)
    if checkbox:
        todos.pop(index)
        func.update_todos(txt_file=filepath,
                          mode='w',
                          todos_p=todos)
        del session_state[todo]
        st.rerun()


st.text_input(label='Enter a To Do:',
              placeholder='Add a to do ...',
              key='new_todo',
              on_change=add_todo_web)
