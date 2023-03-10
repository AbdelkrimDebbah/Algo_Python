Notre code vérifie si une chaîne donnée contient des paires correctement imbriquées de caractères de parenthèses, de crochets ou de guillemets.
Nous n'avons pas spécifier le cas pour les accolades, car en exemple cela n'est pas specifié.

On déclare une variable stack qui sera utilisée pour stocker les caractères ouvrants trouvés dans la chaîne.
DOn déclare également deux listes open_chars et close_chars qui contiennent les caractères d'ouverture et de fermeture correspondants.

Nous initialisons les compteurs count_simple_quote et count_double_quote à 0.
NOUS Itérons sur chaque caractère dans la chaîne s.
--> Si le caractère actuel est une apostrophe simple, alors on incrémente count_simple_quote de 1.
--> Si le caractère actuel est un guillemet double, dans ce cas la on incrémente count_double_quote de 1.

--> Si le caractère actuel est dans la liste open_chars, nous ajoutons le caractère à la pile.

--> Sinon, si le caractère actuel est dans close_chars, nous vérifions si la pile est vide. Si c'est le cas, retourner False, car il n'y a pas de caractère ouvrant correspondant pour ce caractère fermant. 
Sinon, on vérifie si le caractère fermant correspond à celui sur le dessus de la pile. Si ce n'est pas le cas, retourner False.

Retourner True si la longueur de la pile est un multiple de 2 et que les compteurs count_simple_quote et count_double_quote sont également des multiples de 2.

Est-ce que la complexité temporelle est respectée ?

Oui car chaque caractère de la chaîne est visité une seule fois, donc la complexité est de O(n), ce qui répond à la contrainte.
la complexité totale de la fonction est directement proportionnelle à la longueur de la chaîne de caractères s, ce qui correspond à une complexité en temps de O(n)