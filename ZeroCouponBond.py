
class ZeroCouponBonds:
    def __init__(self, principal, maturity, interest_rate):
        self.principal = principal # Principal amount
        self.maturity = maturity # Maturity date
        self.interest_rate = interest_rate / 100 # Market Interest rate (for discounting)
    
    def present_value(self, x, n):
        return x / ((1 + self.interest_rate) ** n) 

    def calculate_price(self):
        return self.present_value(self.principal, self.maturity) 
    
if __name__ == "__main__":
    bond = ZeroCouponBonds(principal=1000, maturity=2, interest_rate=4) 
    print(f"{bond.calculate_price():.2f}") # 924.56