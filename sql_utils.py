import constants
import pyodbc

# Define the connection parameters
server: str = constants.SQL_SERVER
database: str = constants.SQL_DATABASE
username: str = constants.SQL_USER
password: str = constants.SQL_PASSWORD
driver = '{ODBC Driver 18 for SQL Server}'  # Use the latest ODBC driver version

# Create the connection string
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=Yes;Connection Timeout=5;'


def get_crawler_next_match(region: str, server: str) -> int:
    """ Get the next match to be crawled. """
    query: str = f"select max(match_id) from matches where server = '{server}' and region = '{region}'"

    try:
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute(query)


        result = cursor.fetchone()
        cursor.close()
        connection.close()

        return result[0] + 1

    except pyodbc.Error as e:
        print("An error occurred:", e)
        return -1

def get_crawler_next_match_reverse(region: str, server: str) -> int:
    """ Get the next match to be crawled. """
    query: str = f"select min(match_id) from matches where server = '{server}' and region = '{region}'"

    try:
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute(query)


        result = cursor.fetchone()
        cursor.close()
        connection.close()

        return result[0] - 1

    except pyodbc.Error as e:
        print("An error occurred:", e)
        return -1

def write_match(server: str, region: str, match_id: int, result: int) -> None:
    """ Write the match to the database """
    query: str = f"insert into matches (server, region, match_id, result) values ('{server}', '{region}', {match_id}, {result})"

    try:
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()

    except pyodbc.Error as e:
        print("An error occurred:", e)
        return -1

if __name__ == "__main__":
    # When called without being a module, test the most common functions.
    region: str = "europe"
    server: str = "euw1"

    print (get_crawler_next_match(region, server))
