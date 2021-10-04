hash()
    salt : secret
    maxlengh: 10


lancer un webserver:
    Si POST:
        URL = 
        hash = hash(URL)
        stocker le duo hash:URL
        retourner domain.tld/$hash, code 200
    Si GET:
        chercher l'URL
        retourner $URL, code 200
        (rediriger vers l'url ?)
    Sinon:
        Erreur 404
 
