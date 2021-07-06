Static
======

This example demonstrates how you can define and use static machines within
teflo.

**ATTENTION**

This example below has teflo installed in a virtual environment named teflo.
Please replace this virtual environment with the virtual environment you
created for teflo if it differs.

Pre-Run
-------

First lets review the content of the `scenario descriptor file <scenario.yml>`_.
This file contains a provision section with one host resource defined. Static
machines only require a couple keys (*name*, *groups*, *ip_address*). It is highly
recommended to define *ansible_params* key. This tells teflo about how
ansible should connect to the machine.

Run
---

You will need to put you ssh keys in the keys folder and set the permissions to 0600
The name of this folder can be anything, it is a folder to store the ssh keys needed
for provisioning

.. code-block:: bash

    (teflo) $ chmod 0600 ./keys
    (teflo) $ export key_name=<key for creating beaker instances under the keys folder>

To provision the machine, just execute the following teflo command below.

.. code-block:: none

    (teflo) $ teflo run -t provision -s scenario.yml

You will see that teflo skips provisioning due to the machine is static.

Since the machine is static, cleanup task is not necessary. If you wish to run
cleanup, teflo will not delete the machine. You can call cleanup as follows:

.. code-block:: none

    (teflo) $ teflo run -t cleanup -s .teflo/.results/results.yml -w .

As you can see we gave a different scenario file. At the end of each teflo
run a new results file gets generated. This file is an exact copy of the
initial scenario file just with additional information appeneded.
