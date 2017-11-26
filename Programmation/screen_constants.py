"""
This module contains all screen constants, i. e. all texts of the user interface.
"""

# constants for both languages
START_ASK_LANGUAGE = "Hello. Welcome to the cryptography program.\nPlease select your language:\n'f' for Francais, 'e' for English."
LANGUAGE_SETTINGS = "Please select your language:\n'f' for Francais, 'e' for English."

# English user interface


ENGLISH_MAIN_MENU = "What do you want to do-encrypt or decrypt a message?\nEnter c for encrypting or d for decrypting.\nEnter s to change settings(language)\nor q to exit:("
ENGLISH_PRINCIPLES = ""
ENGLISH_ASK_KEY_CAESAR = ""
ENGLISH_ASK_KEY_VIGENERE = ""
ENGLISH_ASK_KEY_ENIGMA = ""
ENGLISH_ASK_TEXT = ""
ENGLISH_TREATED_TEXT = ""
ENGLISH_HELP_PRINCIPLES = "THIS TEXT IS STILL MISSING"
ENGLISH_QUIT_MESSAGE = "Thank you for using our program.\nGood bye and have a nice day."

# French user interface
FRENCH_MAIN_MENU = "Bonjour.Bienvenue sur le programme de cryptographie.\nQue voulez vous faire-crypter ou décrypter un message?\nInsérez c pour crypter ou d pour décrypter.\nInsérez s pour changer les paramètres(langue)\nou q pour quitter le programme:("
FRENCH_PRINCIPLES = ""
FRENCH_ASK_KEY_CAESAR = ""
FRENCH_ASK_KEY_VIGENERE = ""
FRENCH_ASK_KEY_ENIGMA = ""
FRENCH_ASK_TEXT = ""
FRENCH_TREATED_TEXT = ""
FRENCH_HELP_PRINCIPLES = "************** AIDE **************\n\nVoici les explications pour les différents principes de (dé)cryptage.\n\n- Le chiffre de César :\nCe procédé a été inventé lors de l'époque romaine par Jules César pour ses communications secrètes. En décalant l'alphabet par un entier donné chaque lettre est associée à une nouvelle lettre, ainsi on peut crypter le message initiale en remplaçant chaque lettre par la nouvelle lettre attribuée.\n\n- Le chiffre de Vigenère :\nIl a été inventé au 16e siècle par Blaise de Vigenère et est basé sur le tableau de Vigenère (tableau avec deux fois l'alphabetg). Une clé (un mot) est répétée et mis sous le message et de cette manière on peut trouver les lettres correspondantes à partir du tableau.\n\n- Le principe de la machine Enigma :\nL’Enigma est une machine de cryptographie inventée par Arthur Scherbius en 1919. Elle a été utilisée durant la Seconde Guerre mondiale pour la communication secrète entre les différentes unités de l’armée allemande.\nLa machine est constituée de cinq rotors dont un réflecteur, d’un clavier, d’un tableau de permutation et de lampes pour chaque lettre. Pour l’allumer il faut une batterie de 4,5 Volt.\nLe principe est simple : Lorsqu’on appuie sur une lettre du clavier, un courant électrique va être envoyé au tableau de permutation dans lequel la lettre entrée est échangée avec une autre lettre si elles sont connectées. Puis il passera la première fois par les quatre rotors : Dans chacun des trois rotors au milieu il y a un décalage des lettres qui s’opère. À la fin les lettres sont permutées encore une fois dans le réflecteur qui les renvoie par les rotors au tableau de permutation ce qui permettra à une lampe correspondant à une lettre de s’allumer. Ainsi pour chaque lettre on relève la lettre codée, on obtient alors notre message crypté.\n\nInsérez 'm' pour retourner au menu principal."
FRENCH_QUIT_MESSAGE = "Merci d'avoir utilisé notre programme.\nBonne journée, au revoir."
