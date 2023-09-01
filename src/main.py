from flask import Flask, jsonify, request
from flask_cors import CORS
from service.executar_consulta_nfc import executar_consulta_nfc
import time

from service.formatar_data import formatar_data

app = Flask(__name__)
CORS(app)

@app.route('/consultar-nfc', methods=['POST'])
def consultar_nfc():
    try:
        data = request.get_json()
        parametro = data.get('parametro')
        data_param = data.get('data') 

        data_formatada = formatar_data(data_param)

        tentativas = 3  

        for i in range(tentativas):
            try:

                resultado = executar_consulta_nfc(parametro, data_formatada)

                return jsonify({'status': 'success', 'message': resultado})
            
            except Exception as e:
                print(f"Erro ao executar consulta NFC")
                print("Tentando novamente...")
                print(e)
                time.sleep(5)  # Aguarde um tempo antes de tentar novamente
                i+=1
                return jsonify({'status': 'error', 'message': 'Erro após várias tentativas'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Erro no parametro de consulta'})

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
