import pandas as pd
from datetime import datetime, date, timedelta
import streamlit as st
import webbrowser
import openpyxl

st.title('HBD HMTM PATRA KOMISARIAT')
st.header ('Ulang Tahun Hari Ini')
#Read data
df=pd.read_csv('HBD.csv')


df=df[['NAMA','PATRA','PJ','Unique Code']]
df=df.applymap(str)

# current dateTime
now = datetime.now()

# convert to string
date_time_str = now+ timedelta(days=0)
date_time_str = date_time_str.strftime('%#m%d.0')
st.write(date_time_str)

df_new=df[df['Unique Code'].str.fullmatch(date_time_str)]
print(df_new)

#Using unique Code
df_new=df[df['Unique Code'].str.fullmatch(date_time_str)]
df_new_=df_new[['NAMA','PATRA','PJ']]

hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
st.table(df_new_)


st.header ('Guide Line HBD')
st.text('1. Buka google calendar dan atau lihat pembagian HBDan di web ini')
st.text('2. Chat Tiara buat booking publikasi minimal J-3 ')
st.text('3. Cek database, didalemnya yang perlu dicek: foto dan divisinya, download fotonya:')
st.write('[Foto Taraksa Mahogra](https://drive.google.com/drive/folders/1k2bz8m01luw88IdfE1ryjpIKdWwnSQyxEkFFgK6TN2_7S_8q-gT1Ko4fNCygnlnLJbCZbLli)')
st.write('[Foto Aquileo](https://drive.google.com/drive/folders/1mhpdPt4jmCbQuUPCLKTCV4637U2lRDdR2W3SJdvt2nIWRRV2y19XdljH1ukbpvKt5AnP4-3s)')
st.write('4. Edit foto pake canva aja biar gampang, [ini linknya](https://canva.com) ')
st.text('    Login pake canva premium biar gampang editnya')
st.text('    Uname: serkainternal@gmail.com')
st.text('    Password: serka2022')
st.write( '5. Terus buat fun factnya, tanya temen deketnya ya. ')
st.write( 'Untuk Temen deketnya bisa dicari disini: [ini linknya](https://canva.com)')
st.text(' Kalau gaada disini bisa chat gw aja atau ketang nya di masing masing angkatan')


