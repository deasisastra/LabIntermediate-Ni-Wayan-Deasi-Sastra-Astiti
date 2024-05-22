# No 1
class Counter:
   def __init__(self):
      self.count = 0
   def reset(self):
      self.count = 0
   def click(self):
      self.count += 1
   def get_value(self):
      return self.count
   
tally = Counter()
tally.reset()
tally.click()
tally.click()
result = tally.get_value()  # Hasilnya adalah 2
print(result)
tally.click()
result = tally.get_value()  # Hasilnya adalah 3
print(result)

# Error yang terjadi adalah karena perintah tally.reset (line 2 di atas) tidak dijalankan (dihapus). Perintah ini penting untuk menyetel 
# ulang penghitung ke 0 sebelum memulai penghitungan klik. Tanpa perintah ini, penghitung akan terus bertambah dari nilai terakhirnya.




# No 2
class CashRegister:
    def __init__(self):
        self.total = 0.0
        self.item_count = 0
    
    def addItem(self, price):
        self.total += price
        self.item_count += 1
    
    def getTotal(self):
        return self.total
    
    def getCount(self):
        return self.item_count

# Test the class with the given test cases
register1 = CashRegister()
register1.addItem(1.95)
register1.addItem(0.95)
register1.addItem(2.50)

register2 = CashRegister()
register2.addItem(3.75)
register2.addItem(0.15)
register2.addItem(2.25)
register2.addItem(1.80)

# Print the totals and counts
print("Register 1 sells", register1.getCount(), "items, with the total amount of $", register1.getTotal())
print("Register 2 sells", register2.getCount(), "items, with the total amount of $", register2.getTotal())




# No 3
class Fraction:

  def __init__(self, numerator, denominator):
    self.numerator = numerator
    self.denominator = denominator

    # Simplify the fraction
    self._simplify()

  def _gcd(self, a, b):

    while b != 0:
      a, b = b, a % b
    return a

  def _simplify(self):

    gcd = self._gcd(self.numerator, self.denominator)
    self.numerator //= gcd
    self.denominator //= gcd

  def __str__(self):

    return f"{self.numerator}/{self.denominator}"

  def to_float(self):

    return self.numerator / self.denominator

# Example usage
fraction1 = Fraction(1, 3)
fraction2 = Fraction(1, 2)

print(f"Fraction 1: {fraction1}")  # Output: Fraction 1: 1/3
print(f"Fraction 1 as float: {fraction1.to_float():.2f}")  # Output: Fraction 1 as float: 0.33

print(f"Fraction 2: {fraction2}")  # Output: Fraction 2: 1/2
print(f"Fraction 2 as float: {fraction2.to_float():.2f}")  # Output: Fraction 2 as float: 0.50
