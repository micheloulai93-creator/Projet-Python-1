"""Module de gestion des vues avec interface professionnelle"""
import os
import sys
import time
from datetime import datetime


class Style:
    """Codes ANSI pour le style du texte"""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"
    
    # Couleurs texte
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    # Couleurs brillantes
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"
    
    # Backgrounds
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"


class Symbol:
    """Symboles Unicode pour interface professionnelle"""
    # Bordures simples
    H_LINE = "─"
    V_LINE = "│"
    TL_CORNER = "┌"
    TR_CORNER = "┐"
    BL_CORNER = "└"
    BR_CORNER = "┘"
    T_DOWN = "┬"
    T_UP = "┴"
    T_RIGHT = "├"
    T_LEFT = "┤"
    CROSS = "┼"
    
    # Bordures doubles
    H_DOUBLE = "═"
    V_DOUBLE = "║"
    TL_DOUBLE = "╔"
    TR_DOUBLE = "╗"
    BL_DOUBLE = "╚"
    BR_DOUBLE = "╝"
    T_DOWN_DOUBLE = "╦"
    T_UP_DOUBLE = "╩"
    T_RIGHT_DOUBLE = "╠"
    T_LEFT_DOUBLE = "╣"
    CROSS_DOUBLE = "╬"
    
    # Bordures arrondies
    TL_ROUND = "╭"
    TR_ROUND = "╮"
    BL_ROUND = "╰"
    BR_ROUND = "╯"
    
    # Symboles fonctionnels
    ARROW_RIGHT = "►"
    ARROW_LEFT = "◄"
    ARROW_UP = "▲"
    ARROW_DOWN = "▼"
    TRIANGLE_RIGHT = "▶"
    TRIANGLE_LEFT = "◀"
    
    # Puces et marqueurs
    BULLET = "•"
    CIRCLE = "○"
    CIRCLE_FILLED = "●"
    SQUARE = "□"
    SQUARE_FILLED = "■"
    DIAMOND = "◆"
    DIAMOND_OUTLINE = "◇"
    STAR = "★"
    STAR_OUTLINE = "☆"
    
    # Status
    CHECK = "✓"
    CROSS_MARK = "✗"
    PLUS = "+"
    MINUS = "−"
    MULTIPLY = "×"
    
    # Pièces d'échecs (unicodes élégants)
    KING = "♔"
    QUEEN = "♕"
    ROOK = "♖"
    BISHOP = "♗"
    KNIGHT = "♘"
    PAWN = "♙"
    
    # Barres de progression
    BAR_FULL = "█"
    BAR_SEVEN = "▉"
    BAR_SIX = "▊"
    BAR_FIVE = "▋"
    BAR_FOUR = "▌"
    BAR_THREE = "▍"
    BAR_TWO = "▎"
    BAR_ONE = "▏"
    BAR_EMPTY = "░"
    BAR_LIGHT = "▒"
    BAR_MEDIUM = "▓"
    
    # Séparateurs
    DOT = "·"
    ELLIPSIS = "…"
    SEPARATOR = "│"
    
    # Indicateurs
    INFO = "ⓘ"
    WARNING = "⚠"
    ERROR = "⨯"
    SUCCESS = "✔"
    QUESTION = "?"
    EXCLAMATION = "!"


