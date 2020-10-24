class Product:
  initName = ""
  initPrice = 0.0
  initQuantity = 0

  def __init__(self, initial_name, initial_price, initial_quantity):
    self.initName = initial_name
    self.initPrice = initial_price
    self.initQuantity = initial_quantity
  
  def print_product(self):
    print("%s, price %s, %s pcs"%(self.initName,self.initPrice,self.initQuantity))