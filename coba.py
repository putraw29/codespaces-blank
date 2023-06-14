import streamlit as st

def main():
    # Judul aplikasi
    st.title("Aplikasi Chat Sederhana")

    # Mendapatkan input teks dari pengguna
    pesan = st.text_input("Pesan:", "")

    # Menampilkan pesan pengguna
    if st.button("Kirim"):
        st.write("Anda: " + pesan)

    # Menampilkan balasan dari lawan chat
    st.write("Lawan Chat: ...")

if __name__ == "__main__":
    main()
