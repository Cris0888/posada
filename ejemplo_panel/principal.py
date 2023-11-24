from flask import Flask,render_template,request
from flaskext.mysql import MySQL


aplicacion= Flask(__name__)
mysql=MySQL()
aplicacion.config['MYSQL_DATABASE_HOST'] = 'localhost'
aplicacion.config['MYSQL_DATABASE_PORT'] = 3306
aplicacion.config['MYSQL_DATABASE_USER'] = 'root'
aplicacion.config['MYSQL_DATABASE_PASSWORD'] = ''
aplicacion.config['MYSQL_DATABASE_DB'] = 'probando'
mysql.init_app(aplicacion)

@aplicacion.route("/")
def index():
    return render_template("/panel.html")

@aplicacion.route("/buscadorReserva", methods=["POST"])
def buscadorReserva():
    busqueda=request.form["busca_reserva"]

    respuesta1=busqueda.isnumeric()

    if respuesta1 == True:
        sql1=f"SELECT cedula FROM reservas WHERE cedula LIKE '%{busqueda}%'"
        con=mysql.connect()
        cur=con.cursor()
        cur.execute(sql1)
        resultado1=cur.fetchone()
        con.commit()
        return render_template ("panel.html", respuesta1 = resultado1)
    
    elif respuesta1 == False:
        sql2=f"SELECT reserva FROM reservas WHERE reserva LIKE '%{busqueda}%'"
        con=mysql.connect()
        cur=con.cursor()
        cur.execute(sql2)
        resultado2=cur.fetchone()
        con.commit()
        return render_template ("panel.html", respuesta2 = resultado2)
    

@aplicacion.route("/buscadorProducto", methods=['POST'])
def buscadorProducto():
    busqueda2=request.form['num_producto']

    respuesta2=busqueda2.isnumeric()

    if respuesta2 == True:
        sql1=f"SELECT codigo FROM precios WHERE codigo LIKE '%{busqueda2}%'"
        con=mysql.connect()
        cur=con.cursor()
        cur.execute(sql1)
        resultado3=cur.fetchone()
        con.commit()
        return render_template ("panel.html", respuesta3 = resultado3)
    
    elif respuesta2 == False:
        sql2=f"SELECT palabra FROM precios WHERE palabra LIKE '%{busqueda2}%'"
        con=mysql.connect()
        cur=con.cursor()
        cur.execute(sql2)
        resultado4=cur.fetchone()
        con.commit()
        return render_template ("panel.html", respuesta4 = resultado4)




    


if __name__ == '__main__':
    aplicacion.run(debug=True)
