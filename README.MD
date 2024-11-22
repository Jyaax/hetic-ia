# Importer un fichier depuis le cloud

## Étape 1 : Télécharger le fichier depuis Google Drive

1. **Importer le fichier sur Google Drive**  
   Uploadez votre fichier sur Google Drive et assurez-vous d'activer les permissions de lecture en partageant le lien.

2. **Récupérer l'identifiant du fichier**  
   Copiez le lien de partage. Par exemple, si votre lien ressemble à :  
   `https://drive.google.com/file/d/1x_xRse9KXn0M-6a1WlNa6XvWR-HpOjHT/view?usp=drive_link`  
   L'ID du fichier correspond à la portion située entre `/d/` et `/view`.  
   Dans cet exemple, l'ID est : `1x_xRse9KXn0M-6a1WlNa6XvWR-HpOjHT`.

3. **Mettre à jour le script `file_download.py`**  
   Remplacez la valeur de `file_id` dans le fichier `file_download.py` par l'ID récupéré.

4. **Exécuter le script**  
    Lancez la commande suivante pour importer votre fichier :
   ```bash
   python file_download.py
   ```
   Le fichier sera téléchargé et enregistré dans files.

## Étape 2 : Démarrer le chatbot

1. **Lancer le script ollama_script.py**  
   Après avoir téléchargé le fichier, démarrez le chatbot en exécutant :

   ```bash
   python ollama_script.py
   ```

2. **Interagir avec le chatbot**  
   Posez vos questions en lien avec le fichier téléchargé directement dans l'interface.

   Si votre fichier est un peu trop volumineux, la réponse risque d'être longue à arriver.
   C'est le cas du fichier exemple parlant de la théorie des cordes.
