from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # Initially, don't show the success message
    return render_template('index.html', show_contact_success=False)

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Process form data here (e.g., save to database, send email)
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        print(f"Received contact from: {name} ({email}) - Message: {message}") # For debugging

        # After processing, render index.html again, but set the flag to show success message
        # This will cause a full page reload, but the content will be updated within the contact section.
        return render_template('index.html', show_contact_success=True)
    else:
        # If someone navigates directly to /contact via GET, just show the home page without success message
        return redirect(url_for('home')) # Redirect to home to ensure consistent display

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')