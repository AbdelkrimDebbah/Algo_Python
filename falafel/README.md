# Groupe de debbah_a 997943

Je déclare une fonction nommée falafel qui prend une string en parametre et attend un type de retour de type bool (true ou false)

1 - Je crée une liste avec 128 entrée initialisé a 0, pour stocker le nombre d'occurence de chaque caractére ASCII.
Avec sa je crée une variable qui commence a 0. Cette variable sera utilisée pour compter le nombre de caractères ayant un nombre impair d'occurrences dans la chaîne d'entrée.

2 - Je crée une premiére boucle qui va parcourir tout les caractere de la string.
Pour chaque caractére je vais incrémenter la valeur de la liste à l'index correspondant au code ASCII du caractére.

Si le nombre d'occurrences de ce caractère est impaire j'incrémentez la variable de 1. Sinon je décrémente la variable de 1.


3 - Après la boucle for je vérifie si le nombre de caractères ayant un nombre impair d'occurrences dans la chaîne d'entrée est inférieur ou égal à 1. Si c'est le cas, ca voudras dire qu'il est possible de permuter les caracteres de la chaine pour avoir un palindrome donc je renvoie bien True sinonn je renvoie False.

Les différentes contraintes sont respectées :
- On définit bien une fonction nommé falafel avec une string en parametre et qui retourne bien un booléen.

Concernant la complexité en temps du code : 
Ont remarque que la complexité en temps de ce code est de O(n), où n est la longueur de la chaîne en entrée. Cela signifie que la quantité de temps nécessaire pour exécuter le code augmente linéairement avec la taille de la chaîne

L'algorithme choisi satisfait les contraintes du sujet, en terme de complexité, pourquoi ? : 
Tout simplement 

En therme de complexité voici ce qu'on peux rajouter en plus  : l'algorithme choisi satisfait les contraintes du sujet, en terme de complexité. :

Pourquoi ?

Cet algorithme utilise une boucle pour parcourir la chaîne en entrée et maintient un tableau de comptage de caractères de taille constante, ce qui signifie que la complexité en temps est linéaire en fonction de la longueur de la chaîne, soit O(n). 
Cela signifie que la quantité de temps nécessaire pour exécuter le code augmente de manière proportionnelle à la longueur de la chaîne, ce qui en fait un choix efficace en termes de complexité pour résoudre le problème.

J'ai utilisé cet algo car il est simple et efficace. Il est simple car il n'y a pas de boucle imbriquée et il est efficace car il utilise une boucle for pour parcourir la chaîne en entrée et maintient un tableau de comptage de caractères de taille constante, ce qui signifie que la complexité en temps est linéaire en fonction de la longueur de la chaîne, soit O(n).