class UserManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_user(self, username, email):
        self.db_connection.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))

    def get_user(self, username):
        result = self.db_connection.execute("SELECT email FROM users WHERE username = ?", (username,))
        return result.fetchone()

    def update_user(self, username, new_email):
        self.db_connection.execute("UPDATE users SET email = ? WHERE username = ?", (new_email, username))

    def delete_user(self, username):
        self.db_connection.execute("DELETE FROM users WHERE username = ?", (username,))
