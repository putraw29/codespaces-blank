import streamlit as st
import numpy as np

# Fungsi untuk menyelesaikan soal matematika
def solve_math_problem(problem):
    try:
        result = eval(problem)
        return result
    except:
        return "Error: Masukkan soal matematika yang valid"

# Fungsi utama untuk tampilan chatbot
def chatbot():
    st.title("Chatbot Matematika")
    st.write("Selamat datang! Saya adalah Chatbot Matematika yang siap membantu Anda.")
    
    # Loop chatbot
    while True:
        user_input = st.text_input("Tulis soal matematika Anda di sini:")
        
        if user_input:
            response = solve_math_problem(user_input)
            st.write("Hasil:", response)
        
        if st.button("Keluar"):
            break

# Menjalankan chatbot
chatbot()
