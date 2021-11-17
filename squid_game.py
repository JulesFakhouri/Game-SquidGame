# On importes la librairie random
from random import *

# On définit les niveaux dans un dictionnaire :
# Le premier "argument" désnigne la difficulté du niveau, puis
# dans celui-ci nous mettons le nombre de niveau.
niveaux = {
    "facile": 5,
    "difficile": 12,
    "impossible": 20,
}

# On définit les personnages :
# les parenthèses délimitent le tuples
# celui-ci permet d'avoir à peu près le même effet qu'un tableau,
# on peut contenir des éléments dedans, en l'occurrence un dictionnaire:
# le nom, le nombre de billes(marbles), le loss, et le gain.
personnages = (
    {
        "name": "Seong Gi-hun",
        "marbles": 25,
        "loss": 3,
        "gain": 1
    },

    {
        "name": "Kang Sae-Byeok",
        "loss": 2,
        "gain": 2
    },

    {
        "name": "Cho Sang-Woo",
        "loss": 1,
        "gain": 3
    }
)

# On définit le tuple adversaire
adversaires = ()

# Ensuite, dynamiquement on y a ajouté des adversaires:
# 'marbles' : le nombre de billes qu'il possède avec randrange(1, 20) pour
# un integer (donc nombre sans virgule) entre 1 et 20
# On met manuellement les adversaires:
adversaires = (
    {
        "name": "Borislav Iared",
        "marbles": randrange(1, 20)
    },
    {
        "name": "Daisy-Mae Dalby",
        "marbles": randrange(1, 20)
    },
    {
        "name": "Clodagh Carlson",
        "marbles": randrange(1, 20)
    },
    {
        "name": "Genevieve Vincent",
        "marbles": randrange(1, 20)
    },
    {
        "name": "Isabella Lutz",
        "marbles": randrange(1, 20)
    },
    {
        "name": "Colby Greene",
        "marbles": randrange(1, 20)
    },
    {
        "name": "Nakita Woodard",
        "marbles": randrange(1, 20)
    },
    {
        "name": "Curtis Maxwell",
        "marbles": randrange(1, 20)
    },
    {
        "name": "Lochlan Ramsey",
        "marbles": randrange(1, 20)
    },
    {
        "name": "Bea Horn",
        "marbles": randrange(1, 20)
    },
    {
        "name": "Linda John",
        "marbles": randrange(1, 20)
    },
    {
        "name": "Martyna Goddard",
        "marbles": randrange(1, 20)
    },
    {
        "name": "Tehya Blackmore",
        "marbles": randrange(1, 20)
    },
    {
        "name": "Roxy Jackson",
        "marbles": randrange(1, 20)
    },
    {
        "name": "Sanah Hunt",
        "marbles": randrange(1, 20)
    },
    {
        "name": "Aamina Sharples",
        "marbles": randrange(1, 20)
    },
    {
        "name": "Nishat Leach",
        "marbles": randrange(1, 20)
    },
    {
        "name": "Tala Farrington",
        "marbles": randrange(1, 20)
    },
    {
        "name": "Anisa Gamble",
        "marbles": randrange(1, 20)
    },
    {
        "name": "Eva Feeney",
        "marbles": randrange(1, 20)
    },
)

print("--- Choisissez votre niveau ---\n")

# On demande à l'utilisateur de choisir son niveau et on l'inscrit
# Dans la variable "choix niveaux" (pour être utilisée plus tard).
choix_niveau = input("\nVeuillez choisir votre difficulté (facile/difficile/impossible) > ")

# On instancie la variable "nombre de niveaux" à 0 (pour commencer)
# Puis, en fonction de son choix, adapter sa vauleur.
nombre_de_niveaux = 0

# Le niveau['facile'] (par exemple) sert à récuperer la valeur, en l'occurence 5
if choix_niveau == "facile": nombre_de_niveaux = niveaux["facile"]
if choix_niveau == "difficile": nombre_de_niveaux = niveaux["difficile"]
if choix_niveau == "impossible": nombre_de_niveaux = niveaux["impossible"]

print("")

# On itère un tuple avec la fonction enumerate()
# Puis, pour chaque valeur (un personnage) on récupère son nom:
# Key[1] signifie que l'on récupère le dictionnaire (ça fonctionne comme ça en tuple)
# key[0] est l'index (ça va nous servir pour séléctionner le personnage !)
for key in enumerate(personnages):
    print(f"{key[0]} - {key[1]['name']}")

# On demande le choix du personnage sous forme d'int !
choix_personnage = int(input("\nVeuillez choisir votre personnage > "))
caracteristiques_personnage = personnages[0]
nom = caracteristiques_personnage["name"]
marbles = caracteristiques_personnage["marbles"]
loss = caracteristiques_personnage["loss"]
gain = caracteristiques_personnage["gain"]

print("")

# On démarre !
for i in range(nombre_de_niveaux):

    # On prend l'adversaire aléatoire avec le randrange
    # Entre 1 et 19 (car ça commence à 0)
    adversaire = adversaires[randrange(1, 19)]

    print(f"Il ne vous reste plus que {marbles} bille(s) !")
    print(f"Vous rencontrez {adversaire['name']} ! Selon vous, ses billes sont-elles paires(p) ou impaires(i) ?")

    reponse = input("> ")

    # On récupère le nombre de billes de l'adversaire et on le met dans la variable "adversaire paire billes
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
        # Au cas où, on peut enlever les billes de l'adversaire
        adversaires = list(adversaires)
        adversaires.remove(adversaire)
        adversaires = tuple(adversaires)
    else:
        print(f"Vous avez perdu ! Vous perdez {adversaire_billes - gain} bille(s)\n")
        marbles -= (adversaire_billes + loss)

    print("")

    # Si à la fin de la partie le joueur n'a plus de billes, on dit qu'il a perdu
    # Puis on break la boucle
    if marbles < 1:
        print("\nVous avez perdu dommage ! Vous n'avez plus de billes\n")
        break

# Si en sortant de la partie le joueur à au moins une bille,
# Il a gagné !
if marbles >= 1:
    print("\nVous avez gagné (il vous reste au moins 1 bille) n")