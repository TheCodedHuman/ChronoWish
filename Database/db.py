# Here we are fabricating database script for ChronoWish

# Imports
import sqlite3
from pathlib import Path
from Utils.generator_utils import generate_uid
from Assets.TABLES import TABLES

# Classed
class ChronoDB:

    SAFE_TABLES = {"birthdays"}
    SAFE_FIELDS = {"uid", "name", "day", "month"}

    def __init__(self, path: str | Path = "chronowish.db"):
        self.db = sqlite3.connect(path)
        self.cursor = self.db.cursor()
        self.create_tables('birthdays')


    def close(self): 
        """Closes the database"""
        self.db.close()


    def create_tables(self, table_name: str):
        """Reusable function that creates table by taking name to find the query in the TABLES dictionary"""

        if table_name not in TABLES:
            raise ValueError(f"Unknown table: {table_name}")
        
        self.cursor.execute(TABLES[table_name])
        self.db.commit()


    def check_existence(self, find, field_name, table_name = "birthdays") -> bool:                          # can be enhancements
        """Checks if a value exists in a specific field of a table"""

        # Input sanitization (table_name and field_name)
        if table_name not in self.SAFE_TABLES: raise ValueError("Unsafe table name")
        if field_name not in self.SAFE_FIELDS: raise ValueError("Unsafe field name")

        query = f"SELECT 1 FROM {table_name} WHERE {field_name} = ? LIMIT 1"
        result = self.cursor.execute(query, (find,)).fetchone()

        return result is not None                                                                           # returns False if empty set


    def push_birthday(self, name: str, day: int, month: int):
        """Inserts a birthday entry with a unique UID"""

        uid = generate_uid()                                                                                # generate unique_id

        while self.check_existence(uid, "uid"):                                                             # keep checking if that uid exists in db
            uid = generate_uid()
        
        query = "INSERT INTO birthdays (uid, name, day, month) VALUES (?, ?, ?, ?)"                         # t-strings may also be used
        self.cursor.execute(query, (uid, name, day, month))

        self.db.commit()
        return uid
        

# Main
def main():
    db_path = Path(__file__).parent / "chronowish.db"
    db = ChronoDB(db_path)
    db.close()
main()

