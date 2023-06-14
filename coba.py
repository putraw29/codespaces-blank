import streamlit as st

# Membuat daftar pesan
messages = []

# Membuat sidebar dengan input field untuk pengguna
user_input = st.sidebar.text_input("Pesan", "")

# Menambahkan pesan pengguna ke daftar pesan
if st.sidebar.button("Kirim"):
    messages.append(("User", user_input))
    user_input = ""

# Menampilkan pesan
st.title("Aplikasi Chat Streamlit")

# Menampilkan pesan-pesan
for sender, message in messages:
    if sender == "User":
        st.text_input("User", message, key=message)
    else:
        st.text_input("Bot", message, key=message)
