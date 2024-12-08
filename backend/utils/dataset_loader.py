import pandas as pd

def load_dataset(filepath):
    # Load dataset and preprocess
    data = pd.read_csv(filepath)
    dataset = list(zip(data['question'], data['answer']))
    return dataset
