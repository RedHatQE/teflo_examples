#!/bin/bash

source ../../lib/utils.sh

welcome_header

echo "Please make sure the teflo.cfg is updated with your beaker \
credentials."
echo ""

echo "Which teflo command would you like to run (provision|cleanup)?"
read task
echo ""

if [ $task == 'provision' ];
then
    echo "Please provide the following information about your beaker \
group:"
    echo "Job group:"
    read jobgroup
    echo "Username:"
    read username
    echo "Password:"
    read password
    echo "Host FQDN:"
    read host_fqdn
	
    export jobgroup=${jobgroup}
    export username=${username}
    export password=${password}
    export host_fqdn=${host_fqdn}
    teflo_provision
else
    teflo_cleanup
fi
