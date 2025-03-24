def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("john", "doe"))

"""
Adding type hints makes IDEs and their autocorrects more useful.
"""
def get_full_name(first_name: str, last_name:str):
    full_name = first_name.title() + " " + last_name.title()
    
    return full_name