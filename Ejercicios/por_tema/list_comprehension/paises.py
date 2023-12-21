#Crea una lista con paises e imprime lso paises que tengan  la leyenda (LA)

paises = ["Mexico (LA)", "España", "Francia", "Canada", "Brasil (LA)", "China"]

en_mayusculas = [i.upper() for i in paises if "LA" in i]

print(en_mayusculas)