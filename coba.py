import streamlit as st

# Menyimpan pesan dari pengguna
pesan_pengguna = []

def main():
    # Judul aplikasi
    st.title("Aplikasi Chat Sederhana")

    # Tampilan daftar pesan
    with st.beta_expander("Daftar Pesan"):
        for pesan in pesan_pengguna:
            st.write("Anda: " + pesan)

    # Input pesan pengguna
    pesan = st.text_input("Pesan:", "")

    # Tombol Kirim
    if st.button("Kirim"):
        if pesan:
            pesan_pengguna.append(pesan)
            st.text_input("")

if __name__ == "__main__":
    main()
