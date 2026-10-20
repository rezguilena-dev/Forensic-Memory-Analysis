import argparse
import json
import sys

#Je charge le fichier 
def charger(chemin):
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        sys.exit(f"Erreur : fichier introuvable : {chemin}")
    except json.JSONDecodeError as e:
        sys.exit(f"Erreur : JSON invalide : {e}")

# Assure qu'on  est bien dans les marges
def court(valeur, largeur):
    if isinstance(valeur, (list, dict)):
        valeur = json.dumps(valeur, ensure_ascii=False)
    texte = str(valeur)
    return texte if len(texte) <= largeur else texte[: largeur - 1] + "…"


def afficher_tableau(lignes, largeur_max=60):
    # toutes les colonnes présentes, dans l'ordre d'apparition
    colonnes = []
    for ligne in lignes:
        for cle in ligne:
            if cle not in colonnes:
                colonnes.append(cle)

    # largeur de chaque colonne = plus long contenu (limité à largeur_max)
    largeurs = {
        c: min(largeur_max, max(len(c), *(len(court(l.get(c, ""), largeur_max)) for l in lignes)))
        for c in colonnes
    }

    entete = " | ".join(c.ljust(largeurs[c]) for c in colonnes)
    print(entete)
    print("-+-".join("-" * largeurs[c] for c in colonnes))

    for ligne in lignes:
        print(" | ".join(court(ligne.get(c, ""), largeur_max).ljust(largeurs[c]) for c in colonnes))
#Recursif sur les noeuds de l'arbre 
def aplatir(noeuds, niveau=0):
    for n in noeuds:
        ligne = {k: v for k, v in n.items() if k != "__children"}
        ligne["COMM"] = "  " * niveau + str(ligne.get("COMM", ""))
        yield ligne
        yield from aplatir(n.get("__children", []), niveau + 1)
def main():
    parser = argparse.ArgumentParser(description="Affichage du JSON")
    parser.add_argument("fichier")
    args = parser.parse_args()

    data = charger(args.fichier)
    if isinstance(data, dict):
        data = [data]
    
    data = list(aplatir(data))
    print(f"\n{args.fichier} : {len(data)} entrées\n")
    afficher_tableau(data)


if __name__ == "__main__":
    main()