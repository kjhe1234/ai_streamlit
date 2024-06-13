import streamlit as st
from PIL import Image

#사이드바 화면
st.sidebar.title("사이드바")
st.sidebar.header("텍스트 입력")

ueer_id = st.sidebar.text_input("ID입력",value="kjhe1234",max_chars=15)
user_pw = st.sidebar._text_input("PW입력:",value= "12345",type='password')

st.sidebar.header("셀렉트박스")
sel_opt = ['진주 귀걸이를 한 소녀','별이 빛나는 밤','절규','월하정인','고양이','강아지']
user_opt = st.sidebar.selectbox("좋아하는 작품은?",sel_opt)
st.sidebar.write("선택한 작품은:",user_opt)

#매인 화면
st.title("streamlit of sidebar")

if ueer_id == 'kjhe1234':
    image_files=['Vermeer.png','Gogh.png','Munch.png','ShinYoonbok.png','cat.png','dog.png']
    sel_img_index = sel_opt.index(user_opt)
    #선택한 항목에 맞는 이미지 파일 지정
    img_file = image_files[sel_img_index]
    img_local = Image.open(img_file) #PIL 이미지 열기
    st.image(img_local,caption=user_opt)  #이미지 표시
else:
    st.write("ID가 다르면 안보입니다.")

