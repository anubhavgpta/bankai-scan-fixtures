def find_user(connection, username: str):
    # Fixture: parameterized query to prevent SQL injection.
    query = "SELECT id, username, password FROM users WHERE username = ?"
    return connection.execute(query, (username,)).fetchone()
