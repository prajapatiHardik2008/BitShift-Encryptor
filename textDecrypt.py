
def encrypt(path,key):
    try:
        with open(path,'rb') as f:
            text = f.read()
        encryptData = bytearray()
        for i in text:
            if i == 13:
                continue
            encryptData.append((i + 5 + len(key)) % 256)
        with open(path,'wb') as f:
            f.write(encryptData)

        print("Encryption complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt(path,key):
    try:
        with open(path,'rb') as f:
            text = f.read()
        decryptText = bytearray()
        for i in text:
            if i == 13:
                continue
            decryptText.append((i - 5 - len(key)) % 256)
        with open(path,'wb')  as f:
            f.write(decryptText)
        print("Decryption complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

print("[+] Welcome to the Text Encryptor/Decryptor")
print("[+] Please choose an option:")
print("[+] 1. Encrypt a file")
print("[+] 2. Decrypt a file")  
while True:
    choice = input("[+] Enter your choice (1 or 2): ")
    if choice == '1':
        file_path = input("[+] Enter the path of the file to encrypt: ")
        key = input("[+] Enter the encryption key: ")
        encrypt(file_path, key)
        break
    elif choice == '2':
        file_path = input("[+] Enter the path of the file to decrypt: ")
        key = input("[+] Enter the decryption key: ")
        decrypt(file_path, key)
        break
    else:
        print("[!] Invalid choice. Please enter 1 or 2.")   