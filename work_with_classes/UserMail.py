class UserMail:
    def __init__(self, login, mail):
        self.login = login
        self.__email = mail

    def get_email(self):
        return self.__email

    def set_email(self, input_mail):
        if isinstance(input_mail, str) and input_mail.count('@') == 1 and '.' in input_mail[input_mail.index(
                '@'):] and input_mail.count('.') >= 1:
            self.__email = input_mail
        else:
            print("Ошибочная почта")

    email = property(fget=get_email, fset=set_email)
