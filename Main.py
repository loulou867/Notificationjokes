
# On import les modules nécessaire
import time
import pyjokes
from win10toast import ToastNotifier
# création & assignation de la variable blague
blague = pyjokes.get_joke() # pyjoke.get_joke() récupère une blague dans une banque de données de blagues

# Répété 5 fois avec un intervalle de 1800s et une durée d'affichage de 10 s
while 5:
    notify = ToastNotifier()
    notify.show_toast("Une bonne blague :", blague, duration = 10)
    time.sleep(1800)