import re
import hashlib

while True:
    motdepasse = input("Entrez votre mot de passe : ")

    
    if len(motdepasse) < 8:
        print("Le mot de passe doit contenir au moins 8 caractères.")
    
    elif not re.search("[a-z]", motdepasse):
        print("Le mot de passe doit contenir au moins une lettre minuscule.")
    
    elif not re.search("[A-Z]", motdepasse):
        print("Le mot de passe doit contenir au moins une lettre majuscule.")
    
    elif not re.search("[0-9]", motdepasse):
        print("Le mot de passe doit contenir au moins un chiffre.")
    
    elif not re.search("[!@#$%^&*]", motdepasse):
        print("Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
    
    else:
        hash_object = hashlib.sha256(motdepasse.encode())
        print("Le mot de passe est sécurisé et crypté :", hash_object.hexdigest())
        break