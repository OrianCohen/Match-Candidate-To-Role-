import jaydebeapi
from databases_schema.skills_schema import SkillsSchema


# Create the candidate table, will be executes before our api starts
def initialize():
    _execute(("CREATE TABLE IF NOT EXISTS skills ("
              "  id INT PRIMARY KEY AUTO_INCREMENT,"
              "  skill_name VARCHAR NOT NULL)")
             )


# Connection string and credentials to access the database server
def _execute(query, return_result=None):
    connection = jaydebeapi.connect(
        "org.h2.Driver",
        "jdbc:h2:tcp://localhost:5234/jobs",
        ["JOBS", ""],
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

    # takes the merged result and converts them to ExoplanetSchema objects that Flask can further process.
    return SkillsSchema().load(column_and_values, many=True)


# database functions:

#Get a list of all products in products table
def get_all():
    return _execute("SELECT * FROM skills", return_result=True)


#Get a product by id
def get(name):
    return _execute("SELECT * FROM skills WHERE skill_name = {}".format(name), return_result=True)

