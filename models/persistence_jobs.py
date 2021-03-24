import jaydebeapi
from databases_schema.jobs_schema import JobsSchema


# Create the jobs table, will be executes before our app start
def initialize():
    _execute(("CREATE TABLE IF NOT EXISTS jobs ("
              "  id INT PRIMARY KEY AUTO_INCREMENT,"
              "  company_name VARCHAR NOT NULL,"
              "  title VARCHAR NOT NULL"
              "  skills VARCHAR)")
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

    # takes the merged result and converts them to JobsSchema objects that Flask can further process.
    return JobsSchema().load(column_and_values, many=True)



# database functions:

#Get a list of all jobs
def get_all():
    return _execute("SELECT * FROM jobs", return_result=True)


#Get a list of skills by job title name
def get(name):
    return _execute("SELECT skills FROM jobs WHERE name = {}".format(name), return_result=True)


