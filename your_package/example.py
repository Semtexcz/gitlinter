def add(x,y):
    return x+y

def subtract(x,y):
  return x-y # Chyba: nekonzistentní odsazení

def multiply(x, y): return x*y # Chyba: nevhodné umístění příkazu na jednom řádku

z=add(5,2)*subtract(3,1) # Chyba: chybí mezery okolo operátorů
print(z)
