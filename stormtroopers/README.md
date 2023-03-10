# Groupe de debbah_a 997943

On utilise un dictionnaire pour stocker chaque nombre dans la liste d'origine avec une valeur de 1, et incrémente sa valeur dans ce dictionnaire chaque fois qu'il apparaît à nouveau. En fin de boucle, Cette étape prend O(n) temps, car on passe en revue toutes les entrées du dictionnaire. la fonction retourne une nouvelle liste de key (c'est-à-dire de nombres) qui n'ont qu'une valeur dans le dictionnaire.

En termes de complexité, le temps d'exécution est bien de O(n)

Pourquoi ?

 Car nous parcourons bien une seule fois la liste originale et nous utilisons un dictionnaire pour stocker les valeurs. 
 La caracteristique de l'ajout et la recherche dans un dictionnaire en python ont une complexité en temps de O(1) en moyenne, on a une complexité dans le temps en fonction de la taille du tableau.
 
 Pourquoi O(1) ?

La caractéristique de hachage (structure de données qui permet de stocker des paires clé-valeur de manière efficace et rapide) donne une complexité en temps d'accès constante moyenne, ce qui signifie que la complexité en temps pour ajouter ou trouver une valeur à partir d'une clé est en général O(1).


La durée d'exécution de l'algorithme augmente linéairement avec la taille de l'entrée.
 On peux rajouter également que la complexité en espace est de O(n) car on utilise un dictionnaire pour stocker les valeurs.

 => En conclusion dans notre cas nous avons bien une complexité en temps de O(n) lorsque l'on utilise des dictionnaires en python.





 