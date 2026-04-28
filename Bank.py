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
        self.payroll = None

    def setup_branch(self, branch: Branch):
        self.branches.append(branch)
        
    def close_branch(self, branch: Branch, transfer_branch: Branch):
        for staff in branch.get_staff():
            self.transfer_staff_member(branch, transfer_branch, staff)
        self.branches.remove(branch)

    def transfer_staff_member(self, from_branch: Branch, to_branch: Branch, staff: Staff):
        from_branch.remove_staff(staff)
        to_branch.add_staff(staff)

    def setup_new_account(self, account: Account, customer: Customer):
        account.set_customer(customer)
        self.accounts.append(account)
        customer.add_account(account)

        if customer not in self.customers:
            self.customers.append(customer)

    def obtain_balance(self, account: Account):
        return account.get_balance()

    def add_funds(self, account: Account, amount: float):
        balance = account.get_balance()
        account.set_balance(balance + amount)

    def close_account(self, account: Account):
        customer = account.get_customer()
        account.close()
        if customer:
            customer.remove_account(account)

        self.accounts.remove(account)

    def add_staff_member(self, branch: Branch, staff: Staff):
        branch.add_staff(staff)

    def change_opening_time(self, branch: Branch, time: str):
        self.branch_opening_times[branch] = time
