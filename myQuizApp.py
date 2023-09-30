import random
import time

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": "Mars",
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Giraffe", "Whale Shark", "Blue Whale"],
        "answer": "Blue Whale",
    },
    {
        "question": "Who discovered Oxygen?",
        "options": ["Karl William Scheele", "Albert Einstein", "Marie Curie", "Charles Darwin"],
        "answer": "Karl William Scheele",
    },
    {
        "question": "What is the name of the longest river in Africa?",
        "options": ["Niger", "Congo", "Zambezi", "Nile"],
        "answer": "Nile",
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
        "answer": "Canberra",
    },
    {
        "question": "What is the highest mountain in the world?",
        "options": ["Mount Kilimanjaro", "Mount Everest", "Mount Fuji", "Mount McKinley"],
        "answer": "Mount Everest",
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["G", "Ag", "Au", "Pb"],
        "answer": "Au",
    },
    {
        "question": "What is the largest ocean in the world?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean",
    },
    {
        "question": "What is the name of the world's largest coral reef system?",
        "options": ["Great Barrier Reef", "Belize Barrier Reef", "Andros Barrier Reef", "Ap Reef"],
        "answer": "Great Barrier Reef",
    },
    {
        "question": "What is the unit of measurement for electrical resistance?",
        "options": ["Ampere", "Ohm", "Volt", "Watt"],
        "answer": "Ohm",
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Vincent van Gogh"],
        "answer": "Leonardo da Vinci",
    },
    {
        "question": "Which planet in our solar system has the most moons?",
        "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
        "answer": "Jupiter",
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
        "answer": "William Shakespeare"
    },
    {
        "question": "Which gas makes up the majority of Earth's atmosphere?",
        "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"],
        "answer": "Nitrogen"
    },
    {
        "question": "What is the largest organ in the human body?",
        "options": ["Liver", "Skin", "Heart", "Lungs"],
        "answer": "Skin"
    },
    {
        "question": "Which gas is known as laughing gas?",
        "options": ["Oxygen", "Carbon Dioxide", "Methane", "Nitrous Oxide"],
        "answer": "Nitrous Oxide"
    },
    {
        "question": "Who is known as the 'Father of Modern Physics'?",
        "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
        "answer": "Albert Einstein"
    },
    {
        "question": "What is the largest moon in our solar system?",
        "options": ["Io", "Ganymede", "Titan", "Europa"],
        "answer": "Ganymede"
    },
    {
        "question": "What is the largest desert in the world?",
        "options": ["Sahara Desert", "Gobi Desert", "Atacama Desert", "Arabian Desert"],
        "answer": "Sahara Desert"
    },
    {
        "question": "Who was the first Prime Minister of India?",
        "options": ["Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "Indira Gandhi", "Mohandas Karamchand Gandhi"],
        "answer": "Jawaharlal Nehru"
    },
    {
        "question": "Which river is often referred to as the 'Ganga of the South'?",
        "options": ["Yamuna", "Brahmaputra", "Godavari", "Krishna"],
        "answer": "Godavari"
    },
    {
        "question": "Who is known as the 'Father of the Indian Constitution'?",
        "options": ["Mahatma Gandhi", "Sardar Vallabhbhai Patel", "B.R. Ambedkar", "Jawaharlal Nehru"],
        "answer": "B.R. Ambedkar"
    },
    {
        "question": "What is the national emblem of India?",
        "options": ["Lotus", "Peacock", "Lion Capital of Ashoka", "Tiger"],
        "answer": "Lion Capital of Ashoka"
    },
    {
        "question": "Which mountain range separates India from the rest of Asia?",
        "options": ["Himalayas", "Western Ghats", "Eastern Ghats", "Vindhya Range"],
        "answer": "Himalayas"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Giraffe", "Whale Shark", "Blue Whale"],
        "answer": "Blue Whale",
    },
    {
        "question": "Who composed the Indian national anthem, 'Jana Gana Mana'?",
        "options": ["Rabindranath Tagore", "Sarojini Naidu", "Bankim Chandra Chattopadhyay", "Subhas Chandra Bose"],
        "answer": "Rabindranath Tagore"
    },
    {
        "question": "Which famous leader led the Dandi March as part of the Salt Satyagraha in 1930?",
        "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Subhas Chandra Bose", "Sardar Vallabhbhai Patel"],
        "answer": "Mahatma Gandhi"
    },
    {
        "question": "Which historical monument in India is often called the 'Symbol of Love'?",
        "options": ["Taj Mahal", "Qutub Minar", "Red Fort", "Charminar"],
        "answer": "Taj Mahal"
    },
]

# Initialize a variable to keep track of the score
score = 0

# Shuffle the questions to make them random
random.shuffle(questions)

# Function to display a question and get the user's answer


def ask_question(question_obj):
    print(question_obj["question"])
    for i, option in enumerate(question_obj["options"], start=1):
        print(f"{i}. {option}")

    user_answer = input("Enter the number of your answer (1, 2, 3, 4): ")

    if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
        user_answer = question_obj["options"][int(user_answer) - 1]
        return user_answer
    else:
        print("Invalid input. Please enter a number between 1 and 4.")
        return ask_question(question_obj)


# Set a timer for the entire quiz (e.g., 60 seconds)
quiz_time = 300
start_time = time.time()
end_time = start_time + quiz_time

# Main quiz loop
for question in questions:
    if time.time() > end_time:
        print("Time's up!")
        break

    print("\n" + "=" * 100)
    user_choice = ask_question(question)

    if user_choice == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {question['answer']}")

# Display the final score
print("\n" + "=" * 100)
print(f"Quiz Over! Your Score: {score}/{len(questions)}")
