#Desenvolva um programa que indique se as medidas informadas formam um triangulo escaleno (lados diferentes), triangulo isósceles (dois lados iguais) ou 
#triangulo equilátero (todos os lados iguais) 
#Considerando que para que as medidas informadas possam formar um triangulo eles devem seguir a regra r1+r2>r3
print('Analisador de triângulos')
r1 = float(input('Primeiro lado: '))
r2 = float(input('Segundo lado: '))
r3 = float(input('Terceiro lado: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print('As medidas informadas formam um triângulo')
else:
  print('As medidas informadas não forma um triângulo')
