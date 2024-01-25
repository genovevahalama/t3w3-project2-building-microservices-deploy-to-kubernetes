import mysql.connector
import requests

def insert_characters_from_api():
    db_config = {
        "host": "localhost",
        "user": "admin",
        "password": "admin",
        "database": "hogwarts",
    }
    api_url = "https://hp-api.onrender.com/api/characters/staff"
    
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("TRUNCATE TABLE Characters")
        response = requests.get(api_url)
        data = response.json()
        for character in data:
            cursor.execute(
                "INSERT INTO Characters (name, species, gender, house, dateOfBirth, yearOfBirth, wizard, ancestry, eyeColour, hairColour, patronus, hogwartsStudent, hogwartsStaff, actor, alive, image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    character.get("name", None),
                    character.get("species", None),
                    character.get("gender", None),
                    character.get("house", None),
                    character.get("dateOfBirth", None),
                    character.get("yearOfBirth", None),
                    character.get("wizard", None),
                    character.get("ancestry", None),
                    character.get("eyeColour", None),
                    character.get("hairColour", None),
                    character.get("patronus", None),
                    character.get("hogwartsStudent", None),
                    character.get("hogwartsStaff", None),
                    character.get("actor", None),
                    character.get("alive", None),
                    character.get("image", None),
                ),
            )
        conn.commit()
        cursor.close()
        conn.close()
        print("Data inserted successfully into the MySQL database.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")


def insert_spells_from_api():
    db_config = {
        "host": "localhost",
        "user": "admin",
        "password": "admin",
        "database": "hogwarts",
    }
    api_url = "https://hp-api.onrender.com/api/spells"
    
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("TRUNCATE TABLE Spells")
        response = requests.get(api_url)
        data = response.json()
        for spell in data:
            cursor.execute(
                "INSERT INTO Spells (name, description) VALUES (%s, %s)",
                (
                    spell.get("name", None),
                    spell.get("description", None),
                ),
            )
        conn.commit()
        cursor.close()
        conn.close()
        print("Data inserted successfully into the MySQL database.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")

insert_characters_from_api()
insert_spells_from_api()