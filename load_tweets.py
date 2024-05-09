import string
import sqlalchemy
import random
import nltk
import argparse
from sqlalchemy.exc import IntegrityError
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--db', required=True)
parser.add_argument('--user_rows', default=100)
args = parser.parse_args()



engine = sqlalchemy.create_engine(args.db, connect_args={'application_name': 'load_tweets.py'})
connection = engine.connect()

nltk.download('words')
from nltk.corpus import words
word_list = words.words()

#print("hi")

def generate_words(num_words):
    random_words = random.sample(word_list, num_words)
    return random_words

def generate_users(num_users):
    for i in tqdm(range(num_users), desc="Getting users"):
        username=''.join(generate_words(4))
        password=''.join(generate_words(4))
        age=random.randint(1,100)
        connection.execute("INSERT INTO users (username, password, age) VALUES (%s, %s, %s)", (username, password, age))
        print("hi user",i)

def generate_urls(num_urls):
    for i in tqdm(range(num_urls), desc="Getting the urls"):
        url=''.join(generate_words(4))
        try:
            connection.execute("INSERT INTO urls (url) VALUES (%s)", (url))
            print('url', i) 
        except IntegrityError as e:
            print("No url because of dupe")

def generate_messages(num_messages):
    sql = sqlalchemy.sql.text("""SELECT id FROM users;""")
    res = connection.execute(sql)
    creator_ids = [tup[0] for tup in res.fetchall()]    
    for i in tqdm(range(num_messages), desc="Getting messages"):
        creator_id = random.choice(creator_ids)
        message=''.join(generate_words(5))
        try:
            connection.execute("INSERT INTO messages (creator_id, message) VALUES (%s, %s)", (creator_id, message))
        except IntegrityError as e:
            print("No message becasue of dupe")

generate_users(int(args.user_rows))
generate_urls(int(args.user_rows))
generate_messages(10 * int(args.user_rows))

#generate_users(1000000)
#generate_urls(1000000)
#generate_messages(10000000)


connection.close()
