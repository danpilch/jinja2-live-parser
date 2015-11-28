# Jinja2 live parser

Forked from [abourguignon](https://github.com/abourguignon/jinja2-live-parser)

A lightweight live parser for [Jinja2](http://jinja.pocoo.org/docs/dev/) based on [Flask](http://flask.pocoo.org/) and [Jquery](http://jquery.com/).  
All you need is Python and preferably [pip](https://pypi.python.org/pypi/pip).  


## Install

    $ git clone git@github.com:abourguignon/jinja2-live-parser.git
    $ pip install -r requirements.txt
    $ python parser.py

## Or through Dockerfile

#### Build
    
    docker build -t mydocker/j2parser .
    docker run -d -p 49153:5000 mydocker/j2parser

Or simply `pull` it from registry (without building)

    docker run -d -p 49153:5000 sahilsk/j2parser

## Usage 

You are all set, go to `http://localhost:5000/` and have fun.  


## Preview

![preview](http://i.imgur.com/9tSiilb.png)

