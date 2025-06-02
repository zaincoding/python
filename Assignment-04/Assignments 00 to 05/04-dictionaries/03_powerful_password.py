
from hashlib import sha256
def login(email, stored_logins, password_check):
    if stored_logins[email] == hash_password(password_check):
        return True
    return False


def hash_password(password):
    return sha256(password.encode()).hexdigest()

def main():

    stored_logins = {
        "example@gmail.com": "82f20f6c10f1f4da04c9ce896704969498e0a7820f865794a9b5b85fef3f75b1",
        "example@gmail.com": "82f20f6c10f1f4da04c9ce896704969498e0a7820f865794a9b5b85fef3f75b1"

    }
    print(login("example@gmail.com", stored_logins, "zain123"))
    print(login("example@gmail.com", stored_logins, "zain1234"))
if __name__ == '__main__':
    main()