import pandas as pd
import requests
import io

url = "https://raw.githubusercontent.com/Rochester-Biomedical-DS/Hackathon-Summer-2022/main/prediction/prediction.csv"
download = requests.get(url).content

df = pd.read_csv(io.StringIO(download.decode('utf-8')))

print(df.head)