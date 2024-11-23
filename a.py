import streamlit as st
st.header('Bé tập làm toán')
cl1,cl2,cl3 = st.columns(3)
with cl1:
    a = st.number_input('a', 0.00)
with cl2:
    pt = st.radio('Phép toán', options = ['\+', '\-','x',':'],horizontal = True)
with cl3:
    b = st.number_input('b', 0.00)
e = st.number_input('Nhập kết quả', 0.00)
if st.button('Kiểm tra'):
    if pt == '\+':
        i = a + b
    elif pt == '\-':
        i = a-b
    elif pt == 'x':
        i = a*b
    else:
        i = a/b
    if i == e:
        print('Good')
    else:
        print('so bad')