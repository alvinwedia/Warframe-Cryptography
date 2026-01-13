import streamlit as st

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Warframe Cipher",
    page_icon="🧬",
    layout="centered"
)

# =========================
# LOAD CSS
# =========================

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# persistent animated background
st.markdown("<div id='animated-bg'></div>", unsafe_allow_html=True)

# =========================
# CIPHER TABLE (SAMPLE)
# =========================

alpha_map = {
    "A": "MD15", "B": "MP15", "C": "MR18", "D": "MIW13",
    "E": "MR18", "F": "MP15", "G": "MD15", "H": "MIW13",
    "I": "MR18", "J": "MP15", "K": "MD15", "L": "MIW13",
    "M": "MR18", "N": "MP15", "O": "MD15", "P": "MIW13",
    "Q": "MR18", "R": "MP15", "S": "MD15", "T": "MIW13",
    "U": "MR18", "V": "MP15", "W": "MD15", "X": "MIW13",
    "Y": "MR18", "Z": "MP15",
    "0": "TN500", "1": "TN600", "2": "TN700", "3": "TN800",
    "4": "TN900", "5": "TN1000", "6": "TN1100", "7": "TN1200",
    "8": "TN1300", "9": "TN1400"
}

reverse_map = {v: k for k, v in alpha_map.items()}

# =========================
# UI
# =========================

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.title("🧬 Warframe Cipher System")

mode = st.radio(
    "Select Mode",
    ["🔐 Encrypt", "🔓 Decrypt"],
    horizontal=True
)

# =========================
# MODE COLOR CONTROL
# =========================

if mode == "🔐 Encrypt":
    st.markdown("""
    <style>
    :root {
        --c1: #020409;
        --c2: #071a3a;
        --c3: #0b3a6d;
    }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    :root {
        --c1: #020409;
        --c2: #2b0b3f;
        --c3: #5b1a7a;
    }
    </style>
    """, unsafe_allow_html=True)

# =========================
# ENCRYPT
# =========================

if mode == "🔐 Encrypt":

    text = st.text_area(
        "Plain Text (A–Z, 0–9):",
        height=120,
        placeholder="Type your message here..."
    )

    if st.button("Encrypt"):

        clean = "".join(c for c in text.upper() if c.isalnum())

        result = "".join(alpha_map.get(c, "") for c in clean)

        st.markdown("### Cipher Output")
        st.markdown(f"<div class='token-box'>{result}</div>", unsafe_allow_html=True)

# =========================
# DECRYPT
# =========================

else:

    cipher = st.text_area(
        "Cipher Text:",
        height=120,
        placeholder="Enter cipher text here..."
    )

    if st.button("Decrypt"):

        cipher_text = cipher.replace(" ", "").replace("\n", "").strip()

        i = 0
        decoded = ""

        while i < len(cipher_text):
            matched = False
            for code in reverse_map:
                if cipher_text.startswith(code, i):
                    decoded += reverse_map[code]
                    i += len(code)
                    matched = True
                    break
            if not matched:
                i += 1  # skip unknown char

        st.markdown("### Plain Text Output")
        st.markdown(f"<div class='token-box'>{decoded}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
