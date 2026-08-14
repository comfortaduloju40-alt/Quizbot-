"""
Built-in question bank. Add more entries here any time — each is a dict
with 'question', 'options' (2-10 items), 'correct_index', and 'category'.
"""

import random

QUESTIONS = [
    {"question": "What is the capital of Japan?", "options": ["Seoul", "Tokyo", "Beijing", "Bangkok"], "correct_index": 1, "category": "Geography"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Jupiter", "Mars", "Saturn"], "correct_index": 2, "category": "Science"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"], "correct_index": 1, "category": "Literature"},
    {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "correct_index": 3, "category": "Geography"},
    {"question": "How many continents are there?", "options": ["5", "6", "7", "8"], "correct_index": 2, "category": "Geography"},
    {"question": "What gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], "correct_index": 1, "category": "Science"},
    {"question": "Which country hosted the 2016 Summer Olympics?", "options": ["China", "UK", "Brazil", "Russia"], "correct_index": 2, "category": "Sports"},
    {"question": "What is the chemical symbol for gold?", "options": ["Go", "Gd", "Au", "Ag"], "correct_index": 2, "category": "Science"},
    {"question": "Who painted the Mona Lisa?", "options": ["Michelangelo", "Leonardo da Vinci", "Raphael", "Donatello"], "correct_index": 1, "category": "Art"},
    {"question": "What is the smallest prime number?", "options": ["0", "1", "2", "3"], "correct_index": 2, "category": "Math"},
    {"question": "Which language has the most native speakers worldwide?", "options": ["English", "Hindi", "Mandarin Chinese", "Spanish"], "correct_index": 2, "category": "General"},
    {"question": "What is the longest river in the world?", "options": ["Amazon", "Nile", "Yangtze", "Mississippi"], "correct_index": 1, "category": "Geography"},
    {"question": "In which year did World War II end?", "options": ["1943", "1945", "1947", "1950"], "correct_index": 1, "category": "History"},
    {"question": "What is the powerhouse of the cell?", "options": ["Nucleus", "Ribosome", "Mitochondria", "Golgi apparatus"], "correct_index": 2, "category": "Science"},
    {"question": "Which sport uses the term 'love' for zero points?", "options": ["Cricket", "Tennis", "Golf", "Badminton"], "correct_index": 1, "category": "Sports"},
    {"question": "What is the currency of Japan?", "options": ["Won", "Yuan", "Yen", "Ringgit"], "correct_index": 2, "category": "General"},
    {"question": "How many bones are in the adult human body?", "options": ["186", "206", "226", "246"], "correct_index": 1, "category": "Science"},
    {"question": "Which planet has the most moons?", "options": ["Jupiter", "Saturn", "Uranus", "Neptune"], "correct_index": 1, "category": "Science"},
    {"question": "Who developed the theory of relativity?", "options": ["Isaac Newton", "Niels Bohr", "Albert Einstein", "Galileo Galilei"], "correct_index": 2, "category": "Science"},
    {"question": "What is the tallest mountain in the world?", "options": ["K2", "Kangchenjunga", "Mount Everest", "Lhotse"], "correct_index": 2, "category": "Geography"},
]


def get_random_question() -> dict:
    return random.choice(QUESTIONS)
