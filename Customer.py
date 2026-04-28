class Customer:
    def __init__(self, name: str):
        self._name = name
        self._address = "NO ADDRESS" # default value for address and phone number
        self._phone_number = "NO PHONE NUMBER"
        self._accounts = []

    def set_name(self, name: str):
        self._name = name

    def get_name(self):
        return self._name

    # getters and setters for address and phone number
    # and account management methods 

    def set_address(self, address: str):
        self._address = address

    def get_address(self):
        return self._address

    def set_phone_number(self, phone_number: str):
        self._phone_number = phone_number

    def get_phone_number(self):
        return self._phone_number

    def add_account(self, account):
        self._accounts.append(account)

    def remove_account(self, account):
        self._accounts.remove(account)

    def get_accounts(self):
        return self._accounts