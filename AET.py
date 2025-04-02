import streamlit as st
from Crypto.Cipher import AES
import os

#Function to encrypt the file's data

def EncryptFileData(data, key):
    cipher = AES.new(key, AES.MODE_EAX) # Creating a cypher object in EAX mode
    ciphertext,tag=cipher.encrypt_and_digest(data)
    return cipher.nonce+tag+ciphertext

#Function to decrypt the file's data
def DecryptFileData(encryptedData,key):
    nonce = encryptedData[:16] # First 16 bytes are the nonce
    tag = encryptedData[16:32] # Next 16 bytes are the suthentication tags
    ciphertext = encryptedData[32:] # Rest are the actual encrypted text
    cipher = AES.new(key, AES.MODE_EAX,nonce=nonce) # A new cipher object
    # Decrypt and verify the authentication tag to ensure data integrity
    return cipher.decrypt_and_verify(ciphertext,tag)

# Streamlit UI
st.title("🔏 ADVANCED ENCRYPTION TOOL")
st.write("ENCRYPT AND DECRYPT FILES USING AES-256")

# UI controls for selection of operation mode
mode = st.radio("Choose Mode: ", ["Encrypt","Decrypt"])

# Upload the file to encrypt in .txt,.pdf,.png,.jpg or .bin format
uploadedFile = st.file_uploader("Upload a file", type=["txt","pdf","png","jpeg","bin"])
# Input of the key for encryption and decryption
key= st.text_input("Enter a secret key(Must be of 32 characters): ", type="password")

# Process further if both the file and the key are provided
if uploadedFile and key:
    key = key.ljust(32).encode()[:32] #Ensuring key is exactly 32 bytes
    fileBytes = uploadedFile.read() #To read the file conetnt
# Encryption Mode
    if mode=="Encrypt":
        # Encryption using the key
        encrypted_data = EncryptFileData(fileBytes,key)
        #download the encrypted file
        st.download_button("Download Encrypted File",encrypted_data,file_name="encrypted.bin")
# Decryption Mode        
    elif mode == "Decrypt":
        # Attempt to decrypt the file's data
        try:
            decrypted_data = DecryptFileData(fileBytes,key)
            st.download_button("Download Decrypted File",decrypted_data,file_name="decrypted.txt")
        except ValueError:
            # To handle decryption errors 
            st.error("Decryption failed! Incorrect key or the file is corrupted!!")
