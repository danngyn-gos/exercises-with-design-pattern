from abc import ABC, abstractmethod

class Payment:
    def __init__(self, amount: float):
        self.amount = amount
    
    @abstractmethod
    def process(self) -> None:
        pass

class CreditCardPayment(Payment):
    def process(self) -> None:

        print(f"Processing credit card payment of ${self.amount}")
        print("Validating credit card details...")
        print("Charging the credit card...")

class PayPalPayment(Payment):
    def process(self) -> None:
        print(f"Processing PayPal payment of ${self.amount}")
        print("Redirecting to PayPal...")
        print("Completing PayPal transaction...")


class CashPayment(Payment):
    def process(self) -> None:
        print(f"Recording cash payment of ${self.amount} and generating receipt.")
        print("Awaiting physical collection of funds.")

def handle_any_payment(payment: Payment) -> None:
    print("--- Starting Transaction ---")
    payment.process()
    print("--- Transaction Complete ---")


if __name__ == "__main__":
    handle_any_payment(CreditCardPayment(100.00))

    print('\n')
    handle_any_payment(PayPalPayment(200.00))

    print('\n')
    handle_any_payment(CashPayment(50.00))