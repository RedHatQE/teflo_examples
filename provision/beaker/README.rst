Beaker
======

This example demonstrates how you can define and use beaker machines within
teflo.

**ATTENTION**

This example below has teflo installed in a virtual environment named teflo.
Please replace this virtual environment with the virtual environment you
created for teflo if it differs.

Pre-Run
-------

First lets review the content of the `scenario descriptor file <scenario.yml>`_.
This file contains a provision section with one host resource defined. You will
see the machine requires a couple keys (*name*, *groups*, *provisioner*). It is
highly recommended to define *ansible_params* key. This tells teflo about how
ansible should connect to the machine.

Run
---

To provision the machine, please make sure you have set your beaker
credentials properly within the `teflo.cfg <teflo.cfg>`_.

You also need to set the following environment variables. This data will be
templated into the scenario descriptor file.

.. code-block:: bash

    (teflo) $ export jobgroup=<BEAKER_JOB_GROUP>
    (teflo) $ export host_fqdn=<FQDN_OF_SPECIFIC_BEAKER_HOST>


You will also need to put you ssh keys in the keys folder and set the permissions to 0600
The name of this folder can be anything, it is a folder to store the ssh keys needed
for provisioning

.. code-block:: bash

    (teflo) $ chmod 0600 ./keys
    (teflo) $ export key_name=<key for creating beaker instances under the keys folder>

Once you have set those environment variables and ssh keys you can execute the following
command to run teflo.

.. code-block:: none

    (teflo) $ teflo run -t provision -s scenario.yml -w .

You will see teflo provision the machine by submitting a beaker reservation job.
On completion, teflo will create an updated scenario descriptor file
(results.yml). This file will be an exact copy but contains additional
information from provisioning such as ip address, beaker job, etc.

To cleanup the machine, just execute the following teflo command below.

.. code-block:: none

    (teflo) $ teflo run -t cleanup -s .teflo/.results/results.yml

We pointed teflo to the updated descriptor file. This provides teflo with
the updated information from the provision task.