class MenuView:
    """Gestionnaire d'interface utilisateur professionnelle"""
    
    USE_COLORS = True
    SCREEN_WIDTH = 80
    
    @classmethod
    def clear_screen(cls):
        """Efface l'écran"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @classmethod
    def set_title(cls, title):
        """Définit le titre de la fenêtre console"""
        if os.name == 'nt':
            os.system(f'title {title}')
        else:
            sys.stdout.write(f"\x1b]2;{title}\x07")
    
    @classmethod
    def print_header(cls, title, subtitle=None, width=None):
        """Affiche un en-tête professionnel"""
        if width is None:
            width = cls.SCREEN_WIDTH
        
        color = Style.BRIGHT_CYAN if cls.USE_COLORS else ""
        reset = Style.RESET if cls.USE_COLORS else ""
        
        # Ligne supérieure double
        print(f"\n{color}{Symbol.TL_DOUBLE}{Symbol.H_DOUBLE * (width - 2)}"
              f"{Symbol.TR_DOUBLE}{reset}")
        
        # Titre avec pièces d'échecs
        title_with_icons = f"{Symbol.KING}  {title}  {Symbol.QUEEN}"
        padding = (width - len(title_with_icons) - 2) // 2
        print(f"{color}{Symbol.V_DOUBLE}{' ' * padding}{Style.BOLD}"
              f"{title_with_icons}{Style.RESET}{color}"
              f"{' ' * (width - len(title_with_icons) - padding - 2)}"
              f"{Symbol.V_DOUBLE}{reset}")
        
        # Sous-titre si présent
        if subtitle:
            print(f"{color}{Symbol.V_DOUBLE}{' ' * (width - 2)}"
                  f"{Symbol.V_DOUBLE}{reset}")
            padding = (width - len(subtitle) - 2) // 2
            print(f"{color}{Symbol.V_DOUBLE}{' ' * padding}{Style.DIM}"
                  f"{subtitle}{Style.RESET}{color}"
                  f"{' ' * (width - len(subtitle) - padding - 2)}"
                  f"{Symbol.V_DOUBLE}{reset}")
        
        # Ligne inférieure double
        print(f"{color}{Symbol.BL_DOUBLE}{Symbol.H_DOUBLE * (width - 2)}"
              f"{Symbol.BR_DOUBLE}{reset}")
    
    @classmethod
    def print_section(cls, title, width=None):
        """Affiche un titre de section"""
        if width is None:
            width = cls.SCREEN_WIDTH
        
        color = Style.BRIGHT_YELLOW if cls.USE_COLORS else ""
        reset = Style.RESET if cls.USE_COLORS else ""
        
        print(f"\n{color}{Symbol.TL_CORNER}{Symbol.H_LINE * (width - 2)}"
              f"{Symbol.TR_CORNER}{reset}")
        padding = (width - len(title) - 6) // 2
        print(f"{color}{Symbol.V_LINE}{' ' * padding}{Symbol.DIAMOND} "
              f"{Style.BOLD}{title}{Style.RESET}{color} {Symbol.DIAMOND}"
              f"{' ' * (width - len(title) - padding - 6)}"
              f"{Symbol.V_LINE}{reset}")
        print(f"{color}{Symbol.BL_CORNER}{Symbol.H_LINE * (width - 2)}"
              f"{Symbol.BR_CORNER}{reset}\n")
    
    @classmethod
    def print_box(cls, content, width=None, style="single", 
                  color=None, padding=1):
        """Affiche une boîte avec contenu"""
        if width is None:
            width = cls.SCREEN_WIDTH
        
        # Choisir le style de bordure
        if style == "double":
            tl, tr, bl, br = (Symbol.TL_DOUBLE, Symbol.TR_DOUBLE, 
                             Symbol.BL_DOUBLE, Symbol.BR_DOUBLE)
            h, v = Symbol.H_DOUBLE, Symbol.V_DOUBLE
        elif style == "round":
            tl, tr, bl, br = (Symbol.TL_ROUND, Symbol.TR_ROUND,
                             Symbol.BL_ROUND, Symbol.BR_ROUND)
            h, v = Symbol.H_LINE, Symbol.V_LINE
        else:
            tl, tr, bl, br = (Symbol.TL_CORNER, Symbol.TR_CORNER,
                             Symbol.BL_CORNER, Symbol.BR_CORNER)
            h, v = Symbol.H_LINE, Symbol.V_LINE
        
        lines = content.split('\n')
        max_len = max(len(line) for line in lines) if lines else 0
        box_width = min(width, max_len + 2 * padding + 2)
        
        color_code = color if (color and cls.USE_COLORS) else ""
        reset = Style.RESET if cls.USE_COLORS else ""
        
        # Bordure supérieure
        print(f"{color_code}{tl}{h * (box_width - 2)}{tr}{reset}")
        
        # Lignes vides de padding
        for _ in range(padding):
            print(f"{color_code}{v}{' ' * (box_width - 2)}{v}{reset}")
        
        # Contenu
        for line in lines:
            line_padding = box_width - len(line) - 2 - 2 * padding
            print(f"{color_code}{v}{' ' * padding}{line}"
                  f"{' ' * (line_padding + padding)}{v}{reset}")
        
        # Lignes vides de padding
        for _ in range(padding):
            print(f"{color_code}{v}{' ' * (box_width - 2)}{v}{reset}")
        
        # Bordure inférieure
        print(f"{color_code}{bl}{h * (box_width - 2)}{br}{reset}")
    
    @classmethod
    def print_menu_item(cls, key, label, icon=None, selected=False):
        """Affiche un élément de menu stylisé"""
        if cls.USE_COLORS:
            key_color = Style.BRIGHT_GREEN
            label_color = Style.BOLD if selected else Style.RESET
            icon_color = Style.BRIGHT_CYAN
            reset = Style.RESET
        else:
            key_color = label_color = icon_color = reset = ""
        
        prefix = Symbol.ARROW_RIGHT if selected else " "
        icon_str = f"{icon_color}{icon}{reset} " if icon else ""
        
        print(f"  {prefix} {key_color}[{key}]{reset} {icon_str}"
              f"{label_color}{label}{reset}")
    
    @classmethod
    def print_divider(cls, width=None, style="light", color=None):
        """Affiche une ligne de séparation"""
        if width is None:
            width = cls.SCREEN_WIDTH
        
        if style == "heavy":
            char = Symbol.H_DOUBLE
        elif style == "dotted":
            char = Symbol.DOT
        else:
            char = Symbol.H_LINE
        
        color_code = color if (color and cls.USE_COLORS) else ""
        reset = Style.RESET if cls.USE_COLORS else ""
        
        print(f"{color_code}{char * width}{reset}")
    
    @classmethod
    def print_table(cls, headers, rows, title=None, width=None):
        """Affiche un tableau professionnel"""
        if width is None:
            width = cls.SCREEN_WIDTH
        
        if title:
            cls.print_section(title, width)
        
        if not rows:
            print(f"{Style.DIM}  Aucune donnée à afficher{Style.RESET}\n")
            return
        
        # Calculer les largeurs de colonnes
        col_widths = [len(str(h)) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(cell)))
        
        # Ajuster pour tenir dans la largeur
        total_width = sum(col_widths) + len(headers) * 3 + 1
        if total_width > width:
            scale = (width - len(headers) * 3 - 1) / sum(col_widths)
            col_widths = [max(8, int(w * scale)) for w in col_widths]
        
        color = Style.BRIGHT_CYAN if cls.USE_COLORS else ""
        reset = Style.RESET if cls.USE_COLORS else ""
        
        # Ligne supérieure
        print(f"{color}{Symbol.TL_CORNER}", end="")
        for i, w in enumerate(col_widths):
            print(Symbol.H_LINE * (w + 2), end="")
            if i < len(col_widths) - 1:
                print(Symbol.T_DOWN, end="")
        print(f"{Symbol.TR_CORNER}{reset}")
        
        # En-têtes
        print(f"{color}{Symbol.V_LINE}{reset}", end="")
        for i, (header, w) in enumerate(zip(headers, col_widths)):
            print(f" {Style.BOLD}{str(header).ljust(w)}{Style.RESET} ", 
                  end="")
            print(f"{color}{Symbol.V_LINE}{reset}", end="")
        print()
        
        # Séparateur après en-têtes
        print(f"{color}{Symbol.T_RIGHT}", end="")
        for i, w in enumerate(col_widths):
            print(Symbol.H_LINE * (w + 2), end="")
            if i < len(col_widths) - 1:
                print(Symbol.CROSS, end="")
        print(f"{Symbol.T_LEFT}{reset}")
        
        # Lignes de données
        for row_idx, row in enumerate(rows):
            print(f"{color}{Symbol.V_LINE}{reset}", end="")
            for i, (cell, w) in enumerate(zip(row, col_widths)):
                cell_str = str(cell)
                if len(cell_str) > w:
                    cell_str = cell_str[:w-1] + Symbol.ELLIPSIS
                print(f" {cell_str.ljust(w)} ", end="")
                print(f"{color}{Symbol.V_LINE}{reset}", end="")
            print()
        
        # Ligne inférieure
        print(f"{color}{Symbol.BL_CORNER}", end="")
        for i, w in enumerate(col_widths):
            print(Symbol.H_LINE * (w + 2), end="")
            if i < len(col_widths) - 1:
                print(Symbol.T_UP, end="")
        print(f"{Symbol.BR_CORNER}{reset}")
        
        # Ligne de résumé
        print(f"{Style.DIM}  {Symbol.INFO} Total: {len(rows)} "
              f"enregistrement(s){Style.RESET}\n")
    
    @classmethod
    def print_progress_bar(cls, current, total, width=40, label="", 
                          show_percent=True):
        """Affiche une barre de progression élégante"""
        percentage = (current / total) * 100
        filled = int(width * current / total)
        
        bar = (Symbol.BAR_FULL * filled + 
               Symbol.BAR_EMPTY * (width - filled))
        
        if cls.USE_COLORS:
            color = Style.BRIGHT_GREEN
            reset = Style.RESET
        else:
            color = reset = ""
        
        percent_str = f" {percentage:5.1f}%" if show_percent else ""
        
        print(f"\r{label} {color}[{bar}]{reset}{percent_str}", 
              end='', flush=True)
    
    @classmethod
    def print_status(cls, status_type, message):
        """Affiche un message de statut"""
        if status_type == "success":
            icon = Symbol.CHECK
            color = Style.BRIGHT_GREEN if cls.USE_COLORS else ""
        elif status_type == "error":
            icon = Symbol.CROSS_MARK
            color = Style.BRIGHT_RED if cls.USE_COLORS else ""
        elif status_type == "warning":
            icon = Symbol.WARNING
            color = Style.BRIGHT_YELLOW if cls.USE_COLORS else ""
        elif status_type == "info":
            icon = Symbol.INFO
            color = Style.BRIGHT_CYAN if cls.USE_COLORS else ""
        else:
            icon = Symbol.BULLET
            color = ""
        
        reset = Style.RESET if cls.USE_COLORS else ""
        print(f"\n{color}{icon} {message}{reset}")
    
    @classmethod
    def get_input(cls, prompt, icon=None):
        """Demande une saisie utilisateur stylisée"""
        if icon:
            icon_str = f"{Style.BRIGHT_CYAN}{icon}{Style.RESET} " \
                      if cls.USE_COLORS else f"{icon} "
        else:
            icon_str = f"{Style.BRIGHT_CYAN}{Symbol.ARROW_RIGHT}" \
                      f"{Style.RESET} " if cls.USE_COLORS else "> "
        
        return input(f"{icon_str}{prompt}: ").strip()
    
    @classmethod
    def get_choice(cls, options, prompt="Sélectionnez une option"):
        """Affiche un menu de choix et retourne la sélection"""
        print()
        for key, label in options.items():
            cls.print_menu_item(key, label)
        
        print()
        return cls.get_input(prompt)
    
    @classmethod
    def confirm(cls, message, default=False):
        """Demande une confirmation"""
        default_str = "O/n" if default else "o/N"
        response = cls.get_input(f"{message} [{default_str}]", 
                                 icon=Symbol.QUESTION)
        
        if not response:
            return default
        
        return response.lower() in ['o', 'oui', 'y', 'yes']
    
    @classmethod
    def animate_spinner(cls, message, duration=1.0):
        """Affiche un spinner animé"""
        frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        end_time = time.time() + duration
        
        i = 0
        while time.time() < end_time:
            color = Style.BRIGHT_CYAN if cls.USE_COLORS else ""
            reset = Style.RESET if cls.USE_COLORS else ""
            print(f"\r{color}{frames[i % len(frames)]} {message}...{reset}", 
                  end='', flush=True)
            time.sleep(0.1)
            i += 1
        
        print(f"\r{' ' * (len(message) + 10)}\r", end='')
    
    @classmethod
    def pause(cls):
        """Pause l'exécution"""
        print(f"\n{Style.DIM}{Symbol.H_LINE * cls.SCREEN_WIDTH}"
              f"{Style.RESET}")
        input(f"{Style.BRIGHT_YELLOW}  Appuyez sur [Entrée] pour "
              f"continuer{Style.RESET}")
    
    # ==================== MENUS SPÉCIFIQUES ====================
    
    @staticmethod
    def display_main_menu():
        """Menu principal"""
        MenuView.clear_screen()
        MenuView.set_title("Chess Manager - Menu Principal")
        MenuView.print_header(
            "GESTIONNAIRE DE TOURNOIS D'ÉCHECS",
            f"v1.0 {Symbol.SEPARATOR} {datetime.now().strftime('%d/%m/%Y %H:%M')}"
        )
        
        print()
        MenuView.print_menu_item("1", "Gestion des joueurs", Symbol.PAWN)
        MenuView.print_menu_item("2", "Gestion des tournois", Symbol.ROOK)
        MenuView.print_menu_item("3", "Rapports et statistiques", Symbol.STAR)
        MenuView.print_menu_item("4", "Sauvegarder les données", Symbol.SQUARE_FILLED)
        MenuView.print_menu_item("5", "Quitter l'application", Symbol.CROSS_MARK)
        
        MenuView.print_divider()
        return MenuView.get_input("Votre choix")
    
    @staticmethod
    def display_player_menu():
        """Menu gestion des joueurs"""
        MenuView.clear_screen()
        MenuView.print_section(f"{Symbol.PAWN} GESTION DES JOUEURS")
        
        MenuView.print_menu_item("1", "Ajouter un joueur", Symbol.PLUS)
        MenuView.print_menu_item("2", "Ajouter plusieurs joueurs", Symbol.PLUS)
        MenuView.print_menu_item("3", "Modifier un classement", Symbol.STAR)
        MenuView.print_menu_item("4", "Afficher tous les joueurs", Symbol.CIRCLE)
        MenuView.print_menu_item("5", "Supprimer un joueur", Symbol.CROSS_MARK) 
        MenuView.print_menu_item("6", "Retour au menu principal", Symbol.ARROW_LEFT)
        
        MenuView.print_divider()
        return MenuView.get_input("Votre choix")
    
    @staticmethod
    def get_player_info():
        """Formulaire d'ajout de joueur"""
        MenuView.print_section(f"{Symbol.PAWN} NOUVEAU JOUEUR")
        
        print(f"{Style.DIM}Veuillez renseigner les informations du joueur:"
              f"{Style.RESET}\n")
        
        first_name = MenuView.get_input("Prénom", Symbol.ARROW_RIGHT)
        last_name = MenuView.get_input("Nom", Symbol.ARROW_RIGHT)
        birth_date = MenuView.get_input("Date de naissance (JJ/MM/AAAA)", 
                                       Symbol.ARROW_RIGHT)
        gender = MenuView.get_input("Sexe (M/F)", Symbol.ARROW_RIGHT)
        
        while True:
            try:
                ranking = int(MenuView.get_input("Classement", 
                                                Symbol.STAR))
                break
            except ValueError:
                MenuView.print_status("error", 
                                    "Veuillez entrer un nombre valide")
        
        return first_name, last_name, birth_date, gender.upper(), ranking
    
    @staticmethod
    def get_multiple_players_info(count=8):
        """Ajout multiple de joueurs"""
        MenuView.print_section(f"{Symbol.PAWN} AJOUT DE {count} JOUEURS")
        
        print(f"{Style.BRIGHT_YELLOW}{Symbol.INFO} Conseil: Préparez vos "
              f"informations à l'avance{Style.RESET}\n")
        
        players_data = []
        
        for i in range(count):
            MenuView.print_divider(60, "dotted", Style.DIM)
            print(f"\n{Style.BOLD}{Symbol.DIAMOND} Joueur {i + 1}/{count}"
                  f"{Style.RESET}\n")
            
            player_info = MenuView.get_player_info()
            players_data.append(player_info)
            
            # Barre de progression
            time.sleep(0.1)
            MenuView.print_progress_bar(i + 1, count, 
                                       label=f"{Symbol.CHECK} Progression")
            print("\n")
        
        return players_data
    
    @staticmethod
    def display_tournament_menu():
        """Menu gestion des tournois"""
        MenuView.clear_screen()
        MenuView.print_section(f"{Symbol.ROOK} GESTION DES TOURNOIS")
        
        MenuView.print_menu_item("1", "Créer un nouveau tournoi", Symbol.PLUS)
        MenuView.print_menu_item("2", "Gérer un tournoi existant", Symbol.SQUARE_FILLED)
        MenuView.print_menu_item("3", "Afficher tous les tournois", Symbol.CIRCLE)
        MenuView.print_menu_item("4", "Supprimer un tournoi", Symbol.CROSS_MARK)
        MenuView.print_menu_item("5", "Retour au menu principal", Symbol.ARROW_LEFT)
        
        MenuView.print_divider()
        return MenuView.get_input("Votre choix")
    
    @staticmethod
    def get_tournament_info():
        """Formulaire de création de tournoi"""
        MenuView.print_section(f"{Symbol.ROOK} NOUVEAU TOURNOI")
        
        print(f"{Style.DIM}Configuration du tournoi:{Style.RESET}\n")
        
        name = MenuView.get_input("Nom du tournoi", Symbol.ROOK)
        location = MenuView.get_input("Lieu", Symbol.ARROW_RIGHT)
        start_date = MenuView.get_input("Date de début (JJ/MM/AAAA)", 
                                       Symbol.ARROW_RIGHT)
        end_date = MenuView.get_input("Date de fin (JJ/MM/AAAA)", 
                                     Symbol.ARROW_RIGHT)
        
        rounds_input = MenuView.get_input("Nombre de tours [4]", 
                                         Symbol.ARROW_RIGHT)
        number_of_rounds = int(rounds_input) if rounds_input else 4
        
        print(f"\n{Style.BOLD}Contrôle du temps:{Style.RESET}")
        print(f"  [1] Bullet  (< 3 min)")
        print(f"  [2] Blitz   (3-10 min)")
        print(f"  [3] Rapid   (10-60 min)")
        
        time_choice = MenuView.get_input("\nSélection", Symbol.ARROW_RIGHT)
        time_control = {
            "1": "bullet",
            "2": "blitz",
            "3": "rapid"
        }.get(time_choice, "blitz")
        
        description = MenuView.get_input("Description (optionnel)", 
                                        Symbol.ARROW_RIGHT)
        
        return (name, location, start_date, end_date,
                number_of_rounds, time_control, description)
    
    @staticmethod
    def display_single_tournament_menu(tournament):
        """Menu d'un tournoi spécifique"""
        MenuView.clear_screen()
        
        # Boîte d'informations du tournoi
        info_text = (f"{Symbol.ROOK} {tournament.name}\n"
                    f"{Symbol.ARROW_RIGHT} {tournament.location}\n"
                    f"{Symbol.STAR} Tour {tournament.current_round}/"
                    f"{tournament.number_of_rounds}\n"
                    f"{Symbol.CIRCLE} {tournament.time_control.upper()}")
        
        MenuView.print_box(info_text, style="double", 
                          color=Style.BRIGHT_CYAN, padding=1)
        
        print()
        MenuView.print_menu_item("1", "Démarrer un nouveau tour", 
                                Symbol.TRIANGLE_RIGHT)
        MenuView.print_menu_item("2", "Saisir les résultats", 
                                Symbol.SQUARE_FILLED)
        MenuView.print_menu_item("3", "Afficher l'état du tournoi", 
                                Symbol.STAR)
        MenuView.print_menu_item("4", "Retour", Symbol.ARROW_LEFT)
        
        MenuView.print_divider()
        return MenuView.get_input("Votre choix")
    
    @staticmethod
    def display_reports_menu():
        """Menu des rapports"""
        MenuView.clear_screen()
        MenuView.print_section(f"{Symbol.STAR} RAPPORTS ET STATISTIQUES")
        
        MenuView.print_menu_item("1", "Joueurs (ordre alphabétique)", 
                                Symbol.ARROW_RIGHT)
        MenuView.print_menu_item("2", "Joueurs (par classement)", 
                                Symbol.STAR)
        MenuView.print_menu_item("3", "Joueurs d'un tournoi", 
                                Symbol.PAWN)
        MenuView.print_menu_item("4", "Liste des tournois", 
                                Symbol.ROOK)
        MenuView.print_menu_item("5", "Tours d'un tournoi", 
                                Symbol.CIRCLE)
        MenuView.print_menu_item("6", "Matchs d'un tournoi", 
                                Symbol.SQUARE_FILLED)
        MenuView.print_menu_item("7", "Retour au menu principal", 
                                Symbol.ARROW_LEFT)
        
        MenuView.print_divider()
        return MenuView.get_input("Votre choix")
    
    # Méthodes de compatibilité
    @staticmethod
    def display_success(msg):
      MenuView.print_status("success", msg)

    @staticmethod
    def display_success(msg):
      MenuView.print_status("error", msg)

    @staticmethod
    def display_success(msg):
      MenuView.print_status("warning", msg)

    @staticmethod
    def display_success(msg):
      MenuView.print_status("info", msg)
    
    @staticmethod
    def display_players_list(players, title="LISTE DES JOUEURS"):
        """Affiche une liste de joueurs en tableau"""
        headers = ["#", "Nom complet", "Date naissance", "Sexe", "Classement"]
        rows = []
        
        for i, player in enumerate(players, 1):
            full_name = f"{player.first_name} {player.last_name}"
            rows.append([
                i,
                full_name,
                player.birth_date,
                player.gender,
                player.ranking
            ])
        
        MenuView.print_table(headers, rows, title)
    
    @staticmethod
    def display_match_pairing(match_number, player1, player2):
        """Affiche un appariement de match"""
        width = 70
        
        color = Style.BRIGHT_CYAN if MenuView.USE_COLORS else ""
        reset = Style.RESET if MenuView.USE_COLORS else ""
        
        print(f"\n{color}{Symbol.TL_ROUND}{Symbol.H_LINE * (width - 2)}"
              f"{Symbol.TR_ROUND}{reset}")
        
        # Numéro du match
        match_title = f"MATCH {match_number}"
        padding = (width - len(match_title) - 2) // 2
        print(f"{color}{Symbol.V_LINE}{' ' * padding}{Style.BOLD}"
              f"{match_title}{Style.RESET}{color}"
              f"{' ' * (width - len(match_title) - padding - 2)}"
              f"{Symbol.V_LINE}{reset}")
        
        print(f"{color}{Symbol.V_LINE}{' ' * (width - 2)}{Symbol.V_LINE}"
              f"{reset}")
        
        # Joueur 1
        p1_name = f"{player1.first_name} {player1.last_name}"
        p1_info = (f"{Symbol.PAWN} {p1_name} "
                  f"{Symbol.SEPARATOR} Classement: {player1.ranking}")
        padding1 = (width - len(p1_info) - 2) // 2
        print(f"{color}{Symbol.V_LINE}{' ' * padding1}{p1_info}"
              f"{' ' * (width - len(p1_info) - padding1 - 2)}"
              f"{Symbol.V_LINE}{reset}")
        
        # VS
        vs_text = "VS"
        padding_vs = (width - len(vs_text) - 2) // 2
        print(f"{color}{Symbol.V_LINE}{' ' * padding_vs}"
              f"{Style.BOLD}{vs_text}{Style.RESET}{color}"
              f"{' ' * (width - len(vs_text) - padding_vs - 2)}"
              f"{Symbol.V_LINE}{reset}")
        
        # Joueur 2
        p2_name = f"{player2.first_name} {player2.last_name}"
        p2_info = (f"{Symbol.PAWN} {p2_name} "
                  f"{Symbol.SEPARATOR} Classement: {player2.ranking}")
        padding2 = (width - len(p2_info) - 2) // 2
        print(f"{color}{Symbol.V_LINE}{' ' * padding2}{p2_info}"
              f"{' ' * (width - len(p2_info) - padding2 - 2)}"
              f"{Symbol.V_LINE}{reset}")
        
        print(f"{color}{Symbol.BL_ROUND}{Symbol.H_LINE * (width - 2)}"
              f"{Symbol.BR_ROUND}{reset}")
    
    @staticmethod
    def display_tournament_standings(players, title="CLASSEMENT"):
        """Affiche le classement d'un tournoi"""
        MenuView.print_section(f"{Symbol.STAR} {title}")
        
        headers = ["Pos", "Joueur", "Points", "Classement"]
        rows = []
        
        for i, player in enumerate(players, 1):
            # Icône de podium
            if i == 1:
                pos = f"{Symbol.STAR} 1"
            elif i == 2:
                pos = f"{Symbol.STAR_OUTLINE} 2"
            elif i == 3:
                pos = f"{Symbol.STAR_OUTLINE} 3"
            else:
                pos = str(i)
            
            full_name = f"{player.first_name} {player.last_name}"
            rows.append([
                pos,
                full_name,
                f"{player.score:.1f}",
                player.ranking
            ])
        
        MenuView.print_table(headers, rows)
    
    @staticmethod
    def display_round_summary(round_obj):
        """Affiche le résumé d'un tour"""
        width = 70
        
        color = Style.BRIGHT_YELLOW if MenuView.USE_COLORS else ""
        reset = Style.RESET if MenuView.USE_COLORS else ""
        
        print(f"\n{color}{Symbol.TL_DOUBLE}{Symbol.H_DOUBLE * (width - 2)}"
              f"{Symbol.TR_DOUBLE}{reset}")
        
        # Nom du tour
        title = f"{Symbol.ROOK} {round_obj.name}"
        padding = (width - len(title) - 2) // 2
        print(f"{color}{Symbol.V_DOUBLE}{' ' * padding}{Style.BOLD}"
              f"{title}{Style.RESET}{color}"
              f"{' ' * (width - len(title) - padding - 2)}"
              f"{Symbol.V_DOUBLE}{reset}")
        
        # Dates
        if hasattr(round_obj, 'start_time') and round_obj.start_time:
            start_str = f"Début: {round_obj.start_time}"
            end_str = (f"Fin: {round_obj.end_time}" 
                      if round_obj.end_time else "En cours...")
            
            print(f"{color}{Symbol.V_DOUBLE}{' ' * (width - 2)}"
                  f"{Symbol.V_DOUBLE}{reset}")
            print(f"{color}{Symbol.V_DOUBLE}  {Style.DIM}{start_str}"
                  f"{' ' * (width - len(start_str) - 4)}"
                  f"{Style.RESET}{color}{Symbol.V_DOUBLE}{reset}")
            print(f"{color}{Symbol.V_DOUBLE}  {Style.DIM}{end_str}"
                  f"{' ' * (width - len(end_str) - 4)}"
                  f"{Style.RESET}{color}{Symbol.V_DOUBLE}{reset}")
        
        print(f"{color}{Symbol.BL_DOUBLE}{Symbol.H_DOUBLE * (width - 2)}"
              f"{Symbol.BR_DOUBLE}{reset}")
        
        # Afficher les matchs
        if hasattr(round_obj, 'matches'):
            print(f"\n{Style.BOLD}Matchs:{Style.RESET}\n")
            for i, match in enumerate(round_obj.matches, 1):
                MenuView.display_match_result(match, i)
    
    @staticmethod
    def display_match_result(match, match_number):
        """Affiche le résultat d'un match"""
        p1_name = f"{match.player1.first_name} {match.player1.last_name}"
        p2_name = f"{match.player2.first_name} {match.player2.last_name}"
        
        # Déterminer le gagnant ou match nul
        if hasattr(match, 'score1') and hasattr(match, 'score2'):
            if match.score1 > match.score2:
                p1_style = Style.BRIGHT_GREEN
                p2_style = Style.DIM
                result = f"{match.score1} - {match.score2}"
            elif match.score2 > match.score1:
                p1_style = Style.DIM
                p2_style = Style.BRIGHT_GREEN
                result = f"{match.score1} - {match.score2}"
            else:
                p1_style = p2_style = Style.BRIGHT_YELLOW
                result = f"{match.score1} - {match.score2}"
        else:
            p1_style = p2_style = ""
            result = "À venir"
        
        reset = Style.RESET if MenuView.USE_COLORS else ""
        
        print(f"  {Symbol.SQUARE_FILLED} Match {match_number}:")
        print(f"     {p1_style}{p1_name}{reset} vs {p2_style}{p2_name}{reset}")
        print(f"     {Symbol.ARROW_RIGHT} Résultat: {result}")
        print()
    
    @staticmethod
    def display_tournament_card(tournament, index):
        """Affiche une carte de tournoi"""
        width = 60
        
        status = "Terminé" if tournament.is_complete() else "En cours"
        status_color = (Style.BRIGHT_GREEN if tournament.is_complete() 
                       else Style.BRIGHT_YELLOW)
        
        color = Style.BRIGHT_CYAN if MenuView.USE_COLORS else ""
        reset = Style.RESET if MenuView.USE_COLORS else ""
        
        print(f"\n{color}{Symbol.TL_CORNER}{Symbol.H_LINE * (width - 2)}"
              f"{Symbol.TR_CORNER}{reset}")
        
        # Numéro et nom
        header = f"{index}. {Symbol.ROOK} {tournament.name}"
        print(f"{color}{Symbol.V_LINE} {Style.BOLD}{header}"
              f"{' ' * (width - len(header) - 4)}{Style.RESET}{color}"
              f"{Symbol.V_LINE}{reset}")
        
        print(f"{color}{Symbol.T_RIGHT}{Symbol.H_LINE * (width - 2)}"
              f"{Symbol.T_LEFT}{reset}")
        
        # Informations
        info_lines = [
            f"Lieu: {tournament.location}",
            f"Dates: {tournament.start_date} - {tournament.end_date}",
            f"Tours: {tournament.current_round}/{tournament.number_of_rounds}",
            f"Contrôle: {tournament.time_control}",
            f"Statut: {status}"
        ]
        
        for line in info_lines[:-1]:
            print(f"{color}{Symbol.V_LINE} {Symbol.BULLET} {line}"
                  f"{' ' * (width - len(line) - 6)}{Symbol.V_LINE}{reset}")
        
        # Dernière ligne avec statut coloré
        last_line = info_lines[-1]
        print(f"{color}{Symbol.V_LINE} {Symbol.BULLET} "
              f"{last_line.split(':')[0]}: {reset}{status_color}{status}"
              f"{reset}{color}"
              f"{' ' * (width - len(last_line) - 6)}{Symbol.V_LINE}{reset}")
        
        print(f"{color}{Symbol.BL_CORNER}{Symbol.H_LINE * (width - 2)}"
              f"{Symbol.BR_CORNER}{reset}")
    
    @staticmethod
    def display_dashboard(stats):
        """Affiche un tableau de bord avec statistiques"""
        MenuView.clear_screen()
        MenuView.print_header("TABLEAU DE BORD", 
                             f"Mis à jour: {datetime.now().strftime('%H:%M:%S')}")
        
        # Créer des cartes de statistiques
        cards = [
            ("JOUEURS", stats.get('players', 0), Symbol.PAWN),
            ("TOURNOIS", stats.get('tournaments', 0), Symbol.ROOK),
            ("EN COURS", stats.get('active', 0), Symbol.CIRCLE_FILLED),
            ("TERMINÉS", stats.get('completed', 0), Symbol.CHECK)
        ]
        
        card_width = 18
        print()
        
        # Ligne supérieure
        for _ in cards:
            print(f"{Symbol.TL_CORNER}{Symbol.H_LINE * card_width}"
                  f"{Symbol.TR_CORNER}", end="  ")
        print()
        
        # Titres
        for title, _, icon in cards:
            title_str = f"{icon} {title}"
            padding = (card_width - len(title_str)) // 2
            print(f"{Symbol.V_LINE}{' ' * padding}{Style.BOLD}{title_str}"
                  f"{Style.RESET}{' ' * (card_width - len(title_str) - padding)}"
                  f"{Symbol.V_LINE}", end="  ")
        print()
        
        # Séparateur
        for _ in cards:
            print(f"{Symbol.T_RIGHT}{Symbol.H_LINE * card_width}"
                  f"{Symbol.T_LEFT}", end="  ")
        print()
        
        # Valeurs
        for _, value, _ in cards:
            value_str = str(value)
            padding = (card_width - len(value_str)) // 2
            print(f"{Symbol.V_LINE}{' ' * padding}"
                  f"{Style.BRIGHT_GREEN}{Style.BOLD}{value_str}"
                  f"{Style.RESET}{' ' * (card_width - len(value_str) - padding)}"
                  f"{Symbol.V_LINE}", end="  ")
        print()
        
        # Ligne inférieure
        for _ in cards:
            print(f"{Symbol.BL_CORNER}{Symbol.H_LINE * card_width}"
                  f"{Symbol.BR_CORNER}", end="  ")
        print("\n")
    
    @staticmethod
    def display_help_panel():
        """Affiche un panneau d'aide"""
        help_text = f"""
{Symbol.INFO} RACCOURCIS CLAVIER:
  {Symbol.ARROW_RIGHT} [1-9] : Sélection rapide
  {Symbol.ARROW_RIGHT} [Q]   : Quitter le menu actuel
  {Symbol.ARROW_RIGHT} [H]   : Afficher l'aide

{Symbol.INFO} NAVIGATION:
  {Symbol.ARROW_RIGHT} Utilisez les numéros pour naviguer
  {Symbol.ARROW_RIGHT} Suivez les instructions à l'écran
  {Symbol.ARROW_RIGHT} Les données sont sauvegardées automatiquement

{Symbol.INFO} SUPPORT:
  {Symbol.ARROW_RIGHT} Version: 1.0
  {Symbol.ARROW_RIGHT} Documentation: disponible
        """.strip()
        
        MenuView.print_box(help_text, width=60, style="round", 
                          color=Style.BRIGHT_CYAN, padding=1)
    
    @staticmethod
    def display_loading_screen(message="Chargement"):
        """Écran de chargement avec animation"""
        MenuView.clear_screen()
        
        # Logo ASCII
        logo = [
            "   ♔ ♕ ♖ ♗ ♘ ♙",
            "CHESS MANAGER",
            "   ♟ ♞ ♝ ♜ ♛ ♚"
        ]
        
        for line in logo:
            padding = (MenuView.SCREEN_WIDTH - len(line)) // 2
            print(f"{' ' * padding}{Style.BRIGHT_CYAN}{Style.BOLD}"
                  f"{line}{Style.RESET}")
        
        print("\n" * 3)
        
        # Animation de chargement
        MenuView.animate_spinner(message, duration=1.5)
        
        MenuView.print_status("success", "Chargement terminé")
        time.sleep(0.5)