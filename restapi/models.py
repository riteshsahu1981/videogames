from restapi import mysql
from flask_restful import  Resource
from flask import Response
from flask import render_template, url_for, flash, redirect, request, abort
import json

class GamesApi(Resource):
	def get(self, method_name, limit="10"):
	 
		if method_name == "sales": return self.sales(limit)
		elif method_name == "gamesreleases": return self.gamesreleases()
		elif method_name == "years": return self.years()
		elif method_name == "getgamesage": return self.getgamesage()
		elif method_name == "age": return self.age()
		elif method_name == "genre": return self.genre()
		elif method_name == "generegame": return self.generegame()
		else: return self.foo()
			
	def sales(self, limit):
		cur = mysql.connection.cursor()
		cur.execute('select publisher, round(sum(global_sales),2) as total_sales \
						from sales group by publisher  order by  sum(global_sales) desc limit ' + limit)
		row_headers=[x[0] for x in cur.description]
		print(row_headers[0])
		rv = cur.fetchall()
		json_data=[]
		for result in rv:
			json_data.append(dict(zip(row_headers,result)))
		return Response(json.dumps(json_data),  mimetype='application/json')	 
		#return Response(json.dumps(json_data),  mimetype='application/json', headers={'Access-Control-Allow-Origin': '*', "Access-Control-Allow-Methods":"GET, POST PUT, DELETE, OPTIONS", "Access-Control-Allow-Header":"Content-Type"})
		return json.dumps(json_data)
	def gamesreleases(self):
		year = request.args.get('year', "2018")
		cur = mysql.connection.cursor()
		cur.execute("SELECT QueryName, ReleaseDate FROM `features` WHERE `ReleaseYear` = '%s'  " %(year))
		row_headers=[x[0] for x in cur.description]
		#print(row_headers[0])
		rv = cur.fetchall()
		json_data=[]
		for result in rv:
			json_data.append(dict(zip(row_headers,result)))
			 
		return Response(json.dumps(json_data),  mimetype='application/json' )
	def years(self):
		cur = mysql.connection.cursor()
		cur.execute("SELECT distinct ReleaseYear FROM `features` WHERE `ReleaseYear` <> '0000' order by ReleaseYear desc " )
		row_headers=[x[0] for x in cur.description]
		#print(row_headers[0])
		rv = cur.fetchall()
		json_data=[]
		for result in rv:
			json_data.append(dict(zip(row_headers,result)))
			 
		return Response(json.dumps(json_data),  mimetype='application/json' )
	def getgamesage(self):
		age = request.args.get('age', "18")
		cur = mysql.connection.cursor()
		cur.execute("SELECT QueryName, ReleaseDate FROM `features` WHERE `RequiredAge` = '%s'  " %(age))
		row_headers=[x[0] for x in cur.description]
		rv = cur.fetchall()
		json_data=[]
		for result in rv:
			json_data.append(dict(zip(row_headers,result)))
			 
		return Response(json.dumps(json_data),  mimetype='application/json' )
	
	def age(self):
		cur = mysql.connection.cursor()
		cur.execute("SELECT distinct RequiredAge FROM `features` WHERE `RequiredAge` <> '0' order by RequiredAge desc " )
		row_headers=[x[0] for x in cur.description]
		rv = cur.fetchall()
		json_data=[]
		for result in rv:
			json_data.append(dict(zip(row_headers,result)))
			 
		return Response(json.dumps(json_data),  mimetype='application/json' )
		
	def genre(self):
		cur = mysql.connection.cursor()
		cur.execute("SELECT distinct genre FROM `sales`  order by genre asc " )
		row_headers=[x[0] for x in cur.description]
		rv = cur.fetchall()
		json_data=[]
		for result in rv:
			json_data.append(dict(zip(row_headers,result)))
			 
		return Response(json.dumps(json_data),  mimetype='application/json' )
	def generegame(self):
		genre = request.args.get('genre', "Action")
		cur = mysql.connection.cursor()
		cur.execute("SELECT QueryName, ReleaseDate FROM `features` WHERE `GenreIs%s` = 'True'  " %(genre))
		row_headers=[x[0] for x in cur.description]
		rv = cur.fetchall()
		json_data=[]
		for result in rv:
			json_data.append(dict(zip(row_headers,result)))
			 
		return Response(json.dumps(json_data),  mimetype='application/json' )		
	def foo(self):
	 return "tesst"