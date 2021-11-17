
# On importes la librairie random
from random import *

# On définit les niveaux dans un dictionnaire :
# Le premier 'argument' désnigne la difficluté du niveau, puis
# dans celui-ci nous mettons le nombre de niveau.
# Example: facile aura 5 niveaux ('facile': 5)
niveaux = {
    "facile"        : 5,
    "difficile"     : 12,
    "impossible"    : 20,
}

# On définit les personnages :
# les paranthèses délimitent le tuples,
# celui-ci permet d'avoir à peu près le même effet qu'un tableau,
# on peut contenir des éléments dedans, en l'occurence un dictionnaire:
# le nom, le nombre de billes(marbles), le loss, et le gain.
personnages = (
    {
        "name"      :   "Seong Gi-hun",
        "marbles"   :   25,
        "loss"      :   3,
        "gain"      :   1
    },
    
    {
        "name"      :   "Kang Sae-Byeok",
        "loss"      :   2,
        "gain"      :   2
    },

     {
         "name"     :   "Cho Sang-Woo",
         "loss"     :   1,
         "gain"     :   3
     }
)

# On définit le tuple adversaire
adversaires = ()
 
# Ensuite, dynamiquement on y a ajouter des adversaires:
# 'marbles' : le nombre de billes qu'il possède avec randrange(1, 20) pour
# un integer (donc nombre sans virgule) entre 1 et 20
#On met manuellement les adversaires:
adversaires = (
    {
        "name"      :   "Borislav Iared",
        "marbles"   :   randrange(1, 20)
    },
    {
        "name"      :   "Daisy-Mae Dalby",
        "marbles"   :   randrange(1, 20)
    },
    {
        "name"      :   "Clodagh Carlson",
        "marbles"   :   randrange(1, 20)
    },
    {
        "name"      :   "Genevieve Vincent",
        "marbles"   :   randrange(1, 20)
    },
    {
        "name"      :   "Isabella Lutz",
        "marbles"   :   randrange(1, 20)
    },
    {
        "name"      :   "Colby Greene",
        "marbles"   :   randrange(1, 20)
    },
    {
        "name"      :   "Nakita Woodard",
        "marbles"   :   randrange(1, 20)
    },
    {
        "name"      :   "Curtis Maxwell",
        "marbles"   :   randrange(1, 20)
    },
    {
        "name"      :   "Lochlan Ramsey",
        "marbles"   :   randrange(1, 20)
    },
    {
        "name"      :   "Bea Horn",
        "marbles"   :   randrange(1, 20)
    },
    {
        "name"      :   "Linda John",
        "marbles"   :   randrange(1, 20)
    },
    {
        "name"      :   "Martyna Goddard",
        "marbles"   :   randrange(1, 20)
    },
    {
        "name"      :   "Tehya Blackmore",
        "marbles"   :   randrange(1, 20)
    },
    {
        "name"      :   "Roxy Jackson",
        "marbles"   :   randrange(1, 20)
    },
    {
        "name"      :   "Sanah Hunt",
        "marbles"   :   randrange(1, 20)
    },
    {
        "name"      :   "Aamina Sharples",
        "marbles"   :   randrange(1, 20)
    },
    {
        "name"      :   "Nishat Leach",
        "marbles"   :   randrange(1, 20)
    },
    {
        "name"      :   "Tala Farrington",
        "marbles"   :   randrange(1, 20)
    },
    {
        "name"      :   "Anisa Gamble",
        "marbles"   :   randrange(1, 20)
    },
    {
        "name"      :   "Eva Feeney",
        "marbles"   :   randrange(1, 20)
    },
)


print("--- Choisissez votre niveau ---\n")

# Pour mieux organiser le code, on va récuperer tout les
# éléments du dictionnaire 'niveau' puis les afficher
# grâce au système key / value.
# key désignant le type de niveau (example: facile)
# et value désignant sa valeur, donc en l'occurence 5 niveaux
for key, value in niveaux.items():
    print(f"{key}: {value} niveaux")

