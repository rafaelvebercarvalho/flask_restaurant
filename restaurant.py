from flask import Flask, render_template
app = Flask(__name__)


# Dumb db
# Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}


restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name': 'Blue Burgers', 'id': '2'}, {'name': 'Taco Hut', 'id': '3'}]


# Fake Menu Items
items = [
 {'name': 'Cheese Pizza', 'description': 'made with fresh cheese', 'price': '$5.99', 'course': 'Entree', 'id': '1'},
 {'name': 'Chocolate Cake', 'description': 'made with Dutch Chocolate', 'price': '$3.99', 'course': 'Dessert', 'id': '2'},
 {'name': 'Caesar Salad', 'description': 'with fresh organic vegetables', 'price': '$5.99', 'course': 'Entree', 'id': '3'},
 {'name': 'Iced Tea', 'description': 'with lemon', 'price': '$.99', 'course': 'Beverage', 'id': '4'},
 {'name': 'Spinach Dip', 'description': 'creamy dip with fresh spinach', 'price': '$1.99', 'course': 'Appetizer', 'id': '5'}]
item = {'name': 'Cheese Pizza', 'description': 'made with fresh cheese', 'price': '$5.99', 'course': 'Entree', 'id': '1'}


@app.route("/")
@app.route("/restaurant/")
def showRestaurants():
    # return "Pagina que vai mostrar todos os restaurantes"
    return render_template('restaurants.html', restaurants=restaurants)


@app.route("/restaurant/new")
def newRestaurants():
    # return "Pagina para criar novos resturantes"
    return render_template('newRestaurants.html')


@app.route("/restaurant/<int:restaurant_id>/edit")
def editRestaurants(restaurant_id):
    # return "Pagina para editar os resturantes %s" % restaurant_id
    return render_template('editRestaurants.html', restaurant=restaurant)


@app.route("/restaurant/<int:restaurant_id>/delete")
def deleteRestaurants(restaurant_id):
    # return "Pagina para deletar os resturantes %s" % restaurant_id
    return render_template('deleteRestaurants.html', restaurants=restaurants)


@app.route("/restaurant/<int:restaurant_id>")
@app.route("/restaurant/<int:restaurant_id>/menu")
def showMenu(restaurant_id):
    # return "Pagina que vai mostrar o menu do resturante %s" % restaurant_id
    return render_template('menu.html', restaurants=restaurants)


@app.route("/restaurant/<int:restaurant_id>/menu/new")
def newMenuItem(restaurant_id):
    # return "Pagina para criar um novo menu %s" % restaurant_id
    return render_template('newMenuItem.html')


@app.route("/restaurant/<int:restaurant_id>/menu/edit")
def editMenuItem(restaurant_id):
    # return "Pagina para editar um menu do resturante %s" % restaurant_id
    return render_template('editmenuitem.html', item=item )


@app.route("/restaurant/<int:restaurant_id>/menu/delete")
def deleteMenuItem(restaurant_id):
    # return "Pagina para deletar o menu do resturante %s" % restaurant_id
    return render_template('deleteMenuItem.html')


if __name__ == '__main__':
    app.debug = True
app.run(host='0.0.0.0', port=5000)
