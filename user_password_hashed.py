import hashlib as hl

class Password:
    def __init__(self):
        user_pass = input('Enter password plz')
        self.hash_pass = self.hash_it(user_pass)

    def hash_it (self, user_pass):
        self.hash_pass = hl.sha1(user_pass.encode()).hexdigest()
        return self.hash_pass

    def print_pass(self):
        print('Your password hashed is:   ', self.hash_pass)
        print('length of your password hashed is: ', len(self.hash_pass))


myPass = Password()
myPass.print_pass()