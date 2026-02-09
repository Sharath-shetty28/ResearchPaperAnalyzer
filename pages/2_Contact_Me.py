import streamlit as st

st.set_page_config(page_title="Contact Me", page_icon="📬")

st.title("📬 Contact Me")
st.write("Have a question, feedback, or just want to say hi? Fill out the form below 👇")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message", height=150)

    submit = st.form_submit_button("Send Message")

if submit:
    if name and email and message:
        st.success("✅ Thanks for reaching out! I’ll get back to you soon.")
        # You can later connect this to email / database
    else:
        st.error("❌ Please fill in all fields.")

st.markdown("---")
st.subheader("📌 Other Ways to Reach Me")

st.markdown("""
- 📧 **Email:** sharathshetty301@gmail.com
- 💼 **LinkedIn:** https://linkedin.com/in/sharath-shetty28
- 🐙 **GitHub:** https://github.com/Sharath-shetty28
""")
