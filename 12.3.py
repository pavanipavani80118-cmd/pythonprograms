class myclass:
    def __init__(self):
        self.public_attribute="i'm a public attribute"
        self._protected_attribute="i'm a protected attribute"
        self.__private_attribute="i'm a private attribute"
    def public_method(self):
        print("i'm a public method")
    def _protected_method(self):
        print("i'm a protected method")
    def __private__method(self):
        print("i'm a private method")
obj=myclass()
print(obj.public_attribute)
obj.public_method()
print(obj._protected_attribute)
obj._protected_method()
print(obj._myclass__private_attribute)
obj._myclass__private__method()

        
