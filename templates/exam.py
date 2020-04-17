class Ticket_16:
   def convertTemp(self, temperature, convertTo):
    if (convertTo == 'F'):
      temperature = (temperature - 32) * (5/9)
    else:
      temperature = temperature * (9/5) + 32
    
 
    return temperature


if __name__ == "__main__":
    converter = Ticket_16()
    res=converter.convertTemp(100, "С")
    print(f"100*C -> {res}*F")
    res=converter.convertTemp(38, "F")
    print("38*F -> {res}3.3*C")