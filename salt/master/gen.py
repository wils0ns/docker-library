from jinja2 import Template
# TODO implement generator for creating source code for different salt versions
# 1. Organize templates by OS
# 2. Convert Dockerfile to jinja template to dynamically set salt version
# 3. Copy files from common folder into the same directory as the Dockerfile
# 4. gen example: gen.py centos 2018.3