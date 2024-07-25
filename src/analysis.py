import pandas as pd

def run_analysis():
    # Load data
    data = pd.read_csv('data/Housing.csv')
    
    # Perform analysis (e.g., calculate mean)
    mean_value = data['price'].mean()

    return {'mean': mean_value}
