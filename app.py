from flask import Flask, request, jsonify

app = Flask(__name__)

def is_strong_password(password):
    # Implement your password strength logic here
    # For simplicity, let's assume a strong password should have a minimum length of 8 characters
    return len(password) >= 8

@app.route('/check-password', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password')

    if not password:
        return jsonify({'error': 'Password is required'}), 400

    is_strong = is_strong_password(password)

    return jsonify({'is_strong': is_strong})

if __name__ == '__main__':
    app.run(debug=True)