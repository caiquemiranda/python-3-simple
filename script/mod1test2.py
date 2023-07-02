# Este é script/mod1test2.py :

from script.mod1 import saudacao, ola, escrito_por

ola()
ola.escrito_por = 'Miranda'

print('escrito por = ', ola.escrito_por)
print(escrito_por)

greet = saudacao()
greet.manha()
greet.noite()