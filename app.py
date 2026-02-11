from flask import Flask, request, jsonify
from brain import GeminiBrain

app = Flask(__name__)
bot = GeminiBrain()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_id = data.get('user_id', 'guest')
    message = data.get('message', '')

    if not message:
        return jsonify({"error": "No message provided"}), 400

    # Call Gemini
    reply = bot.ask_gemini(user_id, message)
    
    return jsonify({"reply": reply})

if __name__ == '__main__':
    print("Malaz running on Port 5000...")
    app.run(host='0.0.0.0', port=5000)