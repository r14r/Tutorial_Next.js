# solution-image-upload
img_file = st.file_uploader("Bild hochladen", type=["jpg", "png"])
if img_file:
    st.image(img_file)
