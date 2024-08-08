from flask import Flask, request, jsonify, redirect, url_for, render_template
from finalProjectCreds import Creds
from finalProjectSQL import create_connection, execute_query, execute_read_query

app = Flask(__name__)

creds = Creds()  # Creates an instance of the Creds class

@app.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']

    # Check if the username and password are correct
    if username == creds.userLog and password == creds.userPass:
        # Redirect to a dashboard page upon successful login
        return 'NICE UR IN'
    else:
        # Display an error message for invalid credentials
        return 'Invalid username or password. Please try again.'

# read captain(s)
@app.route('/api/captain/all', methods=['GET'])
def getCaptain():

    #connection to the database is established
    conn = create_connection(creds.host, creds.user, creds.password, creds.dbname)

    #sql statement that outputs all entries of the table
    sql = "select * from captain"

    #list that hold all entries accessed from the database
    cap = execute_read_query(conn, sql)
    return jsonify(cap)

# Add a captain as POST method
@app.route('/api/captain/add', methods=['POST'])
def addCap():

    #variables to hold the new data that is going to be inserted into the table
    request_data = request.get_json()
    newid = request_data['id']
    newFname = request_data['firstname']
    newLname = request_data['lastname']
    newCapank = request_data['caprank']
    newHomeplanet = request_data['homeplanet']

    conn = create_connection(creds.host, creds.user, creds.password, creds.dbname)
    # SQL statement to insert the values into the table
    sql = "insert into captain(id, firstname, lastname, caprank, homeplanet) values ('%s', '%s', '%s', '%s', '%s')" % (newid, newFname, newLname, newCapank, newHomeplanet)
    
    #executing the qeury to add an entry into the table
    execute_query(conn, sql)
    return 'Add new Captain successful'


# Function to update a captain entry by the captain ID
@app.route('/api/captain/<int:id>', methods=['PUT'])
def updateCap(id):
    updatedCap = request.json

    #connection to the database is established
    connection = create_connection(creds.host, creds.user, creds.password, creds.dbname)
    if connection is None:
        return jsonify({'Connection Failed'}), 500
    
    #sql to update the data in the table
    sql = f"""
        UPDATE captain 
        SET firstname = '{updatedCap['firstname']}', 
            lastname = '{updatedCap['lastname']}', 
            caprank = {updatedCap['caprank']}, 
            homeplanet = '{updatedCap['homeplanet']}'
        WHERE id = {id}
    """

    #function call to execute the statement stored in the variable
    execute_query(connection, sql)
    connection.close()
    return jsonify({'Captain entry updated successfully'})


# Delete a captain entry with DELETE method
@app.route('/api/captain/delete', methods=['DELETE'])
def deleteCap():
    request_data = request.get_json()
    idtodelete = request_data['id']

    #connection to the datbase is established
    conn = create_connection(creds.host, creds.user, creds.password, creds.dbname)

    #sql statement to delete an entry by the id
    sql = "delete from captain where id = %s" % (idtodelete)

    #function call to execute the query
    execute_query(conn, sql)

    return 'Success'


######################################### spacechip section ###########################################


#read/get spaceships
@app.route('/api/spaceship/all', methods=['GET'])
def getSpaceship():

    #connection to the database is established
    conn = create_connection(creds.host, creds.user, creds.password, creds.dbname)

    #sql statement that outputs all entries of the table
    sql = "select * from spaceship"

    #list that hold all entries accessed from the database
    ship = execute_read_query(conn, sql)
    return jsonify(ship)

# Add a spaceship as POST method
@app.route('/api/spaceship/add', methods=['POST'])
def addShip():

    #variables to hold the new data that is going to be inserted into the table
    request_data = request.get_json()
    newid = request_data['id']
    newMaxweight = request_data['maxweight']
    newCapid = request_data['captainid']
    
    conn = create_connection(creds.host, creds.user, creds.password, creds.dbname)
    # SQL statement to insert the values into the table
    sql = "insert into spaceship(id, maxweight, captainid) values ('%s', '%s', '%s')" % (newid, newMaxweight, newCapid)
    
    #executing the qeury to add an entry into the table
    execute_query(conn, sql)
    return 'Add new Spaceship successful'

