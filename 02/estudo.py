a = input() 
b = input() 
c = input() 

if a == 'vertebrado': 
  if b == 'mamifero':
    if c == 'onivoro':
      print("homem")
    elif c == 'herbivoro':
      print("vaca")
  elif b == 'ave':
    if c == 'carnivoro':
      print("aguia")
    elif c == 'onivoro':
      print("pomba")

elif a == 'invertebrado':
     print('invertebrado')