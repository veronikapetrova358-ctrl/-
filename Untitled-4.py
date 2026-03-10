x - float(input("Введіть відстань (км): "))
total - 0 #загальна відстань
current - 6
hours - 0
while total < x and current > 0:
      total += current
      hours += 1
      current -= 1
if total >= x: 
   print("Туристка подолає відстань за", hours, "год")
else: 
   print("Подолати таку відстань неможливо.")
