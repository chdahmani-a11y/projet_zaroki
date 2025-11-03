##  Contexte du projet  
Ce travail est la **troisième partie (HW3)** du projet de gestion d’une association de jeunes / club scientifique.  
Les précédents (HW1 et HW2) consistaient à :
- Lire et afficher des données depuis un fichier texte (.CSV).  
- Modéliser les entités principales du système (Member, Event, Subscription, ScientificClub).  

Dans cette troisième étape, nous avons **restructuré le projet selon les principes SOLID** pour améliorer la **qualité, la modularité et la maintenabilité** du code.

--------------------------------------------------------------------------------------------------------------

##  Problèmes résolus
Avant : `main.py` lisait directement le fichier → forte dépendance au format CSV.  
Après : `main` utilise une abstraction → facile de changer de source de données.

-----------------------------------------------------------------------------------------------------------

#  Application des principes SOLID — Homework-3_chahira_cylia

## **1. SRP — Single Responsibility Principle**  
Chaque classe a une seule responsabilité :  
- `Member` gère uniquement les données d’un membre.  
- `ScientificClub` gère uniquement la logique du club (affichage, statistiques, génération HTML).  
- `CSVStorage` gère la lecture des données à partir d’un fichier .CSV ou .TXT.  
- `CLIUI` affiche les résultats à l’utilisateur.

Cela rend le code plus clair et plus facile à tester.

### **Application du SRP (partie 2)**
Nous avons introduit deux classes d’assistance :
- `FileStorage` : lecture/écriture des fichiers CSV ou TSV.
- `FinanceManager` : logique financière (comptage, ratios, statistiques).

---------------------------------------------------------------------------------------------------------

## **2. OCP — Open/Closed Principle**  
Le système est **ouvert à l’extension** mais **fermé à la modification**.  
Une classe de base `Event` définit les attributs communs, et trois sous-classes spécialisées (`Trip`, `Meeting`, `Competition`) permettent d’ajouter de nouveaux types d’événements sans modifier le code existant.  
Ainsi, on peut aussi étendre le système avec de nouveaux types d’abonnements (`Donation`, `MonthlySubscription`, `AnnualSubscription`) sans toucher aux classes existantes.

-----------------------------------------------------------------------------------------

## **3. LSP — Liskov Substitution Principle**  
Toutes les classes dérivées d’`Event` implémentent la méthode `describe()` ou `get_summary()` afin d’assurer la substituabilité.  
Exemple : on peut remplacer `Trip` par `Competition` sans casser le comportement du programme.

---------------------------------------------------------------------------------------------------

## **4. ISP — Interface Segregation Principle**  
Les interfaces sont divisées en petites unités spécialisées :  
- `IStorage` pour la gestion du stockage.  
- `IUI` pour la gestion de l’affichage (CLI ou Web).  

### **Application du ISP (partie 2)**
Trois interfaces indépendantes ont été créées :

| Interface | Méthodes clés | Rôle |
|------------|---------------|------|
| **Payable** | `process_payment()` | Gestion des paiements et abonnements des membres |
| **Organizable** | `schedule()` | Planification et gestion des événements |
| **Registrable** | `register_member()` | Enregistrement et gestion des membres |

Chaque classe n’implémente que ce dont elle a besoin :
- `Member` implémente `Payable`
- `ScientificClub` implémente `Organizable` et `Registrable`



## **5. DIP — Dependency Inversion Principle**  
Les modules de haut niveau (comme `MemberRepository` ou `ScientificClub`) dépendent **d’abstractions** et non de classes concrètes.  

Deux interfaces principales ont été définies dans `interfaces/` :  
- **`IStorage`** : définit `load_data()`  
- **`IUI`** : définit `show_message()` et `show_members()`  

Dans `homework03_main.py`, on injecte `CSVStorage` et `CLIUI` sans dépendance directe :

```python
storage = CSVStorage("association_data.txt", encoding='utf-8')
repo = MemberRepository(storage)
ui = CLIUI()
ui.show_message("Chargement des membres...")
members = repo.load_members()
ui.show_members(members)




# Application du principe SRP
git commit -m "feat: apply SRP to Member and ScientificClub"

# Application du principe OCP
git commit -m "refactor: add Event subclasses (Trip, Meeting, Competition)"

# Application du principe LSP
git commit -m "feat: ensure all Event subclasses implement describe() correctly"

# Application du principe ISP
git commit -m "feat: add Payable, Registrable, and Organizable interfaces"

# Application du principe DIP
git commit -m "refactor: inject CSVStorage and CLIUI into main using abstractions"














