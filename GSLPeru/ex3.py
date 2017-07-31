# SOLUTION Ex. 3
pizza_orders = ['pepperoni', 'hawaiian', 'cheese', 'veggie', 'cheese', 'cheese']
finished_pizzas = {}
for pizza in pizza_orders:
  if pizza not in finished_pizzas:
    finished_pizzas[pizza] = 1
    print(pizza.title() + " is done!")
  else:
    finished_pizzas[pizza] += 1
    print(pizza.title() + " is done!")
print("\nI finished these pizzas: ")
for key in finished_pizzas.keys():
  print(key + ": " + str(finished_pizzas[key]))