# oracleSQL
pour PFGimenez/poirot
## Deux commandes
### init
Initialisation de la cible (variable globale) pour éviter de faire plusieurs fois des fonctions coûteuse (e.g. get_default_average_time)
#### GET
```
[Bientôt] python sqloracl.py init ([url](string), optional [avgnb](int))
```
#### POST
```
[Bientôt] python sqloracl.py init ([url](string), [payload](dict), [param](string), optional [avgnb](int))
```
### oracle
retourne 0 si la chaine de caractère est syntaxiquement valide, 1 sinon
 
```
[Bientôt] python sqloracl.py oracle ([injtxt](string))
``` 
