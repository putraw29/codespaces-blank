import streamlit as st
import matplotlib as plt
import numpy as np

def hitung_akar_dan_sumur(x1, x2):
    akar1 = (-x2 + np.sqrt(x2**2 - 4*x1)) / (2*x1)
    akar2 = (-x2 - np.sqrt(x2**2 - 4*x1)) / (2*x1)
    sumbu_simetri = -x2 / (2*x1)
    titik_puncak = x1*(sumbu_simetri**2) + x2*sumbu_simetri

    return akar1, akar2, sumbu_simetri, titik_puncak

# Judul aplikasi
st.title("Persamaan dan Fungsi Kuadrat")

# Input koefisien persamaan kuadrat
a = st.number_input("Masukkan koefisien a")
b = st.number_input("Masukkan koefisien b")
c = st.number_input("Masukkan koefisien c")

# Hitung akar-akar, sumbu simetri, dan titik puncak
akar1, akar2, sumbu_simetri, titik_puncak = hitung_akar_dan_sumur(a, b)

# Menampilkan akar-akar
st.write("Akar-akar persamaan kuadrat:")
st.write(f"Akar 1: {akar1}")
st.write(f"Akar 2: {akar2}")

# Menampilkan sumbu simetri
st.write("Sumbu simetri:")
st.write(f"x = {sumbu_simetri}")

# Menampilkan titik puncak
st.write("Titik puncak:")
st.write(f"({sumbu_simetri}, {titik_puncak})")

# Menghasilkan data untuk grafik
x = np.linspace(-10, 10, 100)
y = a*(x**2) + b*x + c

# Menampilkan grafik
fig, ax = plt.subplots()
ax.plot(x, y)
ax.axvline(x=sumbu_simetri, color='r', linestyle='--', label='Sumbu Simetri')
ax.plot(sumbu_simetri, titik_puncak, marker='o', color='g', label='Titik Puncak')
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
st.pyplot(fig)
