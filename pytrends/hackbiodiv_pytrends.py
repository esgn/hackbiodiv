from pytrends.pyGTrends import pyGTrends
import time
import os
from random import randint

google_username = "votre_identifiant_google"
google_password = "votre_mot_de_passe_google"

# Changer la partie du path entre guillemets
# pour choisir l'emplacement de stockage du csv
path = "D:\DATA\HackBiodiv" + os.sep

# connect to Google
connector = pyGTrends(google_username, google_password)

# make request
connector.request_report("ambroisie")

# wait a random amount of time between requests to avoid bot detection
time.sleep(randint(5, 10))

# download file
connector.save_csv(path, "ambroisie")

# get suggestions for keywords
# Le resulat des suggestions peut etre utilise comme mot cle
# exemple "/m/02fzjg" pour ambroisie plante
keyword = "ambroisie"
data = connector.get_suggestions(keyword)
print(data)
