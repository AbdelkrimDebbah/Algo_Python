Notre code commence par définir une fonction appelée roger_rabbit qui prend en paramètre un entier naturel et retourne un tableau de chaînes de caractères.
La fonction itère ensuite sur les nombres de 1 à n inclus, génère chaque nombre en binaire et l'ajoute à la liste des résultats.

Enfin, la fonction retourne le tableau des résultats.


Pour répondre a l'exercice, nous avons réaliser un algorithme en utilisons une approche de fil d'attente pour générer les représentations binaires. À chaque itération, le premier élément de la file est retiré et utilisé pour générer les représentations binaires du prochain nombre en ajoutant "0" ou "1" à la fin. Le nouveau nombre est alors ajouté a la file.


Le temps de complexité de cet algorithme est en O(n).
Pourquoi ? 


La complexité en temps d'un algorithme dépend du nombre d'opérations que l'algorithme effectue en fonction de la taille de ses entrées. La notation O(n) indique que le temps d'exécution de l'algorithme est proportionnel à n, où n est la taille de l'entrée.

Dans notre algorithme, la boucle for itère n fois, et à chaque itération, elle effectue une série d'opérations fixes qui incluent la suppression d'un élément du file, l'ajout de deux éléments au file, et la mise à jour de la liste result.

Par conséquent, le nombre total d'opérations effectuées par l'algorithme est proportionnel à n, ce qui signifie que le temps d'exécution de l'algorithme est en O(n). En d'autres termes, le temps d'exécution de l'algorithme augmente de manière linéaire avec la taille de l'entrée.

En conclusion : 
Premièrement, notre code ne procède pas par convertion d'une base vers une autre. 

Deuxièmement, notre algorithme a bien une complexité temps en O(n), où n correspond au paramètre reçu.

Nous respectons bien les 2 contraintes demandées. 