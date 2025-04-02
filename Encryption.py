import streamlit as st
from Crypto.Cipher import AES
import os

#Function to encrypt the file's data

def EncryptFileData(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext,tag=cipher.encrypt_and_digest(data)
    return cipher.nonce+tag+ciphertext

#Function to decrypt the file's data
def DecryptFileData(encryptedData,key):
    nonce = encryptedData[:16]
    tag = encryptedData[16:32]
    ciphertext = encryptedData[32:]
    cipher = AES.new(key, AES.MODE_EAX,nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext,tag)

#streamlit UI
st.title("🔏 ADVANCED ENCRYPTION TOOL")
st.write("ENCRYPT AND DECRYPT FILES USING AES-256")

mode = st.radio("Choose Mode: ", ["Encrypt","Decrypt"])

uploadedFile = st.file_uploader("Upload a file", type=["txt","pdf","png","jpeg","bin"])
password= st.text_input("Enter a secret key(Must be of 32 characters): ", type="password")

if uploadedFile and password:
    key = password.ljust(32).encode()[:32] #Ensuring key is exactly 32 bytes
    fileBytes = uploadedFile.read() #To read the file conetnt

    if mode=="Encrypt":
        encrypted_data = EncryptFileData(fileBytes,key)
        #download the encrypted file
        st.download_button("Download Encrypted File",encrypted_data,file_name="encrypted.bin")
        
    elif mode == "Decrypt":
        try:
            decrypted_data = DecryptFileData(fileBytes,key)
            st.download_button("Download Decrypted File",decrypted_data,file_name="decrypted.txt")
        except ValueError:
            st.error("Decryption failed! Incorrect key or the file is corrupted!!")
