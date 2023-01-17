from flask import Flask,request, session, jsonify, redirect, render_template
from EmailAutomatico import enviar_email
from functools import wraps
import jwt
import datetime as dt
from flask_login import LoginManager
from classeBD import BD


app = Flask(__name__)
bd = BD()
login_manager = LoginManager()
login_manager.init_app(app)
app.config["SECRET_KEY"] = "japones7757"


def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({
                "message": "token invalido ou inexistente"
            }), 401
        try:
            data = jwt.decode(token, 'bagriel51', algorithms=["HS256"])
        except: return jsonify({ "message": 'token invalido ou inexistente'}), 403
        return f(*args, **kwargs)
    return decorated

#--------------------------------------------------rota de login---------------------------------------------------
@app.route('/login', methods= ['GET','POST'])
def login():
        
    if request.method == 'POST':
        email = request.args.get('email')
        senha = request.args.get('senha')
        record = bd.verifica_login(email,senha)
        if record != False:
            
            Token = jwt.encode({'user': record,'exp': dt.datetime.now(tz=dt.timezone.utc)}, 'bagriel51')
            return jsonify({"AcessToken": Token}), 200

        else:
            return jsonify(
                {
                    "AcessToken": "acesso negado"
                }
            ), 401
    return redirect(login)
#----------------------------------------------rota de serviços-----------------------------------------------

@app.route('/AddServicos', methods=['GET', 'POST'])
@jwt_required
def AddServicos():
    nome = request.args.get('nome')
    descricao  = request.args.get('descricao') 
    inicio = request.args.get('inicio') 
    final = request.args.get('final') 
    conclusao = request.args.get('conclusao') 
    
    record = bd.cria_projetos(nome, descricao, inicio, final, conclusao)
    return record

#----------------------------------------------rota de funcionarios-------------------------------------------

@app.route("/funcionarios", methods=['GET'])
@jwt_required
def VERfuncionarios():
    
    TabelaFuncionarios = bd.ver_tabelaFuncionarios()
    print(TabelaFuncionarios)
    return TabelaFuncionarios[0]
    
        

#-----------------------------------------------rota de registro-----------------------------------------------

@app.route('/registro', methods = ['POST'])
@jwt_required
def registro():
    nome = request.args.get('nome')
    email = request.args.get('email')
    cpf = request.args.get('cpf')
    senha = request.args.get('senha')
    password = hash.criaHash(senha)
    record = bd.cria_user(nome,email, cpf,password)

    return record

#---------------------------------------------rota de recuperaçao de senha--------------------------------------

@app.route('/busca_email', methods = ['GET','POST'])
@jwt_required
def busca_email():
    return render_template('template1.html')


@app.route('/verifica_senha', methods = ['POST'])
def verifica_senha():
    msg1 = ''
    msg2 = 'senha invalida, no minimo 8 caracteres!'

    
    

    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('password')
        vericacao = bd.recuperar_senha(email)
        if vericacao != False:
            if senha == None or len(senha)<8:
                return render_template('template1.html', msg2 = msg2)
            else:
                bd.redefinir_senha(email, senha)
                return 'senha alterada com sucesso', 200      
        else:
            msg1 = 'email invalido'
    return render_template('template1.html', msg = msg1)


@app.route('/pega_email', methods = ['POST'])
def pega_email():
    email = request.args.get('email')
    status = enviar_email(email)
    return status, 200
#---------------------------------------------rota de mostrar serviços-------------------------------------------
@app.route("/verServicos", methods=['GET'])
# @jwt_required()
def verServicos():
    record = bd.ver_tabelaProjetos()
    return f'{record}'
        



app.run(debug=True)