from flask import Flask,request,render_template_string
from lista_enlazada import Lista
app = Flask(__name__)

lista = Lista()
@app.route('/',methods = ['GET','POST'])
def root():
    global lista
    var = ''
    if request.method == 'POST':
        if 'agregar' in request.form:
            num = request.form["valor"]
            print(num)
            lista.append(num)
            print(lista.print())
        elif 'agregar_inicio' in request.form:
            num = request.form["valor"]
            print(num)
            lista.prepend(num)
            print(lista.print())
        elif 'eliminar' in request.form:
            var = lista.pop()
    cadena = '''
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
            <form method = 'post'>
                <input name = "valor">
                <button name = "agregar" type="submit">Agregar Final</button>
            </form>
            <form method = 'post'>
                <input name = "valor">
                <button name = "agregar_inicio" type="submit">Agregar Inicio</button>
            </form>
            <form method = 'post'>
                <button name = "eliminar" type="submit">Eliminar</button>
            </form>
            <h3>Elementos de la lista: {{lista}}</h3>
            <h3>Elementos eliminado: {{eliminado}}</h3>
            '''
    return render_template_string(cadena,lista = lista.print(),eliminado = var)

if __name__ == '__main__':
    app.run(debug=True)
