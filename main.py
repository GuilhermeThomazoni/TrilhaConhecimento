import agelib

try:
    idade = agelib.get_idade()
except ValueError:
    print("Tipo do valor informado inválido!")
    idade = None

print("Idade informada: ", (idade or "null"))