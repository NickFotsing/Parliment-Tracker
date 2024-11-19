import customtkinter as ctk
import sqlite3
import bcrypt
import main

# Database connections
def create_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) #Hashing
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:  #  Error handling
        return False
    finally:
        conn.close() # cLOSSED connection

def validate_user(username, password): #user valiation
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result and bcrypt.checkpw(password.encode('utf-8'), result[0]):
        return True
    return False

# Registration Page Class
class RegistrationPage(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        self.title("Register")
        self.geometry("400x250")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Username Label and Entry
        self.username_label = ctk.CTkLabel(self, text="Username")
        self.username_label.pack(pady=(20, 5))
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Enter username")
        self.username_entry.pack(pady=(0, 10))

        # Password Label and Entry
        self.password_label = ctk.CTkLabel(self, text="Password")
        self.password_label.pack(pady=(0, 5))
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Enter password", show="*")
        self.password_entry.pack(pady=(0, 10))

        # Register Button
        self.register_button = ctk.CTkButton(self, text="Register", command=self.register)
        self.register_button.pack(pady=(20, 5))

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if create_user(username, password):
            print("Registration successful! You can now log in.")
            self.destroy()  # Close the registration window
            LoginPage()  # Reopen the login page
        else:
            print("Username already exists! Please choose a different username.")

# Login Page Class
class LoginPage(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Login Page")
        self.geometry("400x300")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Username Label and Entry
        self.username_label = ctk.CTkLabel(self, text="Username")
        self.username_label.pack(pady=(20, 5))
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Enter username")
        self.username_entry.pack(pady=(0, 20))

        # Password Label and Entry
        self.password_label = ctk.CTkLabel(self, text="Password")
        self.password_label.pack(pady=(0, 5))
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Enter password", show="*")
        self.password_entry.pack(pady=(0, 20))

        # Login Button
        self.login_button = ctk.CTkButton(self, text="Login", command=self.login)
        self.login_button.pack(pady=(20, 5))

        # Register Button
        self.register_button = ctk.CTkButton(self, text="Register", command=self.open_registration)
        self.register_button.pack(pady=(5, 20))

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if validate_user(username, password):
            print("Login successful")
            self.destroy()  # Closing the login window WINDOW GOES BOOOOOOOOOOOOOOOOOM
            main.run_main_application()  # Calling the main application function
        else:
            print("Login failed! Please check your username and password.")

    def open_registration(self):
        RegistrationPage()  # Open the registration window

# Database setup function to create the database and table if it doesn't exist (New users only)
def setup_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Run the application
if __name__ == "__main__":
    setup_database()
    app = LoginPage()
    app.mainloop()
