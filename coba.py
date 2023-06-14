import streamlit as st

# Menyimpan pesan dari pengguna
pesan_pengguna = []

def main():
    # Judul aplikasi
    st.title("Aplikasi Chat Sederhana")

    # Loop untuk mengirim dan menerima pesan
    while True:
        # Tampilan daftar pesan
        with st.expander("Daftar Pesan"):
            for pesan in pesan_pengguna:
                st.write(pesan)

        # Input pesan pengguna
        pesan = st.text_input("Pesan:", "")

        # Tombol Kirim
        if st.button("Kirim"):
            if pesan:
                pesan_pengguna.append("Anda: " + pesan)
                st.text_input("")

        # Tombol Hapus
        if st.button("Hapus Pesan"):
            pesan_pengguna.clear()

        # Tombol Keluar
        if st.button("Keluar"):
            break

if __name__ == "__main__":
    main()
