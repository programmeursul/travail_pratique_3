# -*- coding: utf-8 -*-
"""
Module contenant la description de la classe Partie qui permet de jouer une partie du jeu démineur.
Dois être démarré en appelant la méthode jouer(). Cette classe contient les informations sur une partie et
utilise un objet tableau_mines (une instance de la classe Tableau).

Auteurs: à compléter
"""

from tableau import Tableau

class Partie():
    """
    Contient les informations sur une partie du jeu Démineur, qui se jouera avec
    un tableau de mines. Des méthodes sont disponibles pour faire avancer la partie 
    et interagir avec l'utilisateur.

    Attributes:
        tableau_mines (Tableau): Le tableau de cases où les mines sont cachées avec lequel se
                déroule la partie.
        partie_terminee (bool): True lorsque l'utilisateur a terminé de jouer la partie (victoire ou défaite)
    """

    def __init__(self):
        """
        Initialisation de la Partie. 
        
        Note: L'instance de la classe Tableau, qui sera manipulée par les méthodes de la classe,
              sera initialisée lors de l'appel de la méthode Partie.jouer().
        """
        self.tableau_mines = None
        self.partie_terminee = False

    def jouer(self):
        """
        Tant que la partie n'est pas terminée, on joue un tour de la partie. 
        Une fois la partie terminée, on affiche le tableau de cases complètement dévoilée
        et on indique un message sur l'issue de la partie (victoire ou défaite).
        """

        dimension_rangee = int(input('Entrez le nombre de lignes : '))
        dimension_colonne = int(input('Entrez le nombre de colonnes : '))
        nombre_mines = int(input('Entrez le nombre de mines : '))
        
        self.tableau_mines = Tableau(dimension_rangee,dimension_colonne,nombre_mines)
        
        compteur_tours = 0
        while not self.partie_terminee:
            compteur_tours +=1
            print(f'\n===> Tour #{compteur_tours} <===')
            self.tableau_mines.afficher_tableau()
            self.tour()
            
        self.tableau_mines.afficher_solution()
        
        # TODO: Afficher le message de victoire ou de défaite
               
    def tour(self):
        """ 
        Jouer un tour, c'est-à-dire:
        
        À chaque tour:
            - On demande à l'utilisateur les coordonnées d'une case à dévoiler
            - On dévoile la case
            - On détecte si une mine a été actionnée, 
              auquel cas affecte True à l'attribut self.partie_terminee.
            - On détecte si toutes les cases ont été dévoilées, 
              auquel cas affecte True à l'attribut self.partie_terminee.
        """
        # TODO: À programmer.
        # On demande les coordonnée et on dévoile la case
        rangee_x, colonne_y = self.demander_coordonnees_case_a_devoiler()
        self.tableau_mines.devoiler_case(rangee_x, colonne_y)

        if  self.tableau_mines.contient_mine(rangee_x, colonne_y):  #Aurait probablement pu aussi être fait avec self.partie_terminee =  self.tableau_mines.contient_mine(rangee_x, colonne_y) je ne sais pas ce qui est le mieux
            self.partie_terminee = True

        if self.tableau_mines.nombre_cases_sans_mine_a_devoiler == 0:
            self.partie_terminee = True

        
    def valider_coordonnees(self, rangee_x, colonne_y):
        """
        Méthode qui valide les coordonnées reçues en paramètres.
        Les coordonnées doivent:
            1) être des caractères numériques;
            2) être à l'intérieur des valeurs possibles des rangées et des colonnes 
                du tableau; et 
            3) correspondre à une case qui n'a pas encore été dévoilée.

        Args:
            rangee_x (str):     Chaîne de caractères contenant la rangée
            colonne_y (str):    Chaîne de caractères contenant  la colonne

        Returns:
            bool : True si les coordonnées sont valides, False autrement.
        """
        valid = True
        # Vérifier si les coordonnées sont des caractères numériques
        if not (rangee_x.isnumeric() and colonne_y.isnumeric()):
            valid = False
        else:
        # Vérifier si les coordonnées sont à l'intérieur des valeurs possibles
        # des rangées et des colonnes du tableau
            rangee_x = int(rangee_x)
            colonne_y = int(colonne_y)
            if not self.tableau_mines.valider_coordonnees(rangee_x, colonne_y):
                valid = False
            else:
        # Vérifier si la case correspondre à une case qui n'a pas encore été
        # dévoilée
                case_xy = self.tableau_mines.obtenir_case(rangee_x, colonne_y)
                if case_xy.est_devoilee:
                    valid = False
        
        # Retourne le résultat
        if not valid:
            print('Coordonnées non valides. Recommencez!')
            return False
        else:
            return True
            
    def demander_coordonnees_case_a_devoiler(self):
        """
        Méthode qui demande à l'utilisateur d'entrer la coordonnée de la case qu'il veut dévoiler.
        Cette coordonnée comporte un numéro de rangée et un numéro de colonne.
        Tant que les coordonnées ne sont pas valides, on redemande de nouvelles coordonnées.
        Une fois les coordonnées validées, on retourne les deux numéros sous forme d'entiers.

        Returns:
            int: Numéro de la rangée
            int: Numéro de la colonne

        """
        rangee = input('Entrez le numéro de ligne : ')
        colonne = input('Entrez le numéro de colonne : ')

        while not self.valider_coordonnees(rangee, colonne):
            rangee = input('Entrez le numéro de ligne : ')
            colonne = input('Entrez le numéro de colonne : ')
        return int(rangee), int(colonne)

