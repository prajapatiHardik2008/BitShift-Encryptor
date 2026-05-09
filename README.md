# BitShift-Encryptor
git clone https://github.com/yourusername/ByteShift-Encryptor.git
    cd ByteShift-Encryptor
    ```

2.  **Run the Tool:**
    ```bash
    python encryptor.py
    ```

3.  **Operations:**
    *   **Encrypt:** Enter `1`, provide the file path, and a secret key. Your file will be transformed into an unreadable format.
    *   **Decrypt:** Enter `2`, provide the path to the encrypted file, and use the **exact same key** to restore the original data.

---

## ⚠️ Security Disclaimer
This tool is intended for **educational purposes** and personal projects. It uses a symmetric substitution cipher which is vulnerable to frequency analysis and brute-force attacks. For high-security needs, always use industry-standard algorithms like AES or RSA.

---

## 🤝 Contributing
Contributions are welcome! If you'd like to add a GUI, support for multiple files, or implement more complex algorithms, feel free to fork the repo and submit a Pull Request.

---

### 📝 License
This project is openHere is the professional English version of the README for your repository.

### 📁 Suggested Repository Names:
*   **ByteShift-Vault**
*   **Simple-File-Cipher**
*   **KeyLength-Encryptor**

---

### 📄 README.md

# ByteShift-Encryptor 🔐

A lightweight Python-based file encryption and decryption tool that operates at the byte level using a custom mathematical offset. It uses both a fixed constant and the length of a user-provided key to scramble data.

---

## ✨ Features
*   **Byte-Level Manipulation:** Works on any file type (Images, PDFs, Text files, etc.) by modifying the raw byte data.
*   **Dynamic Offsetting:** The encryption strength relies on a combination of a fixed shift and the length of your secret key.
*   **No Dependencies:** Built entirely with standard Python libraries. No `pip install` required.
*   **Safe-Byte Handling:** Specifically designed to skip certain control characters (Byte 13) to prevent common file-handling errors.

---

## 🛠️ How It Works

The script iterates through every byte of the target file and applies a Caesar-cipher-inspired transformation.

**Encryption Logic:**
$$NewByte = (OriginalByte + 5 + len(Key)) \pmod{256}$$

**Decryption Logic:**
$$OriginalByte = (EncryptedByte - 5 - len(Key)) \pmod{256}$$

### The Workflow:
1. The script reads the file in binary mode (`rb`).
2. It calculates a "Shift Factor" based on your key length.
3. It rewrites the file with the new byte values (`wb`).

---

## 🚀 Usage

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/ByteShift-Encryptor.git
    cd ByteShift-Encryptor
    ```

2.  **Run the Tool:**
    ```bash
    python encryptor.py
    ```

3.  **Operations:**
    *   **Encrypt:** Enter `1`, provide the file path, and a secret key. Your file will be transformed into an unreadable format.
    *   **Decrypt:** Enter `2`, provide the path to the encrypted file, and use the **exact same key** to restore the original data.

---

## ⚠️ Security Disclaimer
This tool is intended for **educational purposes** and personal projects. It uses a symmetric substitution cipher which is vulnerable to frequency analysis and brute-force attacks. For high-security needs, always use industry-standard algorithms like AES or RSA.

---

## 🤝 Contributing
Contributions are welcome! If you'd like to add a GUI, support for multiple files, or implement more complex algorithms, feel free to fork the repo and submit a Pull Request.

---

### 📝 License
This project is open-source and available under the [MIT License](LICENSE).
