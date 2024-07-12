class SavingAccount:
    pass
class ChekingAccount:
    pass
class BankAccount(SavingAccount, ChekingAccount):
    pass
class Stock:
    pass
class Bond:
    pass
class Security(Stock, Bond):
    pass
class InterestBearingItem(BankAccount, Security):
    pass
class RealEstate:
    pass
class InsurableItem(BankAccount, RealEstate):
    pass
class Asset(BankAccount, Security, RealEstate):
    pass
print(Asset.mro())

