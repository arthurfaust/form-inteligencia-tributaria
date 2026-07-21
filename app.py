from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def diagnostico():
    if request.method == 'POST':
        dados_cliente = request.form.to_dict()
        return {"status": "sucess", "dados_recebidos": dados_cliente}
    
    perguntas_estruturadas = [
       {
            'Código': 'P0002',
            'Tipo': 'Texto',
            'Pergunta / Campo': 'Nome do cliente',
            'subperguntas': []
        },
        {
            'Código': 'P0012',
            'Tipo': 'Sim/Não',
            'Pergunta / Campo': 'Possui participação societária em empresas?',
            'subperguntas': [
                {'Código': 'E0001', 'Tipo': 'Texto', 'Pergunta / Campo': 'Razão Social'},
                {'Código': 'E0002', 'Tipo': 'Texto', 'Pergunta / Campo': 'CNPJ / Identificador estrangeiro'}
            ]
        },
        {
            'Código': 'R0001',
            'Tipo': 'Sim/Não',
            'Pergunta / Campo': 'Recebe rendimentos do trabalho?',
            'subperguntas': [
                {'Código': 'RT001', 'Tipo': 'Texto', 'Pergunta / Campo': '↳ Fonte pagadora'},
                {'Código': 'RT002', 'Tipo': 'Lista', 'Pergunta / Campo': '↳ Tipo de rendimento'}
            ]
        }
    ]

    return render_template('diagnostico.html', perguntas=perguntas_estruturadas)

if __name__ == '__main__':
    app.run(debug=True)