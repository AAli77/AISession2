import streamlit as st

st.title("My Streamlit App")

st.write("Welcome to my Streamlit app!")

name=st.text_input("Enter your name:")
st.write(f"Hello, {name}!")

st.button("Click me!")

st.chat_input("Hi enter the prompt here")

st.sidebar.title("Sidebar")

##Basic Calculator using streamlit
st.sidebar.header("Basic Calculator")   

# Page configuration
st.set_page_config(
    page_title="Python Calculator",
    page_icon="🧮",
    layout="centered"
)

# Application title
st.title("🧮 Simple Calculator")

st.write("A calculator built using Python and Streamlit.")

# User input
num1 = st.number_input(
    "Enter First Number",
    value=0.0
)

num2 = st.number_input(
    "Enter Second Number",
    value=0.0
)

# Select operation
operation = st.selectbox(
    "Select Operation",
    ["Addition (+)",
     "Subtraction (-)",
     "Multiplication (*)",
     "Division (/)"]
)

# Calculate button
if st.button("Calculate", type="primary"):

    if operation == "Addition (+)":
        result = num1 + num2

    elif operation == "Subtraction (-)":
        result = num1 - num2

    elif operation == "Multiplication (*)":
        result = num1 * num2

    elif operation == "Division (/)":

        if num2 == 0:
            st.error("Cannot divide by zero!")
            st.stop()

        result = num1 / num2

    # Display result
    st.success(f"Result: {result:,.2f}")
