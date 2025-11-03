

        # ui/cli_ui.py

class CLIUI:
    """Interface utilisateur en ligne de commande (CLI)"""

    def show_message(self, message):
        print(f"[INFO] {message}")

    def show_members(self, members):
        print("\n=== Liste des membres ===")
        for m in members[:10]:  # afficher seulement les 10 premiers
            print(f"- {m}")
        print(f"... ({len(members)} membres au total)")


