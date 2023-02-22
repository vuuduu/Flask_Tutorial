# We can do this because website is part of a python package due to __init__.py file.
from website import create_app

app = create_app()

# Only if we run this NOT IMPORT are we going to execute the line below.
# Only run the web server if you also run this file.
if __name__ == '__main__':
    # Debug = true mean anytime you made changes to the code (it'll automatically rerun the web server)
    app.run(debug=True)