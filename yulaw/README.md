# Groupe de debbah_a 997943

Notre code définit une fonction yulaw qui prend en entrée une chaîne de caractères s et renvoie une nouvelle chaîne de caractères.

La fonction yulaw commence par initialiser un dictionnaire vide.
Une boucle for est utilisée pour itérer sur les caractères de la chaîne d'entrée s.

Pour chaque caractère, une condition if vérifie si ce caractère existe déjà dans le dictionnaire char_count.

Si oui, le compteur associé à ce caractère dans le dictionnaire est incrémenté.
Si non, le compteur est initialisé à 1 et le caractère est ajouté à la liste result.
Après la boucle, la méthode join est appelée sur la chaîne vide avec la liste result en argument 
pour construire la chaîne de sortie.

En ce qui concerne la complexité temporelle, elle est en O(n), où n est la longueur de la chaîne d'entrée, ici  s. 

Pourquoi ?
Parce que la boucle for est exécutée n fois, où n est la longueur de la chaîne d'entrée.
car chaque caractère de la chaîne est examiné une seule fois dans la boucle for, ce qui prend O(n) temps.
Les opérations de lecture et d'écriture sur le dictionnaire char_count prennent également O(1) temps en moyenne, 
de sorte que la fonction yulaw en entier a une complexité temporelle totale de O(n).
De plus, la complexité temporelle de la méthode join est O(n), où n est la longueur de la liste en argument.