# Function to update a captain entry by the captain ID
@app.route('/api/spaceship/<int:id>', methods=['PUT'])
def updateShip(id):
    updatedship = request.json

    #connection to the database is established
    connection = create_connection(creds.host, creds.user, creds.password, creds.dbname)
    if connection is None:
        return jsonify({'Connection Failed'}), 500
    
    #sql to update the data in the table
    sql = f"""
        UPDATE spaceship 
        SET maxweight = '{updatedship['maxweight']}', 
            captainid = '{updatedship['captainid']}'
        WHERE id = {id}
    """

    #function call to execute the statement stored in the variable
    execute_query(connection, sql)
    connection.close()
    return jsonify({'Spaceship entry updated successfully'})


# Delete a spaceship entry with DELETE method
@app.route('/api/spaceship/delete', methods=['DELETE'])
def deleteShip():
    request_data = request.get_json()
    idtodelete = request_data['id']

    #connection to the datbase is established
    conn = create_connection(creds.host, creds.user, creds.password, creds.dbname)

    #sql statement to delete an entry by the id
    sql = "delete from spaceship where id = %s" % (idtodelete)

    #function call to execute the query
    execute_query(conn, sql)

    return 'Success'


################################################# Cargo section ##########################################


#read/get cargo
@app.route('/api/cargo/all', methods=['GET'])
def getcargo():

    #connection to the database is established
    conn = create_connection(creds.host, creds.user, creds.password, creds.dbname)

    #sql statement that outputs all entries of the table
    sql = "select * from cargo"

    #list that hold all entries accessed from the database
    ship = execute_read_query(conn, sql)
    return jsonify(ship)

# Add a cargo as POST method
@app.route('/api/cargo/add', methods=['POST'])
def addcargo():

    #variables to hold the new data that is going to be inserted into the table
    request_data = request.get_json()
    newid = request_data['id']
    newWeight = request_data['weight']
    newCargotype = request_data['cargotype']
    newDeparture = request_data['departure']
    newArrival = request_data['arrival']
    newShipid = request_data['shipid']
    
    conn = create_connection(creds.host, creds.user, creds.password, creds.dbname)
    # SQL statement to insert the values into the table
    sql = "insert into cargo(id, weight, cargotype, departure, arrival, shipid) values ('%s', '%s', '%s')" % (newid, newWeight, newCargotype, newDeparture, newArrival, newShipid)
    
    #executing the qeury to add an entry into the table
    execute_query(conn, sql)
    return 'Add new Cargo successful'

# Function to update a captain entry by the captain ID
@app.route('/api/cargo/<int:id>', methods=['PUT'])
def updatecargo(id):
    updatedCar = request.json

    #connection to the database is established
    connection = create_connection(creds.host, creds.user, creds.password, creds.dbname)
    if connection is None:
        return jsonify({'Connection Failed'}), 500
    
    #sql to update the data in the table
    sql = f"""
        UPDATE cargo 
        SET weight = '{updatedCar['weight']}', 
            cargotype = '{updatedCar['cargotype']}',
            departure = '{updatedCar['departure']}',
            arrival = '{updatedCar['arrival']}',
            shipid = '{updatedCar['shipid']}'
        WHERE id = {id}
    """

    #function call to execute the statement stored in the variable
    execute_query(connection, sql)
    connection.close()
    return jsonify({'Spaceship entry updated successfully'})


# Delete a spaceship entry with DELETE method
@app.route('/api/cargo/delete', methods=['DELETE'])
def deletecargo():
    request_data = request.get_json()
    idtodelete = request_data['id']

    #connection to the datbase is established
    conn = create_connection(creds.host, creds.user, creds.password, creds.dbname)

    #sql statement to delete an entry by the id
    sql = "delete from cargo where id = %s" % (idtodelete)

    #function call to execute the query
    execute_query(conn, sql)

    return 'Success'



if __name__ == '__main__':
    app.run(debug=True)
