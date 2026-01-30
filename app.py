from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a random secret key

# Create necessary directories if they don't exist
static_dirs = ['static/css', 'static/js', 'static/img', 'static/lib', 'static/mail']
for dir_path in static_dirs:
    os.makedirs(dir_path, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/single')
def single():
    return render_template('single.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Here you would typically:
        # 1. Save to database
        # 2. Send email notification
        # 3. Process the contact form
        
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

# Newsletter subscription route
@app.route('/subscribe', methods=['POST'])
def subscribe():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        
        # Process newsletter subscription
        # Save to database or mailing list
        
        flash('Thank you for subscribing to our newsletter!', 'success')
        return redirect(url_for('index'))

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Admin routes (optional)
@app.route('/admin')
def admin():
    # Add authentication logic here
    return render_template('admin/dashboard.html')

@app.route('/admin/messages')
def admin_messages():
    # Add authentication and message retrieval logic here
    return render_template('admin/messages.html')

if __name__ == '__main__':
    app.run()