import MySQLdb

mydb = MySQLdb.connect(host='127.0.0.1',
    user='root',
    passwd='',
    db='videogame')
cursor = mydb.cursor()
try:
	Query = """ALTER TABLE features DROP  ReleaseYear; ALTER TABLE features DROP  id;"""
	cursor.execute(Query)
	mydb.commit()
except:
	print "Columns not present!!"

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


Query = """ALTER TABLE `features` ADD `id` BIGINT NOT NULL AUTO_INCREMENT FIRST, ADD PRIMARY KEY (`id`);
ALTER TABLE `features` ADD `ReleaseYear` YEAR NULL AFTER `ReleaseDate`;"""
cursor.execute(Query)
mydb.commit()



cursor.close()
print "Done"