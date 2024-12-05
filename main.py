"""C'est l'exo
Import : Augmentation de la limite d'appels
"""
import sys
sys.setrecursionlimit(5000)

def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return [ ]
    chars = [s[0]] # Liste des caractères rencontrés
    occurrences = [1]# Liste des occurrences correspondantes
    k = 1  # Indice pour parcourir la chaîne

    # Parcours de la chaîne
    while k < len(s):
        if s[k] == s[k - 1]:  # Même caractère que le précédent
            occurrences[-1] += 1
        else:  # Nouveau caractère
            chars.append(s[k])
            occurrences.append(1)
        k += 1

    # Combiner les caractères et leurs occurrences en tuples
    return list(zip(chars, occurrences))



def artcode_r(s):
    """Encode une chaîne de caractères en liste de tuples 
    (caractère, occurrences) avec un algorithme récursif.

    Args:
        s (str): La chaîne de caractères à encoder.

    Returns:
        list[tuple]: La liste des tuples correspondant au codage.
    """
    # Cas de base : chaîne vide
    if not s:
        return []

    # Identifier le premier caractère et compter ses occurrences consécutives
    first_char = s[0]
    count = 1
    while count < len(s) and s[count] == first_char:
        count += 1

    # Construire la liste des résultats
    result = [(first_char, count)]

    # Appel récursif sur la sous-chaîne restante
    # Réduire de manière explicite pour éviter des erreurs
    rest_of_string = s[count:]

    # Si la chaîne restante est non vide, appeler récursivement
    return result + artcode_r(rest_of_string)



def main():
    """ La fonction main"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
