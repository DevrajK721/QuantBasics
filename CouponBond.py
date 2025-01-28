
class CouponBond():
    def __init__(self, principal, rate, maturity, interest_rate):
        self.principal = principal # Principal amount
        self.rate = rate / 100 # Coupon rate
        self.maturity = maturity # Maturity date
        self.interest_rate = interest_rate / 100 # Market Interest rate (for discounting)
        
    def present_value(self, x, n):
        return x / (1 + self.interest_rate) ** n
    
    def calculate_price(self):
        price = 0
        # Discount the coupon payments 
        for t in range(1, self.maturity):
            price += self.present_value(self.principal * self.rate, t)
        
        # Discount Principal amount 
        price += self.present_value(self.principal, self.maturity)
        
        return price

if __name__ == "__main__":
    bond = CouponBond(principal=1000, rate=10, maturity=3, interest_rate=4) 
    print(f"{bond.calculate_price():.2f}") # 1166.61