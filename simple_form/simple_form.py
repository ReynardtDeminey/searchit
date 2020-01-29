from flask import Flask, render_template, flash, request, url_for
from form import SearchForm
from datetime import datetime, timezone
import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/', methods=['GET', 'POST'])
def hello():
    form = SearchForm()

    username = ''
    subreddit = ''
    num_of_records = ''
    choice = ''
    query = ''
    data = ''


    if request.method == 'POST':
        username = request.form['username']
        subreddit = request.form['subreddit']
        num_of_records = request.form['num_of_records']
        choice = request.form['choice']
        query = request.form['query']
        
        print(username)
        print(subreddit)
        print(num_of_records)
        print(choice)
        print(query)
        print(type(num_of_records))

        if choice == 'post':
            url = f'https://api.pushshift.io/reddit/search/submission/?q={query}&author={username}&subreddit={subreddit}&size={num_of_records}'
        else:
            url = f'https://api.pushshift.io/reddit/search/comment/?q={query}&author={username}&subreddit={subreddit}&size={num_of_records}'
        
        print(url)

        response = requests.get(url)
        response = response.text
        data = json.loads(response)
        data = data['data']

       
    # if choice == 'post':    
    #     url = f'https://api.pushshift.io/reddit/search/submission/?q={query}&author={username}&subreddit={subreddit}&size={num_of_records}'
    #     response = requests.get(url)
    #     response = response.text
    #     data = json.loads(response)
    #     data = data['data']
    # else:
    #     url = f'https://api.pushshift.io/reddit/search/comment/?q={query}&author={username}&subreddit={subreddit}&size={num_of_records}'
    #     response = requests.get(url)
    #     response = response.text
    #     data = json.loads(response)
    #     data = data['data']
    
    return render_template('index.html', form=form, username=username, subreddit=subreddit, num_of_records=num_of_records, choice=choice, query=query, data=data)




if __name__ == '__main__':
    app.run(debug=True)
