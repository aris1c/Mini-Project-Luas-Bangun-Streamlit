import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar for navigation
with st.sidebar :
    selected = option_menu(
        menu_title="Hitung Luas Bangun",
        options=["Hitung Luas Persegi Panjang","Hitung Luas Segitiga", "Tentang Aplikasi"],
        icons=["calculator","calculator","info-circle"],
        menu_icon="cast",
        default_index=0,
    )


#Untuk Halaman hitung luas persegi Panjang
if (selected=='Hitung Luas Persegi Panjang') :
    st.title('Hitung Luas Persegi Panjang')

    panjang = st.number_input('Masukkan panjang (cm):', min_value=0.0, format="%.2f")
    lebar = st.number_input('Masukkan lebar (cm):', min_value=0.0, format="%.2f")

    if st.button('Hitung'):
        luas = panjang * lebar
        st.success(f'Luas persegi panjang adalah {luas:.2f} cm²')

#Untuk Halaman Hitung Luas Segitiga
if (selected=='Hitung Luas Segitiga') :
    st.title('Hitung Luas Segitiga')

    alas = st.slider('Masukkan alas (cm):', min_value=0.0,max_value=100.0, format="%.2f")
    tinggi = st.slider('Masukkan tinggi (cm):', min_value=0.0,max_value=100.0, format="%.2f")

    if st.button('Hitung'):
        luas = 0.5 * alas * tinggi
        st.success(f'Luas segitiga adalah {luas:.2f} cm²')

#Tentang Aplikasi
if (selected=='Tentang Aplikasi') :
    st.title('Tentang Aplikasi')
    st.write('Aplikasi ini digunakan untuk menghitung luas bangun datar seperti persegi panjang dan segitiga.')
    st.write('Pilih jenis bangun datar yang ingin Anda hitung luasnya dari menu di sebelah kiri.')


# Footer di semua halaman
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background: transparent;
        color: white;
        text-align: center;
        padding: 10px 0;
        z-index: 100;
    }
    </style>
    <div class="footer">
        Powered By Aris Candra
    </div>
    """,
    unsafe_allow_html=True
)    