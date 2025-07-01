# Python stores Class variables in the __dict__ attribute
# It is a mapping proxy which is a dictionary

from pprint import pprint # prints the dictionaries e.t.c it recursively

class Manjaro:
    kernel = "Linux"
    version = "6.12.28"

    # when you add a function to a class it is referred as a class attribute
    # since a function is callable it is called a callable class attribute
    def osInfo():
        print(f"Manjaro use a {kernel} kernel which is version {version}")

pprint(Manjaro.__dict__)
