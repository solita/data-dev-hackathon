#!/bin/bash

ansible-playbook \
    --private-key ../../data-dev.pem \
    -i ../../inventory \
    -e @../../users.yml \
    install.yml
