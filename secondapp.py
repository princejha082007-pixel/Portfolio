from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # Render the new template file (sec_index.html) instead of index.html
    return render_template('sec_index.html', show_contact_success=False)

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Process form data (unchanged)
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        print(f"Received contact from: {name} ({email}) - Message: {message}")

        # Render the new template file with success message
        return render_template('sec_index.html', show_contact_success=True)
    else:
        # Redirect to home (unchanged)
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')