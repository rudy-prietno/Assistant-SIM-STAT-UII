#!/bin/bash

s1="${env_var_name}"
s1="${env_var_name}.py"
s2="main.py"

if [[ "$s1" == "$s2" ]]; then
    gunicorn --bind 0.0.0.0:3000 main:app --reload
else
    gunicorn --bind 0.0.0.0:3000 main1:app --reload
fi