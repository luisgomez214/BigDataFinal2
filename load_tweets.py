import nltk
import random
from nltk.corpus import words

# Download the NLTK corpus data (run this line only once)
nltk.download('words')

# Get a list of English words from the NLTK words corpus
word_list = words.words()

# Create a list of numbers from 0 to 9
numbers = list(range(10))

# Generate a list of random words
random_words = random.sample(word_list, 10)  # You can specify the number of words you want

# Combine the random words and numbers into a single list
alphanumeric_list = random_words + numbers

# Shuffle the list to randomize the order
random.shuffle(alphanumeric_list)

def generate_users(num_users):
    for i in tqdm(range(num_users), desc="Generating Users"):
        user_id = i + 1
        
        # Generate a random username using a random word from word_list
        random_word = random.choice(word_list)
        random_suffix = str(random.randint(1, 9999))  # Optional: add a random suffix for uniqueness
        username = random_word + random_suffix
        
        # Generate a random password using random words and numbers
        password = (
            random.choice(word_list)  # Random word from the list
            + str(random.randint(0, 9))  # Random digit
            + random.choice(word_list)  # Another random word
        )
        
        age = random.randint(18, 80)
        
        # Execute the insert command with the generated data
        connection.execute(
            "INSERT INTO users (username, password, age) VALUES (%s, %s, %s)",
            (username, password, age)
        )
        
        print(f"user {i + 1}: username = {username}, password = {password}, age = {age}")



# Function to generate random users
def generate_users(num_users):
    for i in tqdm(range(num_users), desc="Generating Users"):
        user_id = i + 1
        username = random_words  # Adjust length as needed
        password = generate_random_alphanumeric(12)  # Adjust length as needed
        age = random.randint(18, 80)
        connection.execute("INSERT INTO users (username, password, age) VALUES (%s, %s, %s)", (username, password, age))
        print("user",i)
