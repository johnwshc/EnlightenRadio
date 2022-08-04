from app import app
import json

from flask import render_template, redirect, url_for, flash, request
from analz.playlist.erforms import ShuffleThemesForm
from analz.playlist.ertest import stage
from config import Config
from datetime import datetime


# ###############  index ER HOME   #################
@app.route('/')
@app.route('/index')
def index():
    return render_template('er.html')

# # ##############  Whats Playing  ##############
@app.route('/whats_playing', methods=['GET', 'POST'])
def whats_playing():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            d = json.loads(request.get_data())
            txt = d['wp']
            print(f"wp txt: {txt}")
            with open(Config.ER_WP_P, "w" ) as f:
                f.write(txt)
            return "success"
        else:
            return "invalid content-type"

    with open(Config.ER_WP_P) as f:
        txt = f.read()
    ds = datetime.now().date().strftime('%A')[0:3].lower()
    menu_props = stage.pattern_to_html(ds)
    return render_template('wp.html', wp_txt=txt, menu=menu_props)

# ##### Reporter Gateway  ###################

@app.route('/reporter')
def reporter():
    return render_template('reporter.html', title='reporter')

@app.route('/manage')
def er_mgmt():  # put application's code here
   return render_template('er_manager.html', title='manager')

@app.route('/shuffle', methods=['GET', 'POST'])
def shuffle_themes():
    form = ShuffleThemesForm()
    if form.validate_on_submit():
        print(form.example.data)
        days = [x[:3].lower() for x in form.example.data]
        for day in days:
            st = stage(day)
        return render_template("success.html", data=form.example.data)
    else:
        if request.method == 'GET':
            return render_template('example.html', form=form)

        elif form.errors:

            flash("Validation Failed")
            print(form.errors)
            return redirect(url_for('shuffle_themes'))

        else:
            return "<html><body><h1>ERROR</h1></body><html>"


#
# if __name__ == '__main__':
#     app.run()


