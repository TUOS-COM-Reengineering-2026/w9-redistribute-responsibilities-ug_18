from Account import Account
from Branch import Branch
from Customer import Customer
from Payroll import Payroll
from Staff import Staff


class Bank:
    def __init__(self):
        self.accounts = []
        self.customers = []
        self.branches = []

    def setup_branch(self, branch: Branch):
        self.branches.append(branch)

    def close_branch(self, branch: Branch, transfer_branch: Branch):
        for staff in branch.get_staff():
            self.transfer_staff_member(branch, transfer_branch, staff)
        self.branches.remove(branch)

    def transfer_staff_member(
        self, from_branch: Branch, to_branch: Branch, staff: Staff
    ):
        from_branch.remove_staff_member(staff)
        to_branch.add_staff_member(staff)

    def setup_new_account(self, account: Account, customer: Customer):
        account.set_customer(customer)
        self.accounts.append(account)
        customer.add_account(account)

        if customer not in self.customers:
            self.customers.append(customer)

    def obtain_balance(self, account: Account):
        return account.get_balance()

    def add_interest(self, account: Account):
        account.add_interest()

    def add_funds(self, account: Account, amount: float):
        account.add_funds(amount)

    def close_account(self, account: Account):
        customer = account.get_customer()
        account.close()
        if customer:
            customer.remove_account(account)
        self.accounts.remove(account)

    def change_payroll_date(self, payroll: Payroll, date: str, staff_category: str):
        payroll.change_payroll_date(date, staff_category)
