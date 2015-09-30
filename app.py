from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/clans')
def clans():
    return render_template('clans.html')

@app.route('/members')
def members():
    return render_template('members.html')

@app.route('/clan/<int:id>')
def clan(id):
    return render_template('clan_page.html', clan_id=id)
    
if __name__ == '__main__':

    @app.route('/<path:path>')
    def static_file(path):
        return app.send_static_file(path)


    app.debug = True
    app.run()