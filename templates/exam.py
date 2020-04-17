class Ticket_16:
   def convertTemp(self, temperature, convertTo):
    if (convertTo == 'F'):
      temperature = (temperature - 32) * (5/9)
    else:
      temperature = temperature * (9/5) + 32
    
 
    return temperature

  