import json

def get_scores():
    with open("src/scores/scores.json") as file:
        data = file.read()
    return json.loads(data)

def save_scores(score):
    scores = get_scores()
    scores.append(score)
    
    with open("src/scores/scores.json", "w") as file:
        json.dump(scores, file)