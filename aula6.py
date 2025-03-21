""" 
Conversão de tipos, coerção
type convertion, typecasting, coercion
é o ato de converter um tipo em outro
tipos imutáveis e primitivos:
str, intm, float, bool
"""
print('1', type('1'))
 
print(int('1'), type(int('1'))) # processo de coerção
print(int('11') + 2)
print(float('13') - 5.2)
print(bool('')) # false
print(bool(' ')) # true
print(str(31) +' anos ')