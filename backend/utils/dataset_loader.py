import pandas as pd

def load_dataset(filepath):
    data = pd.read_csv(filepath)
    dataset = list(zip(data['question'], data['answer']))
    return dataset
