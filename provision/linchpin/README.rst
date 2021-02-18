Linchpin
========

This example demonstrates how you can define and use teflo_linchpin_plugin
 to provision resources


Pre-Run
-------

**ATTENTION**

This example below has teflo and teflo_linchpin_plugin are installed in a virtual environment named teflo.
Please replace this virtual environment with the virtual environment you
created for teflo if it differs.

There are four scenarios, where we provision beaker, aws, libvirt and openstack
resources using linchpin. Linchpin is made available to teflo using teh teflo_linchpin_plugin


Run
---

To provision the resources, please make sure you have set your
credentials properly within the `teflo.cfg <teflo.cfg>`_.

You also need to set the following environment variables depending on which scenario you
are running. This data will be templated into the scenario descriptor file.

.. code-block:: bash

    (teflo) $ export jobgroup=<BEAKER_JOB_GROUP>
    (teflo) $ export host_fqdn=<FQDN_OF_SPECIFIC_BEAKER_HOST>


You will also need to put you ssh keys in the keys folder and set the permissions to 0600
The name of this folder can be anything, it is a folder to store the ssh keys needed
for provisioning. The ssh keys may differe for different resources, e.g. the key for beaker
can be differnt than the one for openstack. Export these keys based on what scenarios you choose
to run or store the keys as differnent variables in the scenario files.

.. code-block:: bash

    (teflo) $ chmod 0600 ./keys
    (teflo) $ export key_name=<key for creating beaker instances under the keys folder>

Once you have set those environment variables and ssh keys you can execute the following
command to run teflo.

.. code-block:: none

    (teflo) $ teflo run -t provision -s <scenario_name>.yml -w .

You will see teflo provision the resource.
On completion, teflo will create an updated scenario descriptor file
(results.yml). This file will be an exact copy but contains additional
information from provisioning such as ip address, beaker job, etc.

To cleanup the resources, just execute the following teflo command below.

.. code-block:: none

    (teflo) $ teflo run -t cleanup -s .teflo/.results/results.yml

We pointed teflo to the updated descriptor file. This provides teflo with
the updated information from the provision task.
