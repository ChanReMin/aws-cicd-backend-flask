from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.get("/")
    def hello():
        return "456"

    @app.get("/abcd")
    def hello123():
        return "12345"

    @app.get("/abcdee")
    def hello12333():
        return "1234521"
    
    @app.get("/healthz")
    def healthz():
        return jsonify(status="ok")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
