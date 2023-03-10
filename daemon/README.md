# Groupe de debbah_a 997943

Je déclare une fonction avec comme paramètre un tableau de nombre partitionné avec un pivot k.

Je crée une premiére boucle qui vérifie que les chiffres avant le pivot sont strictement inférieure a ce pivot, dans le cas contraire la réponse est false.
Par la suite je fais une autre boucle qui vérifie que les chiffres aprés ce pivot sont supérieurs a ce pivot, et dans le cas contraire également cela retourne false.

Sinon ca retourne true.

les différentes contraintes sont respectées : 
- On définit bien une fonction nommé daemon avec une liste d'entier numbers comme entrée , et un entier k comme pivot.
- la fonction retourne bien false ou true c'est a dire un boolean par raport aux contraintes exigées, du coup k est bien un pivot puisque qu'il respecte les 2 conditions


Concernant la complexité en temps du code : 
on remarque que le code réalisé itére à deux reprise par rapport au pivot ( c'est a dire l'index k) pour vérifier les conditions requises cité précedemment, : une fois avant et une fois aprés.

En therme de complexité voici ce qu'on peux rajouter en plus  : l'algorithme choisi satisfait les contraintes du sujet, en terme de complexité. : 

Pourquoi ?

Parce que l'algorithme utilise deux boucles pour parcourir les éléments du tableau, ce qui donne une complexité en temps de O(n), où n est la taille du tableau. Ca signifie que la performance de l'algorithme dépend linéairement de la taille du tableau. Cette complexité est raisonnable pour des tailles de tableau relativement petites, mais pour des tailles très grandes, on peux rencontrer des problèmes de performance.

Avec cette algorithme il n'est pas nécessaire de trier le tableau avant de vérifier les conditions, du coup c'est efficace en termes de complexité pour des petits et moyens tableaux.

Dans notre cas il s'agit de petits tableaux, donc cela satifait bien les contraintes du sujet en terme de complexité. 