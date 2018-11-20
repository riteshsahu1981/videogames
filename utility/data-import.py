import MySQLdb

mydb = MySQLdb.connect(host='127.0.0.1',
    user='root',
    passwd='root',
    db='videogame')
cursor = mydb.cursor()


cursor.execute("truncate features;")
mydb.commit()
print "Sales table features "

print "Data import started in features table"
# Query = """load data local infile 'games-features.csv' into table features FIELDS TERMINATED BY ',' 
# ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;"""
Query = """load data local infile 'games-features.csv' into table features FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n' ;"""
cursor.execute(Query)
mydb.commit()

cursor.execute("truncate sales;")
mydb.commit()
print "Sales table truncated "

print "Data import started in sales table"
Query = """load data local infile 'vgsales.csv' into table sales FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n' ;"""
cursor.execute(Query)
mydb.commit()

cursor.close()
print "Done"