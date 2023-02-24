import streamlit as st

def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def volume_kubus(sisi):
    return sisi ** 3

def volume_tabung(jari_jari, tinggi):
    return 22/7 * jari_jari ** 2 * tinggi

def volume_bola(jari_jari):
    return (4/3) * 22/7 * jari_jari ** 3

def volume_kerucut(jari_jari, tinggi):
    return (1/3) * 22/7 * jari_jari ** 2 * tinggi 

pil = int(st.number_input("Masukkan pilihan bangun ruang (1 = Balok, 2 = Kubus, 3 = Tabung, 4 = Bola): "))
if pil == 1:
    p = int(st.number_input("Masukkan panjang balok: "))
    l = int(st.number_input("Masukkan lebar balok: "))
    t = int(st.number_input("Masukkan tinggi balok: "))
    st.write("Volume balok adalah: ", volume_balok(p, l, t))
elif pil == 2:
    s = int(st.number_input("Masukkan sisi kubus: "))
    st.write("Volume kubus adalah: ", volume_kubus(s))
elif pil == 3:
    r = int(st.number_input("Masukkan jari-jari tabung: "))
    t = int(st.number_input("Masukkan tinggi tabung: "))
    st.write("Volume tabung adalah: ", volume_tabung(r, t))
elif pil == 4:
    r = int(st.number_input("Masukkan jari-jari bola: "))
    st.write("Volume bola adalah: ", volume_bola(r))
elif pil == 5:
    r = int(st.number_input("masukkan jari-jari alas kerucut: "))
    t = int(st.number_input("Masukkan tinggi kerucut: "))
else:
    st.write("Pilihan tidak valid!")

