# Entendendo a função print:
print(12,3) # Pode passar mais de um argumento
print(56,4) # Pode passar mais de um argumento
print(56123,4, sep="_") # Usando o separador 
print(56123,4, sep=',') # Usando o separador 

# \r\n -> CRLF
# \n -> LF
print(22,45, sep='-', end='\r\n')
print(12,4, 3, sep=',')
print(23, 3,sep='.', end='\n##')