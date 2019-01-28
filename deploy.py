import os

from flask_wtf.csrf import CSRFProtect

# Flask Imports
from flask import Flask, request
from flask import render_template
from flask_table import Table, Col
from flask import send_file
from flask import redirect

#Pytube Imports
import pytube

#Helpers
import stream_search as streamSearch

#Launch Flask App
app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

csrf = CSRFProtect(app)



@app.route('/', methods=['GET', 'POST'])
def root():
    form = streamSearch.SearchForm(request.form)

    if form.validate_on_submit():
        url = form.url.data
        unique_id_index = url[url.index('?v=')+3::]
        print unique_id_index
        return redirect('/get-hd-video'+'?url='+unique_id_index, code=302)
    else:
        print "Error validating form: ", form.errors
    return render_template('base.html', form=form)


# route example: downlink.com/get-hd-video?url=
@app.route('/get-hd-video', methods=['GET', 'POST'])
def get_video_streams():
    url = 'http://www.youtube.com/watch?v='+request.args.get('url')
    print url
    youtube = pytube.YouTube(url)
    print "Getting youtube streams"
    files = youtube.streams.filter(progressive=True).all()
    stream_table = streamSearch.StreamTable(files)
    print stream_table

    return render_template('stream_result', stream_table=stream_table)


@app.route('/download')
def download():
    return redirect("http://www.example.com", code=302)


# @app.route('/query-example')
# def query_example():
#     language = request.args.get('language') #if key doesn't exist, returns None
#     framework = request.args['framework'] #if key doesn't exist, returns a 400, bad request error
#     website = request.args.get('website')
#
#     return '''<h1>The language value is: {}</h1>
#               <h1>The framework value is: {}</h1>
#               <h1>The website value is: {}'''.format(language, framework, website)
#
# @app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
# def form_example():
#     if request.method == 'POST': #this block is only entered when the form is submitted
#         language = request.form.get('language')
#         framework = request.form['framework']
#
#         return '''<h1>The language value is: {}</h1>
#                   <h1>The framework value is: {}</h1>'''.format(language, framework)
#
#     return '''<form method="POST">
#                   Language: <input type="text" name="language"><br>
#                   Framework: <input type="text" name="framework"><br>
#                   <input type="submit" value="Submit"><br>
#               </form>'''
#
# @app.route('/json-example', methods=['POST']) #GET requests will be blocked
# def json_example():
#     req_data = request.get_json()
#
#     language = req_data['language']
#     framework = req_data['framework']
#     python_version = req_data['version_info']['python'] #two keys are needed because of the nested object
#     example = req_data['examples'][0] #an index is needed because of the array
#     boolean_test = req_data['boolean_test']
#
#     return '''
#            The language value is: {}
#            The framework value is: {}
#            The Python version is: {}
#            The item at index 0 in the example list is: {}
#            The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)
#
# if __name__ == '__main__':
#     app.run(debug=True, port=5000) #run app in debug mode on port 5000


if __name__ == '__main__':
    app.run(debug=True),  # Do not leave on on real situations