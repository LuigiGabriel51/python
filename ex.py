import jwt
import datetime as dt



Token = jwt.encode({'user': 'bagriel','exp': dt.datetime.now(tz=dt.timezone.utc)}, 'luigi123')
def decorated(token):
    if not token:
        return {
            "message": "token invalido ou inexistente"
        }
    try:
        data = jwt.decode(token, 'luigi123', algorithms=["HS256"])
        return True
    except: return False
    
print(decorated(Token))

# def jwt_required(token):
#     if not token:
#         return jsonify({
#             "message": "token invalido ou inexistente"
#         }), 401
#     try:
#         data = jwt.decode(token, 'luigi', algorithms=["HS256"])
#         return True
#     except: 
#         return  False

# @app.route('/login', methods= ['GET','POST'])
# def login():
        
#     if request.method == 'POST':
#         email = request.args.get('email')
#         senha = request.args.get('senha')
#         record = bd.verifica_login(email,senha)
#         if record != False:
            
#             Token = jwt.encode({'user': record,'exp': dt.datetime.now(tz=dt.timezone.utc)}, 'luigi')
#             print(Token)
#             return jsonify({"AcessToken": Token})

#         else:
#             return jsonify(
#                 {
#                     "AcessToken": "acesso negado"
#                 }
#             ), 401
#     return redirect(login)

# @app.route("/funcionarios", methods=['GET'])
# def VERfuncionarios():
#     token = request.args.get('token')
#     if jwt_required(token) == True:
#         TabelaFuncionarios = bd.ver_tabelaFuncionarios()
#         return TabelaFuncionarios
#     else: return {
#         "message": "token invalido"
#     }