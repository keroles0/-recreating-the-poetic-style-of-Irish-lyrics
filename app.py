from flask import Flask, render_template, request
import tensorflow as tf  # Import TensorFlow for Keras models

app = Flask(__name__)

# Load the model using TensorFlow


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.form['user_input']
    model = tf.keras.models.load_model('myModel.h5')
    # Process input as needed for the model (e.g., convert to array, reshape)
    input_data = [float(user_input)]  # Example: Convert user input to a list of floats
    prediction = model.predict([input_data])
    output = f"Prediction: {prediction[0][0]}"  # Format based on model output shape

    return render_template('index.html', user_input=user_input, output=output)

if __name__ == '__main__':
    app.run(debug=True)
