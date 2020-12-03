#!/bin/bash

source ../../lib/utils.sh

welcome_header

echo "Which teflo command would you like to run (provision|cleanup)?"
read task
echo ""

if [ $task == 'provision' ];
then
    teflo_provision
else
    teflo_cleanup
fi
