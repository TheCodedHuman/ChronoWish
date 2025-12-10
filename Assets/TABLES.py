TABLES = {
    "birthdays": """
        CREATE TABLE IF NOT EXISTS birthdays (
            uid TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            day INTEGER NOT NULL,
            month INTEGER NOT NULL
        )
    """
}

