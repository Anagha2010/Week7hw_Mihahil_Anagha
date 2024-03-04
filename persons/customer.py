from persons.person import Person

class Customer(Person):

    def __init__(self, name, cust_id, merchant):
        super().__init__(name, age=None, profession='Customer', pronoun='they')
        self.cust_id = cust_id
        self.merchant = merchant
        self.item_or_service = ''
        self.order_amount = 0
        self.loyalty_points = 0

    # getters and setters

    def place_order(self, item_name, amount):
        self.item_or_service = item_name
        self.order_amount = amount
        self.loyalty_points += self.order_amount//10
        return (f"\nOrder placed by, Name: {self.name}, Customer ID: {self.cust_id} for {self.item_or_service}."
                f"\nOrder amount: Galleons {self.order_amount}\tLoyalty points earned: {self.loyalty_points}")
