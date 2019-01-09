from flask import Flask,request,redirect,url_for
from forumdb import get_posts, add_post

app=Flask(__name__)

#Html portion of the page
HTML_WRAP='''\
<!DOCTYPE html>
<html>
  <head>
    <title>DB Forum</title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
    </style>
  </head>
  <body>
    <h1>DB Forum</h1>
    <form method=post>
      <div><textarea id="content" name="content"></textarea></div>
      <div><button id="go" type="submit">Post message</button></div>
    </form>
    <!-- post content will go here -->
%s
  </body>
</html>
'''
#Html template for an individual post
POST='''\
    <div class=post><em class=date>%s</em><br>%s
    </div>
'''
#main page of the app
@app.route('/',methods=['GET'])
def main():
    posts="\n".join(POST%(date,text) for date,text in get_posts())
    html=HTML_WRAP % posts
    return html

#New Post submission
@app.route('/',methods=['POST'])
def post():
    message=request.form['content']
    add_post(message)
    return redirect(url_for('main'))

#for running at port 8000
if __name__=="__main__":
  app.run(host='0.0.0.0', port=8000)
