from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']

    try:
        result = util.classify_image(image_data)
        print("Result:", result)
        response = jsonify(result)
    except Exception as e:
        print("Error:", e)
        response = jsonify({"error": str(e)})

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000,debug=True)