La fonction morning_sunshine prend en entrée une liste d'entiers, ici numbers. Elle renvoie une liste d'entiers.

result = [] : Nous déclarons un tableau vide qui sera utilisé pour stocker les résultats.
max_value = float("-inf") : Nous définissons une valeur maximale initiale très basse pour pouvoir comparer avec les éléments du tableau.
for i in range(len(numbers) - 1, -1, -1) : Avec la fonction range() nous parcourons le tableau en commençant par la fin (avant derniére valeur plus précisement ici) pour pouvoir traiter les éléments de manière efficace. Nous nous arrétons a la première valeur du tableau.
Nous devons parcourir le tableau à l'envers (d'ou step -1)pour pouvoir comparer les éléments avec la valeur maximale actuelle. 

Si nous parcourions le tableau de gauche à droite, nous ne pourrions pas comparer les éléments avec la valeur maximale actuelle car nous n'aurions pas encore parcouru tous les éléments du tableau.
if numbers[i] > max_value : Si le nombre actuel est strictement supérieur à la valeur maximale actuelle, nous le stockons dans le tableau result et définissons la nouvelle valeur maximale.
return result[::-1] : Enfin, nous renvoyons le tableau result renversé.

Le code a une complexité en temps de O(n) : 

Pourquoi ?

La complexité en temps est le nombre d'opérations effectuées par l'algorithme pour exécuter le code en fonction de la taille de l'entrée (le nombre d'opérations effectuées par l'algorithme sera proportionnel à la taille du tableau, donc plus le tableau est grand, plus le nombre d'opérations sera élevé). Dans ce cas, la taille de l'entrée est la longueur du tableau 'numbers', qui est représentée par la variable 'n'.

Il n'a qu'un seul passage sur le tableau d'entrée 'numbers'. La complexité de notre code est O(n) car nous parcourons chaque élément du tableau qu'une seule fois pour déterminer les valeurs à retourner.



