import streamlit as st

import math

import time

import numpy as np

import matplotlib.pyplot as plt

def luas_permukaan_kubus(sisi):
    return 6 * sisi ** 2

def volume_kubus(sisi):
    return sisi ** 3

def luas_permukaan_balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar)+(panjang * tinggi)+(lebar * tinggi)

def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def luas_permukaan_tabung(jari_jari, tinggi):
    return (2 * 22/7 * jari_jari ** 2)+(22/7 * jari_jari * 2 * tinggi)

def volume_tabung(jari_jari, tinggi):
    return 22/7 * jari_jari ** 2 * tinggi

def luas_permukaan_bola(jari_jari):
    return 4 * 22/7 * jari_jari ** 2

def volume_bola(jari_jari):
    return 4/3 * 22/7 * jari_jari ** 3 

def luas_permukaan_kerucut(jari_jari, garis_pelukis):
    return (22/7 * jari_jari ** 2)+(22/7 * jari_jari * garis_pelukis)

def volume_kerucut(jari_jari, tinggi):
    return 1/3 * 22/7 * jari_jari ** 2 * tinggi

tab1, tab2, tab3, tab4 = st.tabs(["Bangun ruang", "Akar pangkat", "Pythagoras", "Fungsi kuadrat"])

tab1.title("Geometer apps")

tab1.subheader("pilihlah bangun ruang dibawah ini")

M = tab1.selectbox("pilih salah satu", ["pilih...","kubus", "balok", "tabung", "bola", "kerucut"])

if M == "kubus":
    s = (tab1.number_input("Masukkan sisi kubus: "))
    L = "luas permukaan kubus adalah: ", luas_permukaan_kubus(s)
    V = "volume kubus adalah: ", volume_kubus(s)

elif M == "balok":
    p = (tab1.number_input("masukkan panjang balok: "))
    l = (tab1.number_input("masukkan lebar balok: "))
    t = (tab1.number_input("masukkan tinggi balok: "))
    L = "luas permukaan balok adalah: ", luas_permukaan_balok(p, l, t)
    V = "volume balok adalah: ", volume_balok(p, l, t)

elif M == "tabung":
    r = (tab1.number_input("masukkan jari jari tabung: "))
    t = (tab1.number_input("masukkan tinggi tabung: "))
    L = "luas permukaan tabung adalah: ", luas_permukaan_tabung(r, t)
    V = "volume tabung adalah: ", volume_tabung(r, t)

elif M == "bola":
    r = (tab1.number_input("masukkan jari jari bola: "))
    L = "luas permukaan bola adalah: ", luas_permukaan_bola(r)
    V = "volume bola: ", volume_bola(r)

elif M =="kerucut":
    r = (tab1.number_input("masukkan jari jari kerucut: "))
    p = (tab1.number_input("masukkan tinggi kerucut: "))
    t = math.sqrt(r**2 + p**2)
    L = "Luas permukaan kerucut adalah: ", luas_permukaan_kerucut(r, t)
    V = "volume kerucut adalah: ", volume_kerucut(r, p)

else:
    L = RuntimeError("Masukkan pilihan anda !!!")

K = tab1.button("Cek Hasil")

if K:
    tab1.success(L)
    tab1.success(V)

tab2.title("Power and Root")

A = tab2.radio("PIlih salah satu program", ["Akar 2", "Akar 3", "Pangkat"])

if A == "Akar 2":
    B = tab2.number_input("Masukkan bilangan : ")
    D = B ** (1/2)

elif A == "Akar 3":
    H = tab2.number_input("Masukkan bilangan : ")
    D = H ** (1/3)

elif A == "Pangkat":
    E = tab2.number_input("Masukkan Bilangan : ")
    F = tab2.number_input("Masukkan bilangan pangkat : ")
    D = E ** F

G = tab2.button("Cek hasil")

if G:
    tab2.success(D)

tab3.title("Pythor")

a = tab3.number_input("Masukkan panjang sisi A")
b = tab3.number_input("Masukkan panjang sisi B")
c = (a ** 2 + b ** 2) ** 0.5
d = "Panjang sisi miring (C) adalah:", c

e = tab3.button("Cek sisi miring")

if e:
    tab3.success(d)

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def plot_fungsi_kuadrat(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Grafik Fungsi Kuadrat')
    st.pyplot()

def hitung_akar_kuadrat(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + np.sqrt(discriminant)) / (2*a)
        x2 = (-b - np.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        return None

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def hitung_akar_dan_sumur(x1, x2):
    akar1 = (-x2 + np.sqrt(x2**2 - 4*x1)) / (2*x1)
    akar2 = (-x2 - np.sqrt(x2**2 - 4*x1)) / (2*x1)
    sumbu_simetri = -x2 / (2*x1)
    titik_puncak = x1*(sumbu_simetri**2) + x2*sumbu_simetri

    return akar1, akar2, sumbu_simetri, titik_puncak

# Judul aplikasi
tab4.title("Persamaan dan Fungsi Kuadrat")

# Input koefisien persamaan kuadrat
a = tab4.number_input("Masukkan koefisien a")
b = tab4.number_input("Masukkan koefisien b")
c = tab4.number_input("Masukkan koefisien c")

# Hitung akar-akar, sumbu simetri, dan titik puncak
akar1, akar2, sumbu_simetri, titik_puncak = hitung_akar_dan_sumur(a, b)

# Menampilkan akar-akar
if tab4.button("tampilkan Akar-akar"):
    tab4.write("Akar-akar persamaan kuadrat:")
    tab4.write(f"Akar 1: {akar1}")
    tab4.write(f"Akar 2: {akar2}")

# Menampilkan sumbu simetri
if tab4.button("Tampilkan sumbu simetri"):
    tab4.write("Sumbu simetri:")
    tab4.write(f"x = {sumbu_simetri}")

# Menampilkan titik puncak
if tab4.button("Tampilkan titik puncak"):
    tab4.write("Titik puncak:")
    tab4.write(f"({sumbu_simetri}, {titik_puncak})")

# Menghasilkan data untuk grafik dan grafik
if tab4.button("Tampilkan grafik dan data"):
    x = np.linspace(-10, 10, 100)
    y = a*(x**2) + b*x + c
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.axvline(x=sumbu_simetri, color='r', linestyle='--', label='Sumbu Simetri')
    ax.plot(sumbu_simetri, titik_puncak, marker='o', color='g', label='Titik Puncak')
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    tab4.pyplot(fig)
