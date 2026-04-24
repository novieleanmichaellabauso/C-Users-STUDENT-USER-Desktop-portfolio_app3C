import streamlit as st
st.title(" Contact Us")

name = st.text_input("Novie Lean Michaella Bauso")
email = st.text_input("bausomykamikayazarcon@gmail.com")
message = st.text_area("Message")
if st.button("Send"):
if name and email and message:
st.success("Message sent successfully! ✅")
else:
st.error("Please fill all fields.")
st.markdown("### Social Links")
st.write("- GitHub: https://github.com/novieleanmichaellabauso)
st.write("- Facebook: https://www.facebook.com/share/1KPHKbN2od/")