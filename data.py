import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory


app= Flask(__name__)
app.secret_key= 'mysecretkey'

@app.route('/')
def index():

    return render_template('index.html')

"""@app.route('/carta') # '/'quiere decir pagina  principal
def carta():
    
    df= pd.read_excel("Libro.xlsx")
    df1=df[['Unnamed: 1', 'Producto', 'Precio Actualizado']]
    df1.columns= ['tipo','producto', 'precio']

    return render_template("carta.html",df1 = df1)"""

@app.route('/pizza') # '/'quiere decir pagina  principal
def pizza():
    


    return render_template("pizza.html")#,df1 = pizzas)

@app.route('/empanada') # '/'quiere decir pagina  principal
def empanada():
    

    
    return render_template("empanada.html")

@app.route('/milanesa') # '/'quiere decir pagina  principal
def milanesa():
    
    
    
    return render_template("Milanesa.html")

@app.route('/sandwich') # '/'quiere decir pagina  principal
def sandwich():
    
    
    
    return render_template("sandwich.html")

@app.route("/fritas") # '/'quiere decir pagina  principal
def fritas():


    return render_template("fritas.html")

@app.route('/bebidas') # '/'quiere decir pagina  principal
def bebidas():


    return render_template("bebidas.html")

"""@app.route('/lookup', methods=['POST'])
def lookup():
    cadena=request.form["lookup"]
    cadena=cadena.lower()
    df= pd.read_excel("Libro.xlsx")
    df1=df[['Unnamed: 1', 'Producto', 'Precio Actualizado']]
    df1.columns= ['tipo','producto', 'precio']
    df1['producto']=df1['producto'].str.lower()
    lookups= df1[df1["producto"].str.contains(r""+cadena+"" ,regex=True)]
          
    if len(lookups)==0:
        flash("No se ha encontrado coincidencia")
        return render_template("lookup.html", df1 = lookups)
        
    else:
        return render_template("lookup.html", df1 = lookups)"""
    
if __name__ == '__main__':
    app.run(debug=True)
    #index()
    #pizza()
