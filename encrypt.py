iimport os
from cryptography.fernet import Fernet

KEY_FILE = "folder.key"

# ---------- KEY GENERATION ----------
def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        print("[+] Key generated")
    else:
        print("[!] Key already exists")

def load_key():
    return open(KEY_FILE, "rb").read()

# ---------- FILE ENCRYPT ----------
def encrypt_file(path, fernet):
    with open(path, "rb") as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(path, "wb") as f:
        f.write(encrypted)

# ---------- FILE DECRYPT ----------
def decrypt_file(path, fernet):
    with open(path, "rb") as f:
        data = f.read()
    decrypted = fernet.decrypt(data)
    with open(path, "wb") as f:
        f.write(decrypted)

# ---------- FOLDER ENCRYPT ----------
def encrypt_folder(folder_path):
    key = load_key()
    fernet = Fernet(key)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, fernet)

    print("[✓] Folder encrypted successfully")

# ---------- FOLDER DECRYPT ----------
def decrypt_folder(folder_path):
    key = load_key()
    fernet = Fernet(key)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, fernet)

    print("[✓] Folder decrypted successfully")

# ---------- MAIN ----------
if __name__ == "__main__":
    print("1. Generate Key")
    print("2. Encrypt Folder")
    print("3. Decrypt Folder")

    choice = input("Select option: ")

    if choice == "1":
        generate_key()

    elif choice == "2":
        folder = input("Enter folder path: ")
        encrypt_folder(folder)

    elif choice == "3":
        folder = input("Enter folder path: ")
        decrypt_folder(folder)

    else:
        print("Invalid option")