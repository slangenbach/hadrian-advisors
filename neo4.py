def query_neo4j(query, conn, user, password):
    """
    Connect to remote Neo4j database, execute query and print results
    :param query: query string to be executed
    :param conn: connection string
    :param user: username
    :param password: password
    :return: print records returned by query
    """
    from neo4j.v1 import GraphDatabase, basic_auth

    # connect to neo4j
    driver = GraphDatabase.driver(conn, auth = basic_auth(user, password))
    session = driver.session()

    # run query
    result = session.run(query)

    # print result
    return [print(r) for r in result]

# define connection
conn = "bolt://localhost:7687"
user = "neo4j"
password = "kot67neo4j"

# define query
query = "MATCH(p:Person{name:'Tom Hanks'})-[:ACTED_IN]-(m)" + "RETURN p, m"

# execute query
query_neo4j(query, conn, user, password)