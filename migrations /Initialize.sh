flask db init               # Initialize migration directory
flask db migrate -m "Init"  # Generate migration files
flask db upgrade            # Apply migrations
