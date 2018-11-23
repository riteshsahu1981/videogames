from restapi import mysql
from flask_restful import  Resource
from flask import Response
import json

class GamesApi(Resource):
	def get(self, method_name, limit="10"):
		if method_name == "sales": return self.sales(limit)
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
			 
		return Response(json.dumps(json_data),  mimetype='application/json', headers={'Access-Control-Allow-Origin': '*', "Access-Control-Allow-Methods":"GET, POST PUT, DELETE, OPTIONS", "Access-Control-Allow-Header":"Content-Type"})
		return json.dumps(json_data)
	
	def foo(self):
	 return "tesst"