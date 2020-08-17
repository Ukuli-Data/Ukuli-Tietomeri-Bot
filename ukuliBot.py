class User:
    def __init__(self, name, userid):
        self.name = name
        self.userid = userid

entities = ["tietomeri", "ukuli", "iota", "arduino", "rasp"]
intents = ["tila", "osta", "mite", "toimi"]

tietomeri = {
  "name" : "Tietomeri",
  "desc" : "Tietomeri on alusta IoT-projekteille."
}

ukuli = {
  "name" : "Ukuli Data",
  "desc" : "Ukuli Data on uusi ja innokas ohjelmistoyritys."
}

iota = {
  "name" : "IOTA",
  "desc" : "IOTA on IoT-laitteita varten suunniteltu kryptovaluutta."
}

arduino = {
  "name" : "Arduino",
  "desc" : "Arduino on suosittu avoimen lähdekoodin mikrokontrolleri."
}

rasp = {
  "name" : "Raspberry Pi",
  "desc" : "Raspberry Pi on pieni tietokone joka on suosittu IoT-projekteissa."
}


entityDictionaries = {
  "tietomeri" : tietomeri,
  "ukuli" : ukuli,
  "iota" : iota,
  "arduino" : arduino,
  "rasp" : rasp,
}
