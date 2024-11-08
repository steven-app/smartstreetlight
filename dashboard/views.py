from flask import Blueprint, render_template

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
def display_dashboard():
    # Load the embedded Power BI Dashboard
    return render_template('dashboard.html')
