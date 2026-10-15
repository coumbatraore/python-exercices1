
ventes = [
    {"produit": "café", "prix": 2.5, "quantite": 120},
    {"produit": "thé", "prix": 2.0, "quantite": 80},
    {"produit": "jus", "prix": 3.5, "quantite": 45},
]

ca_par_produit = {}
for vente in ventes:
    nom = vente["produit"]
    ca_par_produit[nom] = vente["quantite"] * vente["prix"]

print( ca_par_produit)


total = sum(ca_par_produit.value())
print(f"Total : {total:.2f} euros")

meilleur_produit = ""
meilleur_ca = 0
for nom, ca in ca_par_produit.items():
    if ca > meilleur_ca:
        meilleur_ca = ca
        meilleur_produit = nom 
print(f"Meilleur produit : {meilleur_produit}")
