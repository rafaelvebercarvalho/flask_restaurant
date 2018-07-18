from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/restaurant")
def showRestaurant():
    return "Pagina que vai mostrar todos os restaurantes"

@app.route("/restaurant/new")
def newRestaurant():
    return "Pagina para criar novos resturantes"

@app.route("/restaurant/<int:restaurant_id>/edit")
def editRestaurant(restaurant_id):
    return "Pagina para editar os resturantes %s" %restaurant_id

@app.route("/restaurant/<int:restaurant_id>/delete")
def deleteRestaurant(restaurant_id):
    return "Pagina para deletar os resturantes %s" %restaurant_id

@app.route("/restaurant/<int:restaurant_id)
@app.route("/restaurant/<int:restaurant_id/menu")
def showMenu(restaurant_id):
    return "Pagina que vai mostrar o menu do resturante %s" %restaurant_id

@app.route("/restaurant/<int:restaurant_id/menu/new")
def newMenuItem(restaurant_id):
    return "Pagina para criar um novo menu para um restaurantes %s" %restaurant_id

@app.route("/restaurant/<int:restaurant_id/menu/edit")
def editMenuItem(restaurant_id):
    return "Pagina para editar um menu do resturante %s" %restaurant_id

@app.route("/restaurant/<int:restaurant_id/menu/delete")
def deleteMenuItem(restaurant_id):
    return "Pagina para deletar o menu do resturante %s" %restaurant_id

if __name__ == '__main__':
    app.debug = True
app.run(host='0.0.0.0', port=5000)
