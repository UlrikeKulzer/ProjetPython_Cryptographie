    def create: #fill lists




    def encrypt_caesar(text, key):
        crypted_text = ''
        for i in text:
            if ord(i) + key > 90:
                i = chr(ord('A') - 1 + (key - (ord('Z') - ord(i))))
                crypted_text += i
            else:
                i = chr(ord(i) + key)
                crypted_text += i
        return crypted_text

    def decrypt_caesar(text, key):
        decrypted_text=''
        for i in text:
            if ord(i)-key<65:
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




