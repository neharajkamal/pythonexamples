''' 
    logic
    Accept first name 
    Accept last Name
    Print  first name last name
    Print  L. firstname
    Print  Lastname, First name
'''

''' variables should begin with alphabet followed by alpha numeric without any special characters'''

firstname = input("Enter your first name: ")

lastname = input("Enter your last name: ")

print("{0} {1}".format(firstname, lastname))

print("{0}. {1}".format(lastname[0], firstname))

print("{0}, {1}".format(lastname, firstname))







