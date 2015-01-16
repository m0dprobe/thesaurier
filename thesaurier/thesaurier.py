from flask import Flask, request, render_template, url_for, redirect, flash
import json, urllib.request


app = Flask(__name__)

app.config.update(
    DEBUG = True,
    SECRET_KEY = 'foobar'
)

if __name__ == '__main__':
    app.run()


class NoResultsError(Exception):
    def __init__(self, word):
        self.word = word

    def __str__(self):
        return repr(self.word)


def thesaurus_for_word(word):
    response = urllib.request.urlopen('https://www.openthesaurus.de/synonyme/search?q={0}&format=application/json'.format(word)).read().decode('UTF-8')
    json_response = json.loads(response)
    if json_response['synsets']:
        return json_response['synsets'][0]['terms'][0]['term']
    else:
        raise NoResultsError(word)


@app.route('/', methods=['GET', 'POST'])
def convertText():
    if request.method == 'POST':
        textToConvert = request.form['text']
        words = textToConvert.split(' ')
        result = ""
        no_results = []
        for word in words:
            try:
                result += thesaurus_for_word(word)
            except NoResultsError as nr:
                # TODO: implement better handling when there are no results
                result += word
                no_results.append(word)
        return render_template('result.html', result=result, errors=no_results)

    return render_template('input.html')
