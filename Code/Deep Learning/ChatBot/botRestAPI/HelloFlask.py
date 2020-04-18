#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask

app = Flask(__name__)


# In[ ]:


@app.route('/')

def index():
    return "Hello, World!"


# In[ ]:


@app.route('/india')
def index1():
    return "Namaste"


# In[ ]:


@app.route('/france')
def index2():
    return "Bonjour"


# In[ ]:


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=21021)


# In[ ]:


exit


# In[ ]:




