from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
    "https://www.google.com/search?q=shop+clothes&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi-6peHhdXhAhWlsKQKHfhCADAQ_AUIDigB&biw=1920&bih=898#imgrc=HC4sYaX9B4eTNM:",
    "https://www.google.com/search?q=shop+clothes&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi-6peHhdXhAhWlsKQKHfhCADAQ_AUIDigB&biw=1920&bih=898#imgrc=AxDuUcMS0F7_DM:",
    
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
