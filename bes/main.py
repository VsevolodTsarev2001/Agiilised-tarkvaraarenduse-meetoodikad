import streamlit as st 

st.session_state.tasks = []

st.title("Todo List")
def add_task():
    task = st.text_input("Sisesta uus ülesanne", key = "new_task_input")
    if st.button("Lisa"):
        if task.strip():
            st.session_state.tasks.append({"text":task, "done":False})
            st.rerun()
        else:
            st.warning("Please enter a task!")
add_task()

st.subheader("Ülesanne nimikiri")
def show_tasks():
    if not st.session_state.tasks:
        st.info("Ei ole ülesanded")
        return
    
    for index,task in enumerate(st.session_state.tasks):
        cols = st.columns([0.05,0,90,0.05])
        with cols[0]:
            task["done"] = st.checkbox("",value=task["done"],key=f"done_{index}")
        with cols[1]:
            text = task ["text"]
            st.markdown(text)
        with cols[2]:
            if st.button("Kustuta", key=f"delete{index}"):
                st.session_state.tasks.pop(index)
                st.rerun()
show_tasks()