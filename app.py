from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Configure upload folder
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Define allowed image extensions
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

# Helper function to check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get uploaded files from the request object
    files = request.files.getlist('file[]')

    # Create a list to store the paths to the uploaded images
    image_paths = []

    # Loop through the uploaded files
    for file in files:
        # If the file has an allowed extension
        if allowed_file(file.filename):
            # Save the file to the upload folder
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Add the path to the image_paths list
            image_paths.append(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # Render the template that displays the uploaded images
    return render_template('uploaded.html', image_paths=image_paths)

if __name__ == '__main__':
    app.run(debug=True)
