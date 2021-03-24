import jaydebeapi
from databases_schema.candidates_schema import CandidatesSchema


# Create the candidate table, will be executes before our app start
def initialize():
    _execute(("CREATE TABLE IF NOT EXISTS candidates ("
              "  id INT PRIMARY KEY AUTO_INCREMENT,"
              "  name VARCHAR NOT NULL,"
              "  phone INT,"
              "  city VARCHAR NOT NULL"
              "  title VARCHAR NOT NULL"
              "  skills VARCHAR)")
             )


# Connection string and credentials to access the database server
def _execute(query, return_result=None):
    connection = jaydebeapi.connect(
        "org.h2.Driver",
        "jdbc:h2:tcp://localhost:5234/candidates",
        ["CAN", ""],
        "../h2-1.4.200.jar")

    cursor = connection.cutsor()
    cursor.execute(query)
    if return_result:
        return_result = _convert_to_schema(cursor)
    cursor.close()
    connection.close()

    return return_result


def _convert_to_schema(cursor):
    # saved in the descriptions field
    column_names = [record[0].lower() for record in cursor.description]
    column_and_values = [dict(zip(column_names, record)) for record in cursor.fetchall()]

    # takes the merged result and converts them to CandidateSchema objects that Flask can further process.
    return CandidatesSchema().load(column_and_values, many=True)


# database functions:


#Get a list of all candidates
def get_all():
    return _execute("SELECT * FROM candidates", return_result=True)


# Get a match candidate by job title
def get(job_title):
    return _execute("SELECT * FROM candidates WHERE title = {}".format(job_title), return_result=True)


