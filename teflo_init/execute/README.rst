Execute_Example
===============

This example demonstrates how you can execute tests against test machines
using teflo.

**ATTENTION**

This example below has teflo installed in a virtual environment named teflo.
Please replace this virtual environment with the virtual environment you
created for teflo if it differs.

Pre-Run
-------

First lets review the content of the `scenario descriptor file <scenario.yml>`_.
This file contains a provision section which contains one host resource
defined. For the case of keeping this example simple, the host resource is
the localhost where teflo will be run. This way we can avoid any provisioning
of machines. The execute section contains two execute task to be run. First tasks
runs a shell command and collects some logs. The second task runs a script to
add two numbers

This example makes use of labels feature provided by teflo.
You can run or skip a task by providing its label

Run
---

To execute tests against the machines under test, just run the following
teflo command.

.. code-block:: none

    (teflo) $ teflo run -t provision -t execute -s scenario.yml

You will see teflo skip over provisioning the machine due to its a static
machine. Then execute task will start to run the defined test.

To execute just the first task


.. code-block:: none

    (teflo) $ teflo run -t execute -s scenario.yml -l exe1


To skip the first execute tasks and run only the second one


.. code-block:: none

    (teflo) $ teflo run -t execute -s scenario.yml -sl exe1

**NOTE**
For more examples check out the `examples repo <https://github.com/RedHatQE/teflo_examples>`_.
