import streamlit as st
import re

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(
    page_title="Warframe Cipher System",
    page_icon="🛡️",
    layout="centered"
)

# =============================
# LOAD CSS
# =============================
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# =============================
# CIPHER DATA
# =============================

letter_cipher = {
    "A": "MP15", "B": "ML18", "C": "MSW21", "D": "MDV24", "E": "FRR15",
    "F": "MIW13", "G": "MTS19", "H": "MC17", "I": "MD16", "J": "FOE24",
    "K": "FO24", "L": "MVR20", "M": "FSG14", "N": "ML16", "O": "FR17",
    "P": "FD20", "Q": "MCP23", "R": "MR18", "S": "MG21", "T": "FS16",
    "U": "MR25", "V": "MTN13", "W": "MD15", "X": "NBXW20", "Y": "FA21",
    "Z": "FA14"
}

number_cipher = {
    "0": "TAP760",
    "1": "TFR22",
    "2": "TG34",
    "3": "TT60",
    "4": "TC22",
    "5": "TD260",
    "6": "TP70",
    "7": "TE640",
    "8": "TD28",
    "9": "TS120"
}

reverse_letter = {v: k for k, v in letter_cipher.items()}
reverse_number = {v: k for k, v in number_cipher.items()}

all_tokens = list(reverse_letter.keys()) + list(reverse_number.keys())

# sort by length descending (untuk greedy match)
all_tokens.sort(key=len, reverse=True)


# =============================
# HEADER
# =============================

st.markdown("<div class='title'>WARFRAME CIPHER</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Encrypt & Decrypt using Warframe Algorithm</div>", unsafe_allow_html=True)

# =============================
# MAIN CARD
# =============================

st.markdown("<div class='card'>", unsafe_allow_html=True)

mode = st.radio(
    "Select Mode",
    ["🔐 Encrypt", "🔓 Decrypt"],
    horizontal=True
)

# ---------- ENCRYPT ----------
if mode == "🔐 Encrypt":

    text = st.text_area(
        "Plain Text (A–Z, 0–9):",
        height=120,
        placeholder="Enter Plain Text Here..."
    )


    if st.button("Encrypt 🔐"):
        result = []
        invalid = []

        for ch in text.upper():
            if ch in letter_cipher:
                result.append(letter_cipher[ch])
            elif ch in number_cipher:
                result.append(number_cipher[ch])
            elif ch == " ":
                result.append("/")
            else:
                invalid.append(ch)

        st.markdown("### Cipher Output")

        output = "".join(result)   # horizontal, tanpa spasi
        st.markdown(f"<div class='output-box'>{output}</div>", unsafe_allow_html=True)


        if invalid:
            st.warning(f"Unsupported characters: {', '.join(set(invalid))}")

# ---------- DECRYPT ----------
else:

    cipher = st.text_area(
        "Cipher Text:",
        height=120,
        placeholder="Enter Cipher Text Here..."
    )

    if st.button("Decrypt 🔓"):
        cipher_text = cipher.upper()
        cipher_text = re.sub(r"[^A-Z0-9]", "", cipher_text)

        i = 0
        result = []
        invalid = []

        while i < len(cipher_text):
            match_found = False

            for token in all_tokens:
                if cipher_text.startswith(token, i):
                    if token in reverse_letter:
                        result.append(reverse_letter[token])
                    elif token in reverse_number:
                        result.append(reverse_number[token])

                    i += len(token)
                    match_found = True
                    break

            if not match_found:
                invalid.append(cipher_text[i:i+5])
                i += 1


        st.markdown("### Plain Text Output")

        st.markdown(f"<div class='output-box'>{''.join(result)}</div>", unsafe_allow_html=True)

        if invalid:
            st.warning(f"Invalid cipher codes: {', '.join(set(invalid))}")

st.markdown("</div>", unsafe_allow_html=True)

# =============================
# FOOTER
# =============================

st.markdown("<div class='footer'>Warframe Cipher System</div>", unsafe_allow_html=True)
