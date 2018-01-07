from flask_script import Manager
from wangyinews import create_app
app = create_app()
manage = Manager(app)


if __name__ == '__main__':
    app.run(debug = True)
