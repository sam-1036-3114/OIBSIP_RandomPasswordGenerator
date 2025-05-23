import streamlit as st
from password_utils import generate_password
import pyperclip

st.set_page_config(page_title="🔐 Password Generator", layout="centered")

st.title("🔐 Advanced Password Generator")

st.markdown("Configure your password options below:")

# --- Input Controls ---
length = st.slider("Password Length", min_value=4, max_value=64, value=12)

st.write("**Select character types to include:**")
col1, col2, col3 = st.columns(3)
with col1:
    use_letters = st.checkbox("Letters (A-Z, a-z)", value=True)
with col2:
    use_digits = st.checkbox("Digits (0-9)", value=True)
with col3:
    use_symbols = st.checkbox("Symbols (!@#$...)")

exclude_chars = st.text_input("Exclude specific characters (optional)", placeholder="e.g. O0Il")

# --- Validation & Button ---
if st.button("🔄 Generate Password"):
    if not (use_letters or use_digits or use_symbols):
        st.error("❗ Please select at least one character type.")
    else:
        try:
            password = generate_password(
                length=length,
                use_letters=use_letters,
                use_digits=use_digits,
                use_symbols=use_symbols,
                exclude_chars=exclude_chars
            )
            st.success("✅ Generated Password:")
            st.code(password)

            if st.button("📋 Copy to Clipboard"):
                pyperclip.copy(password)
                st.success("Copied to clipboard!")

        except Exception as e:
            st.error(f"❌ Error: {e}")
