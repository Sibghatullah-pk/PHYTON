from cryptography.fernet import Fernet


pwd = input("What is your master password? ")

MASTER_PASSWORD = "SIBGHAT"  
if pwd != MASTER_PASSWORD:
    print("Access denied. Incorrect master password.")
    quit()

print("Access granted.")
def load_key():
    try:
        with open("key.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        return key

key = load_key()
fer = Fernet(key)
def view():
    try:
        with open("passwords.txt", "r") as f:
            lines = [line.strip() for line in f if line.strip()]
            if not lines:
                print("No passwords found.")
                return
            for line in lines:
                website, enc_pass = line.split("|")
                decrypted_pass = fer.decrypt(enc_pass.encode()).decode()
                print(f"Website: {website.strip()}, Password: {decrypted_pass}")
    except FileNotFoundError:
        print("No password file found.")

def add():
    name = input("Enter the website name: ")
    password = input("Enter the password: ")
    encrypted_pass = fer.encrypt(password.encode()).decode()
    with open("passwords.txt", "a") as f:
        f.write(f"{name} | {encrypted_pass}\n")
    print("Password added successfully!")

while True:
    mode = input("Would you like to add a new password or view existing ones? (add/view) or 'q' to quit: ").lower()
    
    if mode == "q":
        print("Exiting the password manager. Goodbye!")
        break
    elif mode == "add":
        add()
    elif mode == "view":
        print("Here are your passwords:")
        view()
    else:
        print("Invalid mode. Please choose 'add', 'view', or 'q'.")
 