import os
from flask import Response, Flask

app = Flask(__name__)




@app.route("/image/<imageid>")
def get_image(imageid):
    print("================" + imageid)
    imgPath = os.path.abspath(os.path.dirname(__file__)) + "/static/" + imageid + ".jpg"
    with open(imgPath, 'rb') as f:
        image = f.read()
    resp = Response(image, mimetype="image/jpeg")
    return resp

if __name__ == "__main__":
    app.run()
