#import tkinter
#tasks = []

#def add_task(task):
#    return tasks.append(task)


#def main():
#    print("1 - lisada ülesande \n 2 - kustutada ülesande \n 3 - ulesanded")
#    userInput = input("Mida sa tahad?")
#    if userInput == '1':
#        tasks = add_task(input("Sisesta ülesande: "))
#    elif userInput == '2':
#        pass
#    elif userInput == '3':
#        pass
#    else:
#        print("Sa sisestasid midagi vale")

import streamlit as st

if "tasks" not in st.session_state:
    st.session_state.tasks = []
st.title("Todo list")

#main()