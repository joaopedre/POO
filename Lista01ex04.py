print("Digite quatro valores: ")
a = int(input())
b = int(input())
c = int(input())
d = int(input())

pares=[]
impares=[]

if a%2 == 0: pares.append(a)
if b%2 == 0: pares.append(b)
if c%2 == 0: pares.append(c)
if d%2 == 0: pares.append(d)
if a%2 != 0: impares.append(a)
if b%2 != 0: impares.append(b)
if c%2 != 0: impares.append(c)
if d%2 != 0: impares.append(d)

print(f"Pares: ", {sum(pares)})
print(f"Impares: ", {sum(impares)})