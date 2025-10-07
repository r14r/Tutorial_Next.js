files = st.file_uploader("Mehrere FAQs", type="txt", accept_multiple_files=True)
faq_data = ""
if files:
    for f in files:
        faq_data += f.read().decode() + "\n"
