from colorthief import ColorThief
from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static/"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/show-colors", methods=["GET", "POST"])
def show_colors():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
            image_path = f"static/{image.filename}"

            color_thief = ColorThief(image_path)
            palette = color_thief.get_palette(color_count=11)
            hex_palette = []
            for color in palette:
                hex = '#%02x%02x%02x' % color
                hex_palette.append(hex)
            return render_template("get_colors.html", image=image_path, palette=hex_palette)

if __name__ == "__main__":
    app.run(debug=True)