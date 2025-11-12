from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.get("/")
    def hello():
        return "456"

    @app.get("/abcd")
    def hello123():
        return "12345678

    @app.get("/chungcock")
    def hello12333():
        return "i'm noob"
    
    @app.get("/healthz")
    def healthz():
        return jsonify(status="ok")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
