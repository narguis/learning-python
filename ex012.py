# Calculating the new price of a product if a 5% discount is applied

preco = float(input("\033[34mQual é o preço do produto?\033[m "))
desconto = preco-(preco*(5/100))
print(f"O produto que custava \033[31mR${preco}\033[m na promoção de "
      f"\033[32m5%\033[m passará a custar \033[32mR${desconto}\033[m")
