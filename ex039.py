# Asks for the year you were born and says if you need to enlist yourself to
# mandatory military service

from datetime import date
ano = int(input('Em que ano você nasceu? '))
data = date.today().year - ano
if data < 18:
    print(f'\033[1;32mAinda falta(m) {18-data} ano(s) para o seu alistamento!\033[m')
elif data > 18:
    print(f'\033[1;31mVocê deveria ter se alistado há {data-18} ano(s) atrás!\033[m')
else:
    print(f'\033[1;34mEstá na hora de se alistar!\033[m')
