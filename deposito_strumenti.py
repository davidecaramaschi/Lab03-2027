class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = []
        self.prestiti = []
        self.contatore_prestiti = 0

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        try:
            with open(file_path, 'r') as file:
                for riga in file:
                    parti = riga.strip().split(',')
                    s1 = Strumento(parti[0], parti[1], parti[2], int(parti[3]), float(parti[4]))
                    self.strumenti.append(s1)

        except FileNotFoundError:
            raise FileNotFoundError("File non trovato")

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        if len(self.strumenti) == 0:
            codice_nuovo = 'S1'
        else:
            ultimo_strumento = self.strumenti[-1]
            ultimo_codice = ultimo_strumento.codice
            numero = int(ultimo_codice[1:])
            codice_nuovo = 'S' + str(numero + 1)

        strumento_finale = Strumento(codice_nuovo, tipo, marca, anno_acquisto, valore)
        self.strumenti.append(strumento_finale)

        return strumento_finale

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        return sorted(self.strumenti, key=lambda strumento: strumento.marca)

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO
        trovato = False

        for f in self.strumenti:
            if f.codice == id_strumento:
                trovato = True
                break

        if not trovato:
            raise ValueError("Strumento non esistente")

        for d in self.prestiti:
            if d.id_strumento == id_strumento:
                raise ValueError("Strumento già in prestito")

        self.contatore_prestiti += 1
        codice_nuovo = 'P' + str(self.contatore_prestiti)

        prestito_finale = Prestito(codice_nuovo,data, id_strumento, cognome_allievo)
        self.prestiti.append(prestito_finale)

        return prestito_finale

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        for f in self.prestiti:
            if f.codice == id_prestito:
                self.prestiti.remove(f)
                return

        raise ValueError("Prestito non esistente")

class Strumento:
    def __init__(self, codice,tipo, marca, anno_acquisto, valore):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore

    def __str__(self):
        return f'{self.codice} {self.tipo} {self.marca} {self.anno_acquisto} {self.valore}'

class Prestito:
    def __init__(self, codice, data, id_strumento, cognome_allievo):
        self.codice = codice
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        return f'{self.codice} {self.data} {self.id_strumento} {self.cognome_allievo}'