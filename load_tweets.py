import sqlalchemy
import string
import argparse
import random
import nltk
from tqdm import tqdm
from sqlalchemy.exc import IntegrityError

parser = argparse.ArgumentParser()
parser.add_argument('--db', required=True)
parser.add_argument('--user_rows', default=100)
args = parser.parse_args()

engine = sqlalchemy.create_engine(args.db, connect_args={'application_name': 'load_tweets.py'})
connection = engine.connect()

nltk.download('words')
from nltk.corpus import words
word_list = words.words()
print("hi")
def generate_words(num_words):
    random_words = random.sample(word_list, num_words)
    return random_words

def generate_users(num_users):
    for i in tqdm(range(num_users), desc="Currently Generating and Populating Users"):
        username=''.join(generate_words(2))
        password=''.join(generate_words(3))
        age=random.randint(8,100)
        sql=sqlalchemy.sql.text("""INSERT INTO users (username, password, age) VALUES (:u, :p, :a);""")
        try:
            res = connection.execute(sql, {
                'u': username,
                'p': password,
                'a': age
                })
        except IntegrityError as e:
            print("Could Not Insert User Number: ",i, " Due To Duplication ","Error Message: ", e)

def generate_urls(num_urls):
    for i in tqdm(range(num_urls), desc="Currently Generating and Populating Urls"):
        url=''.join(generate_words(4))
        sql=sqlalchemy.sql.text("""INSERT INTO urls (url) VALUES (:url);""")
        try:
            res = connection.execute(sql, {
                'url': url,
                })
        except IntegrityError as e:
            print("Could Not Insert Url Number" ,i," Due To Duplication ","Error Message: ", e)

def generate_messages(num_messages):
    sql = sqlalchemy.sql.text("""SELECT id FROM users;""")
    res = connection.execute(sql)
    creator_ids = [tup[0] for tup in res.fetchall()]    
    for i in tqdm(range(num_messages), desc="Currently Generating and Populating Messages"):
        creator_id = random.choice(creator_ids)
        message=''.join(generate_words(5))
        sql=sqlalchemy.sql.text("""INSERT INTO messages (creator_id, message) VALUES (:ci, :m);""")
        try:
            res = connection.execute(sql, {
                'ci': creator_id,
                'm': message
                })
        except IntegrityError as e:
            print("Could Not Insert Message: ",i," Due To Duplication ","Error Message: ", e)

generate_users(int(args.user_rows))
generate_urls(int(args.user_rows))
generate_messages(10 * int(args.user_rows))

connection.close()
