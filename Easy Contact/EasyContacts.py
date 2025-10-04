import json
class Person:
    def __init__(self, nom, prenom, numero, email, adresse):
        self.nom = nom
        self.prenom = prenom
        self.numero = numero
        self.email = email
        self.adresse = adresse
    def __str__(self):
        return f" Il s'appelle {self.nom} {self.prenom} \n Son numéro de téléphone est {self.numero} \n Il habite a {self.adresse} \n Son email est {self.email}"
    def to_dict(self):
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "numero": self.numero,
            "email": self.email,
            "adresse": self.adresse
        }


while True:
    print(
        "--- Menu --- \n"
        "1: Ajouter un nouveau contact \n" 
        "2: Supprimer un contact existant \n"
        "3: Rechercher un contact par nom ou numéro \n"
        "4: Quitter")
    option = input("Choisir un option: ")

    if option == "1":
        print("--- Ajouter un nouveau contact ---")
        information = Person(
            nom =  input("Ton Nom: "),
            prenom = input("Ton Prenom: "),
            numero = input("Ton numero: "),
            email = input("Ton email: "),
            adresse = input("Ton adresse: "))
        print("Les informations ont était enregistré")
        contact_dict = information.to_dict()
        try:
            with open("contacts.json", "r") as f:
                    contacts = json.load(f)
        except FileNotFoundError:
                contacts = []
        except json.JSONDecodeError:
                contacts = []
        contacts.append(information.to_dict())
        with open("contacts.json", "w") as f:
            json.dump(contact_dict, f, indent=4)
    elif option == "2":
        print("--- Supprimer un contact existant ---")
        
        break
    elif option == "3":
        print("---  Rechercher un contact par nom ou numéro ---")
        break
    elif option == "4":
        print("Au revoir 👋")
        break
    else:
        print("Ce n'est pas une option")



