import streamlit as st
import qrcode
import qrcode.image.svg

st.write("# Geração de QRcode")
link = st.text_input("### Digite o **link do QRcode** abaixo e aperte enter:", "seu link aqui")
# st.image('testefundobranco.svg', caption='qrcode')
# https://front.petz.com.br/checkin-customer?subsidiary=04%200030

def generateQRcode(link):
    img = qrcode.make(link, image_factory= qrcode.image.svg.SvgPathFillImage)
    img.save("testefundobranco.svg")


if st.button('Gerar QRcode'):
    generateQRcode(link)
    st.image('testefundobranco.svg', caption=f'qrcode para {link}')
    with open("testefundobranco.svg", "rb") as file:
        btn = st.download_button(
                label="Baixar QRcode como SVG",
                data=file,
                file_name="flower.svg",
                mime="image/svg"
            )
