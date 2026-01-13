import streamlit as st

st.set_page_config(page_title="Warframe Cipher", page_icon="🛡️", layout="centered")

st.title("🛡️ Warframe Cipher Generator")
st.write("Enkripsi teks menggunakan Warframe (A–Z) dan Tenet Weapons (0–9)")

# =============================
# DATA CIPHER HURUF
# =============================
letter_cipher = {
    "A": "MP15", "B": "ML18", "C": "MSW21", "D": "MDV24", "E": "FRR15",
    "F": "MIW13", "G": "MTS19", "H": "MC17", "I": "MD16", "J": "FOE24",
    "K": "FO24", "L": "MVR20", "M": "FSG14", "N": "ML16", "O": "FR17",
    "P": "FD20", "Q": "MCP23", "R": "MR18", "S": "MG21", "T": "FS16",
    "U": "MR25", "V": "MTN13", "W": "MD15", "X": "NBXW20", "Y": "FA21",
    "Z": "FA14"
}

# =============================
# DATA CIPHER ANGKA
# =============================
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

# =============================
# INPUT USER
# =============================
plaintext = st.text_input("Masukkan teks (A–Z dan 0–9):", "")

if st.button("🔐 Enkripsi"):
    result = []
    invalid = []

    for ch in plaintext.upper():
        if ch in letter_cipher:
            result.append(letter_cipher[ch])
        elif ch in number_cipher:
            result.append(number_cipher[ch])
        elif ch == " ":
            result.append("/")  # pemisah kata
        else:
            invalid.append(ch)

    st.subheader("Cipher Text:")
    st.code(" ".join(result))

    if invalid:
        st.warning(f"Karakter tidak dikenali: {', '.join(set(invalid))}")

st.markdown("---")
st.caption("Cipher System based on Warframe & Tenet Weapons | Streamlit App")
