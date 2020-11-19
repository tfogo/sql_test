import mysql.connector
import hexdump

# Connect to server
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    use_pure=True)

cnx.database = "foo"

# Get a cursor
cur = cnx.cursor()

# Execute a query
cur.execute("SELECT CURDATE()")

# Fetch one result
row = cur.fetchone()
print("Current date is: {0}".format(row[0]))

cmd = mysql.connector.constants.ServerCmd.FIELD_LIST
arg = bytearray('bar'.encode('utf-8'))
arg.append(0)
print(arg)
res = cnx._send_cmd(cmd, arg)

print("Response is: \n")
hexdump.hexdump(res)

# Close connection
cnx.close()