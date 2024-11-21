import requests

def download_file_from_google_drive(file_id):
    url = f'https://drive.google.com/uc?id={file_id}&export=download'
    response = requests.get(url)

    if response.status_code == 200:
        with open(f"files/downloaded-file.txt", 'wb') as f:
            f.write(response.content)
        print(f"File downloaded successfully")
    else:
        print(f"File couldn't be downlaoded")

file_id = '1x_xRse9KXn0M-6a1WlNa6XvWR-HpOjHT'
download_file_from_google_drive(file_id)