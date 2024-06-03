import streamlit as st
import qrcode
import qrcode.image.svg

st.set_page_config(
    page_title="Gerador de QRcode",
    page_icon="📷",
)

st.write("# Geração de QRcode")
link = st.text_input("### Digite o **link do QRcode** abaixo e aperte enter:", "Seu link aqui")

def generateQRcode(link):
    img = qrcode.make(link, image_factory= qrcode.image.svg.SvgPathFillImage)
    img.save("qrcode-gerado")


if st.button('Gerar QRcode'):
    generateQRcode(link)
    st.image('qrcode-gerado', caption=f'qrcode para {link}')
    with open("qrcode-gerado", "rb") as file:
        btn = st.download_button(
                label="Baixar QRcode como SVG",
                data=file,
                file_name=f"qrcode-{link}.svg",
                mime="image/svg"
            )
