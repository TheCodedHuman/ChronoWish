from datetime import date
from Assets.MONTHS import months


def calc_age(year_of_birth: int) -> int:
    """Fetches current year, subtracts it with user's year of birth and returns an integer"""

    if not isinstance(year_of_birth, (int, float)): 
        raise TypeError(f"{year_of_birth} is not integer type, its of type: {type(year_of_birth)}")

    cur_year = date.today().year
    return (cur_year - year_of_birth)            # maybe sqlite either stores or returns values in string datatype


def get_dob(d, m, y) -> str:
    month = months.get(m)
    if not month: return None
    return f"{d:>0} {month.capitalize()} {y}"


class ReorderBirthdayData:
    def __init__(self, data: list[tuple], ui_cols: list[str], debug: bool = False):
        self.ui_cols = tuple(s.lower() for s in ui_cols)        # ("uid", "dob", "name", "age") or n! => non-repeating combination
        self.static_db_cols = ("uid", "name", "dob", "age")     # btw, db_cols are ("uid", "name", "day", "month", "year")
        self.debug = debug
        self.relation = self.find_col_order_relation()
        self.data = self.preprocess_data(data)


    def find_col_order_relation(self) -> list[int]:
        """This function try connecting each column of ui with the column of db, returning a list like [1, 0, 3, 2]"""

        col_juggle_relation: list[int] = []                  

        try:
            for col in self.static_db_cols:
                
                if col in self.ui_cols:
                    col_juggle_relation.append(self.ui_cols.index(col))

                else:
                    if self.debug:  
                        print(f"Warning: {col} not found in ui_cols")

        except Exception as e:
            print("Exception occured:", e)      # even this will return empty list

        else:
            if self.debug: 
                print(f"Relation found successfully!: {col_juggle_relation}")
            
        return col_juggle_relation


    def preprocess_data(self, data: list[tuple]) -> list[tuple]:
        """it converges the data from database in the order the ui to be ordered and arranged
        like if db returns ("uid", "name", "day", "month", "year")
        then it will turn the data to ("uid", "dob", "name", "age")"""

        pre_processed_data = []

        for row in data:            # row is a iterable here like tuple or list

            uid: str = row[0]
            name: str = row[1]
            dob: str = get_dob(row[-3],     # day
                               row[-2],     # month         # sqlite is maybe already giving
                               row[-1])     # year
            age:int = calc_age(row[-1])

            restructured_data = (uid, name, dob, age)
            pre_processed_data.append(restructured_data)

        if self.debug: print(f"Pre-Processed Data:{pre_processed_data}")
        return pre_processed_data
    
    
    def reorder_data(self) -> list[tuple]:           # main function that returns the data back to ResultSection
        """This understands the index order of col_map, and based on that re-places the column that are being sent to ui/resultSection"""

        new_data = []

        for row in self.data:

            new_row = [None] * len(self.relation)
            
            for index, item in zip(self.relation, row):
                new_row[index] = item

            new_data.append(tuple(new_row))

        if self.debug: print(f"New Re-Strutured Data:{new_data}\n")
        return new_data


