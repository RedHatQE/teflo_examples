Data Pass-through
=================

This example demonstrates how you can perform configuration against test
machines by ansible using teflo with passing data between orchestrate actions.

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
of machines. The orchestrate section contains two actions to be processed.
Each action is an ansible playbook to be run. Each action has a *hosts* key
which defines which host resource to be run against (defined in the provision
section).

Run
---

To configure the machines under test, just run the following teflo command.

.. code-block:: none

    (teflo) $ teflo run -t provision -t orchestrate -s scenario.yml -sl data_pass

You will see teflo skip over provisioning the machine due to its a static
machine. Orchestrate task will start and execute both the actions defined
against the hosts it was declared against. This example will first installing
product a and then go on to install product b. Product b installation requires
data from product a. The product a playbook will set facts that are persistent
and can be accessed by the product b install playbook. This will just run the
first two orchestrate task without label data_pass

To run third tasks with lable 'data_pass'

.. code-block:: none

    (teflo) $ teflo run -t orchestrate -s .teflo/.results/results.yml -w . -l data_pass

This will run task orc_task3, where you run a script by passing data about the provisioned host
as parameters. WE have declared user_name as a metadata of the provisioned host , which we will use
as input to the python script along with the provisioned hosts's ip address

To cleanup the machine, just execute the following teflo command below.

.. code-block:: none

    (teflo) $ teflo run -t cleanup -s .teflo/.results/results.yml -w .

We pointed teflo to the updated descriptor file. This provides teflo with
the updated information from the provision/orchestrate task. Please note
nothing will be deleted due to the host resource was static.



