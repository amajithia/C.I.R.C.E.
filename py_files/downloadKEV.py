import requests
import pandas as pd
from datetime import datetime
import os


kev_url = "https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv"


def download_kev(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"KEV dataset downloaded successfully to {save_path}")
    else:
        print(f"Failed to download KEV dataset: Status code {response.status_code}")


today = datetime.today().strftime('%Y-%m-%d')
save_folder = 'C:/Users/majit/Downloads/kev_datasets'
os.makedirs(save_folder, exist_ok=True) 
save_path = f'{save_folder}/kev_{today}.csv'


download_kev(kev_url, save_path)
