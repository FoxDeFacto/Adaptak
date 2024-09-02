from flask import Flask, render_template, request, redirect, url_for, flash
import os

# Define the base directory (absolute path to your project folder)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        field_of_study = request.form['field_of_study']
        is_freshman = request.form['is_freshman']
        birthdate = request.form['birthdate']
        roommate = request.form['roommate']
        gender = request.form['gender']
        turnus = request.form['turnus']
        transport = request.form['transport']
        street = request.form['street']
        street_number = request.form['street_number']
        city = request.form['city']
        zip = request.form['zip']
        country = request.form['country']

        # Combine the data into a single string separated by semicolons
        record = f"{first_name};{last_name};{email};{phone};{field_of_study};{is_freshman};{birthdate};{roommate};{gender};{turnus};{transport};{street};{street_number};{city};{zip};{country};\n"

        # Use the absolute path to the file
        file_dir = os.path.join(BASE_DIR, 'Records')
        file_path = os.path.join(file_dir, 'registrations.txt')
        
        # Ensure the directory exists
        os.makedirs(file_dir, exist_ok=True)
        
        # Write the record to a text file
        with open(file_path, 'a') as f:
            f.write(record)

        # Flash a success message
        flash('Přihláška byla úspěšně odeslána!', 'success')

        return redirect(url_for('index'))

@app.route('/galerie')
def galerie():
    return render_template('galerie.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

@app.route('/prihlaska')
def prihlaska():
    return render_template('prihlaska.html')

if __name__ == '__main__':
    app.run(debug=True)
