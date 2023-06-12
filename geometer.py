import streamlit as st

import math

import time

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

tab1, tab2, tab3 = st.tabs(["Bangun ruang", "Akar pangkat", "Pythagoras"])

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

st.caption("Made by Raditya Putra")
