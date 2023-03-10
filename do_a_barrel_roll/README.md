# Groupe de debbah_a 997943

 La fonction prend en entrée deux arguments: "numbers", qui est une liste d'entiers, et "k", qui est un entier. La fonction retourne également une liste d'entiers.

La longueur de la liste "numbers" est déterminée avec "n = len(numbers)". "k % = n" signifie que "k" sera égal au reste de la division de "k" par "n".

Si "k" est égal à 0 ou n est égal a 0, la fonction retourne la liste "numbers" telle quelle. 
Si "k" est égal à 1, la fonction retourne la liste "numbers" avec le premier élément déplacé à la fin.
Si "k" est égal à 2, la fonction retourne la liste "numbers" avec les deux premiers éléments déplacés à la fin.
Ainsi de suite...



Mais est ce que cette contrainte est respecté : 
Est ce que notre solution a une complexité en temps de O(n), où n est la longueur du tableau reçu ? 

Oui, cette fonction respecte la contrainte d'avoir une complexité en temps de O(n). Les seules opérations effectuées sur la liste "numbers" sont de trouver la longueur de la liste avec "len(numbers)", de trouver un sous-liste avec "numbers[k:]" et "numbers[:k]", et de les concaténer avec l'opérateur "+". Toutes ces opérations ont une complexité en temps constant, donc la complexité totale de la fonction est de O(n).


