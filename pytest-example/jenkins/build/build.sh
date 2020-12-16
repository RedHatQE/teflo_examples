#!/usr/bin/env bash

function header {
    echo "**** ATTENTION ****"
    echo "Jenkins authentication (auth.ini) needs to be set!"
    echo ""
}

header
ansible-playbook site.yml -v
