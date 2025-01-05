from flask import Flask, request, jsonify
from textmancer import Textmancer

app = Flask(__name__)

# Initialize the text generation model
textmancer = Textmancer(model_name='gpt2-medium')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    max_length = data.get('max_length', 150)
    temperature = data.get('temperature', 1.0)
    num_return_sequences = data.get('num_return_sequences', 1)

    generated_texts = textmancer.generate_text(
        prompt=prompt,
        max_length=max_length,
        temperature=temperature,
        num_return_sequences=num_return_sequences
    )

    return jsonify({'generated_texts': generated_texts})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
