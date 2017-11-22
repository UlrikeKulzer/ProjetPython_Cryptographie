    def create: #fill lists



    def format(text): # in Main -> run-Funktion in Main aufrufen (1 Zeile)



    def encrypt(text): # raus damit



    def decrypt(text): # das auch



    def encrypt_caesar(text, key):
        crypted_text = ''  # chaine vide dans laquelle on va ajouter au fur et à mesure le texte crypté
        for i in text:
            if ord(i) + key > 90:  # si en ajoutant la clé au numéro de la lettre on dépasse le numéro de Z on doit revenir au début de l'alphabet
                i = chr(ord('A') - 1 + (key - (ord('Z') - ord(i))))
                crypted_text += i
            else:  # sinon on opère de manière normale
                i = chr(ord(i) + key)
                crypted_text += i
        return crypted_text

    def decrypt_caesar(text, key):
        decrypted_text=''       #chaine vide dans laquelle on va ajouter au fur et à mesure le texte décrypté
        for i in text:
            if ord(i)-key<65:  #si en soustrayant la clé au numéro de la lettre on trouve un numéro inférieur à celui de A on doit repartir à la fin de l'alphabet
                i=chr(ord('Z')+1-(key-(ord(i)-ord('A'))))
                decrypted_text+=i
            else:
                i=chr(ord(i)-key)
                decrypted_text+=i
        return decrypted_text


    def encrypt_vigenere(text, key):
        vigenere_table = [][]


    def decrypt_vigenere(text, key):
        vigenere_table = [][]


    def encrypt_enigma(text, key):
        return_path = False
        initial_list = []
        first_rotor = []
        second_rotor = []
        third_rotor = []


    def decrypt_enigma(text, key):
        return_path = False
        initial_list = []
        first_rotor = []
        second_rotor = []
        third_rotor = []





# ENIGMA

    def search_index(letter, alphabeth):

    def plugboard(letter):

    def shift_first_rotor(letter):

    def shift_second_rotor(letter):

    def shift_third_rotor(letter):

    def permutation_reflector(letter):




