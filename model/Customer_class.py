import salabim as sim
class Customer(sim.Component):
    """
    Customer class for the supermarket.
    Traverses the store to via its route to fulfill its shopping_list, while carrying either a shopping basket or cart.
    """
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__name__ = 'CustomName'
        self.InitModel = model.__getattribute__("l")
        self.route = self.InitModel.route_distribution_pdf.sample()
        self.shopping_list = {
            "fruit_and_vegetables": int(round(self.InitModel.fruit_and_vegetables_distribution.sample())),
            "meat_and_fish": int(round(self.InitModel.meat_and_fish_distribution.sample())),
            "bread": int(round(self.InitModel.bread_distribution.sample())),
            "cheese_and_dairy": int(round(self.InitModel.cheese_and_dairy_distribution.sample())),
            "canned_and_packed_food": int(round(self.InitModel.canned_and_packed_food_distribution.sample())),
            "frozen_foods": int(round(self.InitModel.frozen_food_distribution.sample())),
            "drinks": int(round(self.InitModel.drinks_distribution.sample())),
        }
        self.carrying = None
        self.actions_log = []


    def log_action(self, action):
        """Helper function to log an action with the current time."""
        self.actions_log.append((self.InitModel.env.now(), action))

    def process(self):
        """"
        Process determines what the customer will do. At the start they will take a cart or basket. Afterwards they will traverse their route and take the items they need according to their shopping list. If they have finished their route (when progress is equal to the length of the shopping list), they will go to the checkout.
        """
        self.start_shopping()
        for next_product in self.route:
            if self.shopping_list[next_product] > 0:
                self.get_product(next_product)
        self.go_to_checkout()

    def start_shopping(self):
        """ Get either a shopping cart or basket"""
        want_to_carry = self.InitModel.cart_basket_distribution.sample()
        self.log_action(f"Entered cart/basket queue for {want_to_carry}")
        self.request(want_to_carry)
        self.log_action(f"Got {want_to_carry}")
        self.carrying = want_to_carry

    def go_to_checkout(self):
        """Proceed to the emptiest queue in the checkout and wait while items are processed. Returns shopping cart/basket afterwards."""
        # enter emptiest queue
        emptiest_queue = min(self.InitModel.number_of_checkouts, key=lambda checkout: checkout.requesters().length())
        self.log_action(f"Entered checkout queue {emptiest_queue}")
        self.request(emptiest_queue)
        self.log_action(f"Started checking out")
        item_scan_time = sum(self.InitModel.time_per_item_distribution.sample() for _ in range(sum(self.shopping_list.values())))
        self.hold(
            item_scan_time + self.InitModel.payment_time_distribution.sample())  # hold the customer for scanning all items and during payment
        self.log_action(f"Finished checking out")
        # return cart/basket (implicit since process finishes)

        # print log if we want to debug

        if self.InitModel.customer_to_log:
            if self.name() == f"customer.{self.InitModel.customer_to_log}":
                print(self.carrying.claimers().print_info())
                print(f"Customer's Action Log for customer {self.name()}:")
                for time, action in self.actions_log:
                    print(f"At time {time}, customer: {action}")

    def get_product(self, product):
        """
        Function to get the required number of {product}.
        Customer holds while the products are taken.
        Special cases for cheese_and_dairy and bread as they require clerks.
        """
        if product == "cheese_and_dairy":
            self.log_action(f"requesting cheese and dairy")
            self.request(self.InitModel.cheese_and_dairy_clerks)
            self.log_action(f"Being helped for cheese and dairy")
            self.hold(self.InitModel.cheese_and_dairy_time_distribution.sample())
            self.log_action(f"Got cheese and dairy")
            self.release(self.InitModel.cheese_and_dairy_clerks)
        elif product == "bread":
            self.log_action(f"requesting bread")
            self.request(self.InitModel.bread_clerks)
            self.log_action(f"Being helped for bread")
            self.hold(self.InitModel.bread_time_distribution.sample())
            self.log_action(f"Got bread")
            self.release(self.InitModel.bread_clerks)
        else:
            amount = self.shopping_list[product]
            self.log_action(f"Getting {product}")
            for _ in range(amount):
                self.hold(self.InitModel.time_per_item_distribution.sample())
                self.log_action(f"Got {product}")