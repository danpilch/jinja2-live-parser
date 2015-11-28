# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from jinja2 import Template, Environment, meta
from inspect import getmembers, isfunction
from random import choice
import argparse
import json
import yaml
import imp
import filters
import os

app = Flask(__name__)

# Import custom filters from filters.py
imported_filters = { name: function for name, function in getmembers(filters) if isfunction(function) }
app.jinja_env.filters.update(imported_filters)


@app.route("/")
def render():
    return render_template('index.html', all_filters = app.jinja_env.filters)


@app.route('/convert', methods=['GET', 'POST'])
def convert():
    dummy_values = [ 'Lorem', 'Ipsum', 'Amet', 'Elit', 'Expositum', 
        'Dissimile', 'Superiori', 'Laboro', 'Torquate', 'sunt', 
    ]

    tpl = app.jinja_env.from_string(request.form['template'])
    values = {}

    if bool(int(request.form['dummyvalues'])):
        # List variables (introspection)
        env = Environment()
        vars_to_fill = meta.find_undeclared_variables(env.parse(request.form['template']))

        for v in vars_to_fill:
            values[v] = choice(dummy_values)
    else:
        if request.form['optiontype'] == 'yaml':
            values = json.loads(json.dumps(yaml.load(request.form['values'])))
        else:
            values = json.loads(request.form['values'])

    rendered_tpl = tpl.render(values)

    if bool(int(request.form['showwhitespaces'])):
        # Replace whitespaces with a visible character (will be grayed with javascript)
        rendered_tpl = rendered_tpl.replace(' ', u'•')

    return rendered_tpl.replace('\n', '<br />')

def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-b", "--bind", help="Define IP to bind to.", default="127.0.0.1")
    parser.add_argument("-p", "--port", type=int, help="Define Port to bind to.", default=5000)
    parser.add_argument("-d", "--debug", help="Enable Debug.", action="store_true")
    args = parser.parse_args()

    if args.debug:
        app.debug = True

    app.run(host=args.bind, port=args.port)

if __name__ == "__main__":
    main()
