import requests

def download_file_from_google_drive(file_id):
    url = f'https://drive.google.com/uc?id={file_id}&export=download'
    response = requests.get(url)

    if response.status_code == 200:
        # Sauvegarde du fichier dans le dossier 'files' avec le même nom que l'ID du fichier
        with open(f"files/{file_id}.txt", 'wb') as f:
            f.write(response.content)
        print(f"File downloaded successfully.")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

# Remplacez par votre ID de fichier Google Drive
file_id = '1J9-xfK3HHHykRSCktKf2hdoVKpKKs7zo'
download_file_from_google_drive(file_id)