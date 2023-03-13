import math

import time

import streamlit as st

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

st.title("Geometer Apps")

st.subheader("pilihlah bangun ruang dibawah ini")

M = st.selestbox("pilih salah satu", ["kubus", "balok", "tabung", "bola", "kerucut"])

if M == "kubus":
    s = int(st.number_input("Masukkan sisi kubus: "))
    L = "luas permukaan kubus adalah: ", luas_permukaan_kubus(s)
    V = "volume kubus adalah: ", volume_kubus(s)

elif M == "balok":
    p = int(st.number_input("masukkan panjang balok: "))
    l = int(st.number_input("masukkan lebar balok: "))
    t = int(st.number_input("masukkan tinggi balok: "))
    L = "luas permukaan balok adalah: ", luas_permukaan_balok(p, l, t)
    V = "volume balok adalah: ", volume_balok(p, l, t)

elif M == "tabung":
    r = int(st.number_input("masukkan jari jari tabung: "))
    t = int(st.number_input("masukkan tinggi tabung: "))
    L = "luas permukaan tabung adalah: ", luas_permukaan_tabung(r, t)
    V = "volume tabung adalah: ", volume_tabung(r, t)

elif M == "bola":
    r = int(st.number_input("masukkan jari jari bola: "))
    L = "luas permukaan bola adalah: ", luas_permukaan_bola(r)
    V = "volume bola: ", volume_bola(r)

elif M =="kerucut":
    r = int(st.number_input("masukkan jari jari kerucut: "))
    t = int(st.number_input("masukkan panjang garis pelukis kerucut: "))
    p = int(st.number_input("masukkan tinggi kerucut: "))
    L = "Luas permukaan kerucut adalah: ", luas_permukaan_kerucut(r, t)
    V = "volume kerucut adalah: ", volume_kerucut(r, p)

else:
    L = RuntimeError("Masukkan pilihan anda !!!")

K = st.button("Cek Hasil")

if K:
    st.success(L)
    st.success(V)
    st.balloons()

st.caption("Made By Raditya Putra")
