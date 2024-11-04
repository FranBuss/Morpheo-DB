from src.configurations.DatabaseManager import DatabaseManager

db = DatabaseManager()
output = db.select_data("SELECT * FROM JUEGOS")

for i in output:
    print(i)

