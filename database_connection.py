class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        self.connected = True
        print(f"Connected to the Databse {self.db_name}") 
        return self

    def __exit__(self,exc_type,exc_value,traceback):
        self.connected = False
        print(f"Disconnected from the Database {self.db_name}") 
        # Handle any exception  
        if exc_type:
            print(f"Exception Occurs {exc_value}")
        return True  
    

with DatabaseConnection("ExampleDB") as db:
    print(f"Is Connected? {db.connected}")