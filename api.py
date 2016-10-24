from flask.ext.restless import ProcessingException

from app import api
from entries.forms import CommentForm
from models import Comment
from models import User
from models import Entry
from models import Tag

def post_preprocessor(data, **kwargs):
    form = CommentForm(data=data)
    if form.validate():
        return form.data
    else:
        raise ProcessingException(
                  description='Invalid form submission.',
                  code=400)


api.create_api(
    Comment,
    include_columns=['id', 'name', 'url', 'body',
                     'created_timestamp'],
    include_methods=['gravatar'],
    methods=['GET', 'POST'],
    preprocessors={
        'POST': [post_preprocessor],
    })

api.create_api(User,include_columns=['id','email', 'password_hash', 
                                     'name', 'active', 'admin', 'created_timestamp'],
                                      methods=['GET', 'POST', 'DELETE'])

api.create_api(Entry,include_columns=['id','title', 'slug', 
                                     'body', 'status', 'created_timestamp', 
                                     'modified_timestamp', 'author_id', 'tags', 'comments'],
                                      methods=['GET', 'POST', 'DELETE'])

api.create_api(Tag,include_columns=['id', 'name', 'slug'],
                                      methods=['GET', 'POST', 'DELETE'])

#curl -X POST -H "Content-Type: application/json" -d '{"name": "REST-tag"}' http://127.0.0.1:5000/api/tag
#curl -X POST -H "Content-Type: application/json" -d '{"email" : "userx@gmail.com", "password_hash" : "userx", "name" : "John Doe", "slug" : "john-doe" }' http://127.0.0.1:5000/api/user

#curl -X POST -H "Content-Type: application/json" -d '{title": "post using REST", "body": "This is the post content.", author_id : 2, "tags": 1}' http://127.0.0.1:5000/api/entry


