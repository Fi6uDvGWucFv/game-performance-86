import json

class GameDataProcessor:
    def __init__(self, data):
        self.data = data

    def validate_data(self):
        if not isinstance(self.data, dict):
            raise ValueError('Data must be a dictionary')
        if 'scores' not in self.data:
            raise KeyError('Missing key: scores')
        if not isinstance(self.data['scores'], list):
            raise ValueError('Scores must be a list')

    def calculate_average_score(self):
        self.validate_data()  
        try:
            total = sum(self.data['scores'])
            count = len(self.data['scores'])
            average = total / count
            return average
        except ZeroDivisionError:
            return 'No scores to average'
        except TypeError:
            return 'Scores must be numbers'

    def to_json(self):
        try:
            return json.dumps(self.data)
        except (TypeError, OverflowError) as e:
            return f'Error converting to JSON: {str(e)}'

# Example usage
if __name__ == '__main__':
    game_data = {'scores': [100, 200, 300]}
    processor = GameDataProcessor(game_data)
    print(processor.calculate_average_score())  # Should print the average score
    print(processor.to_json())  # Should print JSON representation of the data