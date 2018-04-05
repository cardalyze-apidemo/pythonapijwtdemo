from flask import Flask, jsonify, request
from model.restaurant import Restaurant, RestaurantSchema
from model.entree import Entree
from flask_jwt_extended import (JWTManager, create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'apidemosecretkey' # Change this!
jwt = JWTManager(app)
# Provide a method to create access tokens. The create_access_token()
# function is used to actually generate the token, and you can return
# it to the caller however you choose.
@app.route('/login', methods=['POST'])
def login():
	if not request.is_json:
		return jsonify({"msg": "Missing JSON in request"}), 400
	username = request.json.get('username', None)
	password = request.json.get('password', None)
	if not username:
		return jsonify({"msg": "Missing username parameter"}), 400
	if not password:
		return jsonify({"msg": "Missing password parameter"}), 400

        #This is where you can verify the user and password using internal database
        #or AD/LDAP
	if username != 'test' or password != 'test':
		return jsonify({"msg": "Bad username or password"}), 401

	# Identity can be any data that is json serializable
	access_token = create_access_token(identity=username)
	return jsonify(access_token=access_token), 200

@app.route('/restaurants')
@jwt_required
def get_restaurants():

    entree1 = Entree(1, 'Chicken Marsala', 'Italian', True)
    entree2 = Entree(2, 'Chicken Florentine', 'Italian', True);
    entree3 = Entree(3, 'Fettucini Alfredo', 'Italian', True);
    entree4 = Entree(4, 'Pepperoni Pizza', 'Italian', True);
    
    entree5 = Entree(5, 'Chicken Tikka Masala', 'Indian', True);
    entree6 = Entree(6, 'Chicken Kadahi', 'Indian', True);
    entree7 = Entree(7, 'Tandoori Chicken', 'Indian', True);
    entree8 = Entree(8, 'Butter Naan', 'Indian', True);
    entree9 = Entree(9, 'Rogan Josh', 'Indian', True);
	
    entree10 = Entree(10, 'Avocado Burger', 'American', True);
    entree11 = Entree(11, 'Chicken Wings', 'American', True);
    entree12 = Entree(12, 'Fillet Mignon', 'American', True);
    
    restaurant1 = Restaurant('1', 'Ippolitos', 'Atlanta', True, 4) 
    restaurant1.addEntree(entree1)
    restaurant1.addEntree(entree2)
    restaurant1.addEntree(entree3)
    restaurant1.addEntree(entree4)

    restaurant2 = Restaurant('2', 'Maharaja', 'Dunwoody', True, 5)
    restaurant2.addEntree(entree5)
    restaurant2.addEntree(entree6)
    restaurant2.addEntree(entree7)
    restaurant2.addEntree(entree8)
    restaurant2.addEntree(entree9)

    restaurant3 = Restaurant('3', 'Friends', 'Suwanee', True, 5)
    restaurant3.addEntree(entree10)
    restaurant3.addEntree(entree11)
    restaurant3.addEntree(entree12) 

    restaurants = [
                    restaurant1, restaurant2, restaurant3
                  ]
    schema = RestaurantSchema(many=True)
    restaurants = schema.dump(restaurants)
    return jsonify(restaurants)

