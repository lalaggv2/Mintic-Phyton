#palindrome

frase0 = "luzazul"
frase1 = 'severlaalreves'
frase2 = 'anitalavalatina'
frase3 = 'Holamundo'

def palindrome(frase):
  frase2 = frase[::-1]
  if frase == frase2:
    print('Es palindrome')
  else:
    print('No es palindrome')

palindrome(frase)