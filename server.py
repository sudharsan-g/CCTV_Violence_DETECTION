from flask import Flask, request, render_template
import base64
from obj import get_r

app = Flask(__name__, template_folder='templates')

@app.route('/')
def fn():
    print("YES")
    return render_template('index.html')

@app.route('/v', methods=['POST'])
def getv():
    data = request.json['data']
    video_binary = base64.b64decode(request.json['data'])
    # Write the binary data to a temporary file
    with open("temp.mp4", "wb") as f:
        f.write(video_binary)
    return get_r("temp.mp4")


if __name__ == '__main__':
    app.run(debug=True)

    
