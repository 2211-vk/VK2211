import streamlit as st
c1,c2 = st.columns([2,3])
with c1:
    st.header('Tra Sua CoTAI')
    st.image('https://i.imgur.com/lEpdPsT.jpeg')
with c2:
    Gia = st.radio('Kich co', ('Nho(30K)', 'Vua(40K)', 'Lon(50K)'), horizontal = True)
    Gia1 = int(Gia[len(Gia)-4:len(Gia)-2])
    st.write('Them')
    co1,co2 = st.columns(2)
    c1,c2,c3,c4 = 0,0,0,0
    with co1:
        them = 0
        ten = ''
        if st.checkbox('Sua(5K)'):
            them += 5
            ten += ' ' + 'Sua'
        if st.checkbox('Ca phe(8K)'):
            them += 8
            ten +=  ' ' + 'Ca phe'
    with co2:
        if st.checkbox('Kem(10K)'):
            them += 10
            ten += ' ' + 'Kem'
        if st.checkbox('Trung(15K)'):
            them += 15
            ten += ' ' + 'Trung'
cl1,cl2 = st.columns(2)
with cl1:
    t = st.multiselect('Topping', ['Trân châu trắng (5K)', 'Trân châu đen (5K)', 'Thạch rau câu (6K)', 'Vải (7K)', 'Nhãn (8K)', 'Đào (10K)'])
    c = 0
    o = ''
    for u in ['Trân châu trắng (5K)', 'Trân châu đen (5K)', 'Thạch rau câu (6K)', 'Vải (7K)', 'Nhãn (8K)', 'Đào (10K)']:
        if u in t and u == 'Đào (10K)':
            c += 10
        elif u in t:
            c += int(u[len(u)-3:len(u)-2])
    for i in t:
        o+=i + ' '

with cl2:
    a = st.number_input('So luong', min_value = 1, step = 1)
x = st.text_area('Ghi chu')
if st.button('Dat hang', use_container_width= True):
    tien = (Gia1 + them + c)*a
    st.success(f'''
               Co {Gia[:len(Gia)-5]}\n
them : {ten}

Topping: {o}

{x}

So luong: {a}

Thanh tien: {tien}''')