# On demande à l'utilisateur de choisir son niveau et on l'inscrit
# dans la variable 'choix_niveaux' (pour être utilisée plus tard).
choix_niveau = input("\nVeuillez choisir votre difficulté (facile/difficile/impossible) > ")

# On instancie la variable 'nombre_de_niveaux' à 0 (pour commencer)
# Puis, en fonction de son choix, adapter sa vauleur.
nombre_de_niveaux = 0

# Le niveau['facile'] (par exemple) sert à récuperer la valeur, en l'occurence 5
# On aurait pu faire if choix_niveaux == 'F': nombre_de_niveaux = 5
# mais au niveau de l'organisation faire comme je le fait est beaucoup plus propre
# et beaucoup plus modulable !
if choix_niveau == "f": nombre_de_niveaux = niveaux["facile"]
if choix_niveau == "d": nombre_de_niveaux = niveaux["difficile"]
if choix_niveau == "i": nombre_de_niveaux = niveaux["impossible"]

print("")

# On itère un tuple avec la fonction enumerate()
# Puis, pour chaque valeur (un personnage) on récupère son nom:
# key[1] signifie que l'on récupère le dictionnaire (ça fonctionne comme ça en tuple)
# key[0] est l'index (ça va nous servir pour séléctionner le personnage !)
for key in enumerate(personnages):
    print(f"{key[0]} - {key[1]['name']}")

# On demande le choix du personnage sous forme d'int !
# Pourquoi ? Tout simplement parce-que par défaut python renvoit la valeur d'un input sous
# forme de chaine de caractère (un string).
# Or, nous voulons un nombre pour récuperer le dictionnaire du personnage
# via son index, qui est un int (nombre) !
choix_personnage = int(input("\nVeuillez choisir votre personnage > "))

# Pour simplifier les choses, j'ai fait une variable pour chaque
# caractéristique (ça évite de réécrire caracteristiques_personnage à chaque fois)
caracteristiques_personnage = personnages[0]
nom     = caracteristiques_personnage["name"]
marbles = caracteristiques_personnage["marbles"]
loss    = caracteristiques_personnage["loss"]
gain    = caracteristiques_personnage["gain"]

print("")

# On démarre !
for i in range(nombre_de_niveaux):

    # On prends l'adversaire aléatoire avec le randrange
    # Entre 1 et 19 (car ça commence à 0 !)
    adversaire = adversaires[randrange(1, 19)]

    print(f"Il ne vous reste plus que {marbles} bille(s) !")
    print(f"Vous rencontrez {adversaire['name']} ! Selon vous, ses billes sont-elles paires(p) ou impaires(i) ?")

    reponse = input("> ")

    # On récupère le nombre de billes de l'adversaire et on le met dans la variable 'adversaire_paire_billes'
    adversaire_billes = adversaire["marbles"]

    # On vérifie si le nombre est pair avec un modulo
    adversaire_paire = (adversaire_billes % 2 == 0)

    # On met reponse_paire (réponse du joueur en tant que booléen)
    reponse_paire = (reponse == "p")

    # On affiche le choix du joueur
    if reponse_paire:
        print("\nVous avez choisi paire")
    else:
        print("\nVous avez choisi impaire")

    if reponse_paire == adversaire_paire:
        print(f"Vous avez gagné ! Vous récuperez {adversaire_billes + gain} bille(s)\n")
        marbles += (adversaire_billes + gain)
        #Au cas où, on peut enlever les billes de l'adversaire
        adversaires = list(adversaires)
        adversaires.remove(adversaire)
        adversaires = tuple(adversaires)
    else:
        print(f"Vous avez perdu ! Vous perdez {adversaire_billes - gain} bille(s)\n")
        marbles -= (adversaire_billes + loss)

    print("")

    # Si a la fin de la partie le joueur n'a plus de billes, on dit qu'il a perdu
    # puis on break la boucle (on sors)
    if marbles < 1:
        print("\nVous avez perdu ! Vous n'avez plus de billes\n")
        break

# Si en sortant de la partie le joueur à au moins une bille,
# Il a gagné !
if marbles >= 1:
    print("\nVous avez gagné (il vous reste au moins 1 bille) n")