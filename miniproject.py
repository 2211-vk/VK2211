import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('score.csv', index_col=None)
df.fillna(0, inplace=True)
df.isnull().sum()
df['P3'] = sum([df['P3-1'], df['P3-2'], df['P3-3'], df['P3-4']])
df['Total'] = sum([df['P1'], df['P2'], df['P3']])
df['Class-Group'] = ["Không Chuyên" if df['Class'][i][2] != 'C' else "Chuyên Tin" if df['Class'][i][3:] == 'TIN' else "Chuyên Sinh" if df['Class'][i][3:] == 'SI' else "Chuyên Toán" if df['Class'][i][3] == 'T' else "Chuyên Lý/Hoá" if df['Class'][i][3] in ['L', 'H'] else "Chuyên Anh" if df['Class'][i][3] == 'A' else 'Không Chuyên' for i in range(len(df))]
df = pd.DataFrame(df)

st.header('Bảng điểm thi giữa kì lớp MC4AI')
c1, c2, c3 = st.columns(3)
with c1:
    st.text('Khối chuyên')
    tt = st.checkbox('Toán - Tin', value = True)
    lhs = st.checkbox('Lý - Hóa - Sinh', value = True)
    va = st.checkbox('Văn - Anh', value = True)
    k = st.checkbox('Khác', value = True)
    cr = np.array(['Toán', 'Tin', 'Hoá', 'Sinh', 'Văn', 'Anh', 'Chuyên'])
with c2:
    kl = st.radio("Khối lớp", ["Tất cả", "Lớp 10", "Lớp 11", "Lớp 12"])
    match kl:
        case 'Tất cả': a = '0'
        case 'Lớp 10': a = ('11', '12')
        case 'Lớp 11': a = ('10','12')
        case 'Lớp 12': a = ('10','11') 
with c3:
    w = st.selectbox('Giờ học', ('Tất cả','Sáng', 'Chiều'))
    match w:
        case 'Tất cả': i = 'None'
        case 'Sáng': i = 'A'
        case 'Chiều': i = 'M'
co1,co2 = st.columns(2)
with co1:
    st.dataframe(df[(df['Class-Group'].str.endswith(tuple([i for i in cr[[tt,tt,lhs,lhs,va,va,k]]]))) & ~(df['Class'].str.startswith(a)) & ~(df['MC-Class'] == i)])
with co2:
    fig = px.bar(df[(df['Class-Group'].str.endswith(tuple([i for i in cr[[tt,tt,lhs,lhs,va,va,k]]]))) & ~(df['Class'].str.startswith(a)) & ~(df['MC-Class'] == i)], x = 'Gender', y = 'Total', color = 'MC-Class', barmode = 'group')
    st.plotly_chart(fig)