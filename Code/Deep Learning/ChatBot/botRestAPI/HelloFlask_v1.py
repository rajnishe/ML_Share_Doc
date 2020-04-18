#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask
from flask import request

app = Flask(__name__)


# In[ ]:


@app.route('/')

def index():
    return "Hello, World!"


# In[ ]:


# Create a URL
#  which send th JSON format data
#  and function read this JSON format
#  and print on console 
#  print key & value 
#

@app.route('/india/<c_id>',methods=['GET'])
def index1(c_id):
    print(c_id)
    return "Namaste" + str(c_id)


# In[ ]:
@app.route('/ind/',methods=['GET'])
def multiArg():
    c_id = request.args.get('c_id') 
    print(c_id)
    return "Namaste" + str(c_id)



@app.route('/france')
def index2():
    return "Bonjour"


# In[ ]:


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=21022)


