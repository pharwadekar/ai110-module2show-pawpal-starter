import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan")
    st.session_state.owner.add_pet(Pet("Mochi", "dog"))

st.subheader("Quick Demo Inputs")
owner_name = st.text_input("Owner name", value=st.session_state.owner.name)
if owner_name != st.session_state.owner.name:
    st.session_state.owner.name = owner_name

st.markdown("### Pets")
if st.session_state.owner.pets:
    for p in st.session_state.owner.pets:
        st.write(f"- {p.name} ({p.species})")

with st.expander("Add a new pet"):
    new_pet_name = st.text_input("New Pet name")
    new_species = st.selectbox("New Species", ["dog", "cat", "other"])
    if st.button("Add Pet"):
        if new_pet_name:
            st.session_state.owner.add_pet(Pet(new_pet_name, new_species))
            st.rerun()

st.markdown("### Tasks")

if st.session_state.owner.pets:
    col1, col2, col3 = st.columns(3)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
    with col2:
        time = st.time_input("Time")
    with col3:
        pet_choice = st.selectbox("For Pet", [p.name for p in st.session_state.owner.pets])

    if st.button("Add task"):
        task = Task(task_title, time.strftime("%H:%M"))
        for p in st.session_state.owner.pets:
            if p.name == pet_choice:
                p.add_task(task)
        st.rerun()

st.divider()

st.subheader("Build Schedule")

if st.button("Generate schedule"):
    scheduler = Scheduler(st.session_state.owner)
    tasks = scheduler.sort_by_time(st.session_state.owner.get_all_tasks())
    
    if tasks:
        st.success("Schedule Generated!")
        schedule_data = [{"Time": t.time, "Pet": p_name, "Task": t.description, "Status": "Done" if t.completed else "Pending"} for p_name, t in tasks]
        st.table(schedule_data)
        
        conflicts = scheduler.detect_conflicts()
        if conflicts:
            st.warning(f"Conflicts detected at: {', '.join(conflicts)}")
            
    else:
        st.info("No tasks scheduled.")
