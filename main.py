class User:
    def __init__(self) -> None:
        print("user created")


user1 = User()

user1.id = "001"
user1.name = 'Ola'

print(user1)