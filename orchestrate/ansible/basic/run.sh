#!/bin/bash

source ../../../lib/utils.sh

welcome_header

echo ""

echo "Which teflo command would you like to run (orchestrate|cleanup)?"
read task
echo ""

if [ $task == 'orchestrate' ];
then
    teflo_orchestrate
else
    teflo_cleanup
fi
