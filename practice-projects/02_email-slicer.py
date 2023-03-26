
mail = ''
def validate_email():
    global mail
    mail = input('enter a email address? ')
    if ('@' in mail) and ( '.' in mail):
        return True
    return False

while True:
    if validate_email():
        user, domain = mail.split('@')
        domain, sub_domain = domain.split('.')
        print(f'Your username is {user}, domain is {domain} and sub-domain is {sub_domain.upper()}')
        break
    else:
        print('Please enter a valid once')
