import numpy as np
import pandas as pd

class GameDataProcessor:
    def __init__(self, data):
        self.data = data

    def clean_data(self):
        self.data.dropna(inplace=True)  # Remove missing values
        self.data = self.data[self.data['score'] >= 0]  # Filter out negative scores

    def normalize_scores(self):
        score_max = self.data['score'].max()
        score_min = self.data['score'].min()
        self.data['normalized_score'] = (self.data['score'] - score_min) / (score_max - score_min)  # Normalize scores to [0, 1]

    def process(self):
        self.clean_data()  # Clean the input data
        self.normalize_scores()  # Normalize scores

    def get_processed_data(self):
        return self.data


# Example usage:
if __name__ == '__main__':
    sample_data = pd.DataFrame({
        'player': ['Alice', 'Bob', 'Charlie', 'David'],
        'score': [100, np.nan, -50, 75]
    })
    processor = GameDataProcessor(sample_data)
    processor.process()
    print(processor.get_processed_data())
