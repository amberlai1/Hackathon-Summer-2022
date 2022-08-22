import pandas as pd


url = "https://raw.githubusercontent.com/Rochester-Biomedical-DS/Hackathon-Summer-2022/main/prediction/prediction.csv"
download = pd.read_csv('https://raw.githubusercontent.com/Rochester-Biomedical-DS/Hackathon-Summer-2022/main/test_data/features_test.tsv', sep='\t')
train = pd.read_csv('https://raw.githubusercontent.com/Rochester-Biomedical-DS/Hackathon-Summer-2022/main/train_data/features_train.tsv', sep ='\t')
print(download.columns)
print (train.head)