from app import app
from utils import get_prediction
from flask import Flask, jsonify, request, abort

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        mi_encabezado = request.headers.get('MiEncabezado')
        if (mi_encabezado != "PongaAquiSuHeader"):
            # Hacer algo aqui
            print("Header equivocado")
            print(mi_encabezado)
            abort(401)
        else:
            print("Header correcto")
        file = request.files['file']
        img_bytes = file.read()
        class_id, class_name = get_prediction(image_bytes=img_bytes)
        #return jsonify({'class_id': class_id, 'class_name': class_name, 'mi_encabezado': mi_encabezado}) 
        return jsonify({'class_id': class_id, 'class_name': class_name})


if __name__ == "__main__":
    app.run(port=5001)
