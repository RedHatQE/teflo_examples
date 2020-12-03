#!/bin/bash

source ../../lib/utils.sh

welcome_header

echo "Please make sure the teflo.cfg is updated with your openstack \
credentials."
echo ""

echo "Which teflo command would you like to run (provision|cleanup)?"
read task
echo ""

if [ $task == 'provision' ];
then
    echo "Please provide the following information about your openstack \
tenant:"
    echo "Internal network:"
    read network
    echo "Keypair:"
    read keypair

    export network=${network}
    export keypair=${keypair}

    teflo_provision
else
    teflo_cleanup
fi
