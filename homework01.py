

# homework1_chahira_cylia
#lecture d'un fichier texte(séparé par tabulations) et génération d'un page html
import csv
import sys
from html import escape 

def read_tab_file(filename, encoding='utf-8'):
    """
    Lit un fichier texte où les champs sont séparés par des tabulations.
    """
    try:
        with open(filename, 'r', encoding=encoding, newline='') as f:
            reader = csv.reader(f, delimiter='\t')
            try:
                header = next(reader)
            except StopIteration:
                print("Le fichier est vide.")
                return [], []
            data = [row for row in reader]
        return header, data

    except UnicodeDecodeError:
        if encoding != 'latin1':
            print("Problème d'encodage UTF-8, nouvelle tentative avec latin1 ...")
            return read_tab_file(filename, encoding='latin1')
        else:
            raise

    except FileNotFoundError:
        print("Erreur : le fichier est introuvable.")
        sys.exit(1)


def generate_html(header, data, output_file):
    """
    Génère une page HTML contenant un tableau de données.
    """
    html_parts = []
    html_parts.append("<!doctype html>")
    html_parts.append("<html lang='fr'>")
    html_parts.append("<head>")
    html_parts.append("<meta charset='utf-8' />")
    html_parts.append("<meta name='viewport' content='width=device-width, initial-scale=1' />")
    html_parts.append("<title>Membres de l’Association</title>")
    html_parts.append("<style>")
    html_parts.append("body{font-family:Arial, sans-serif; margin:20px; background:#f7f7f7;}")
    html_parts.append("h2{text-align:center;color:#0b6efd;}")
    html_parts.append("table{border-collapse:collapse;width:100%;background:white;}")
    html_parts.append("th,td{border:1px solid #ddd;padding:8px;text-align:left;}")
    html_parts.append("th{background:#f0f0f0;}")
    html_parts.append("tr:nth-child(even){background:#fafafa;}")
    html_parts.append("tr:hover{background:#f1f7ff;}")
    html_parts.append("</style>")
    html_parts.append("</head>")
    html_parts.append("<body>")
    html_parts.append("<h2>Liste des membres de l’association</h2>")

    html_parts.append("<table>")
    html_parts.append("<thead><tr>")
    for col in header:
        html_parts.append(f"<th>{escape(col)}</th>")
    html_parts.append("</tr></thead>")

    html_parts.append("<tbody>")
    for row in data:
        html_parts.append("<tr>")
        for i in range(len(header)):
            cell = row[i] if i < len(row) else ""
            html_parts.append(f"<td>{escape(cell)}</td>")
        if len(row) > len(header):
            for extra in row[len(header):]:
                html_parts.append(f"<td>{escape(extra)}</td>")
        html_parts.append("</tr>")
    html_parts.append("</tbody>")
    html_parts.append("</table>")
    html_parts.append("</body></html>")

    content = "\n".join(html_parts)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Fichier HTML créé avec succès : association_data.html")


def main():
    input_file = "association_data.txt"
    output_file = "association_data.html"

    header, data = read_tab_file(input_file)
    if not header:
        print("Aucun en-tête trouvé dans le fichier.")
        return

    print("En-têtes détectés :", header)
    print("Nombre de lignes lues :", len(data))
    generate_html(header, data, output_file)


if __name__ == "__main__":
    main()

