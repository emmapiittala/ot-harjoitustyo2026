'''handle scores'''
import json

def get_scores():
    '''Return saved scores from json file'''
    with open("src/scores/scores.json", encoding="utf=8") as file:
        data = file.read()
    return json.loads(data)

def save_scores(username, score):
    '''Save player username annd score to json file'''
    scores = get_scores()
    scores.append({
        "username": username,
        "score": score
    })

    with open("src/scores/scores.json", "w", encoding="utf=8") as file:
        json.dump(scores, file)
