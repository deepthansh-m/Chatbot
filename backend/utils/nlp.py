import spacy
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load('en_core_web_md')


def preprocess_query(query):
    return nlp(query.lower())


def calculate_similarity(query1, query2):
    vec1 = preprocess_query(query1).vector
    vec2 = preprocess_query(query2).vector
    return cosine_similarity([vec1], [vec2])[0][0]


def match_intent(user_query, dataset):
    best_match = None
    highest_similarity = -1

    for question, response in dataset:
        similarity = calculate_similarity(user_query, question)
        if similarity > highest_similarity:
            best_match = response
            highest_similarity = similarity

    return best_match if best_match else "Sorry, I didn't understand that."
