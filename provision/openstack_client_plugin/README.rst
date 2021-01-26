OpenStack
=========

This example demonstrates how you can define and use openstack machines within
teflo.

**ATTENTION**

This example below has teflo and teflo_openstack_client-plugin
installed in a virtual environment named teflo.
Please replace this virtual environment with the virtual environment you
created for teflo if it differs.

First lets review the content of the `scenario descriptor file <scenario.yml>`_.
This file contains a provision section with one host resource defined.
For more examples on how to use teflo_openstack_client_plugin
please visit `here <https://github.com/RedHatQE/teflo_openstack_client_plugin/blob/master/docs/user.md#examples>`_

Run
---

To provision the machine, please make sure you have set your openstack
credentials properly within the `teflo.cfg <teflo.cfg>`_.

There are other atributes for openstack_client , that can be configured in
teflo.cfg. Please visit
`here <https://github.com/RedHatQE/teflo_openstack_client_plugin/blob/master/docs/user.md#provisioner-configuration>`__ to get more information
You also need to set the following environment variables. This data will be
templated into the scenario descriptor file.

.. code-block:: bash

    (teflo) $ export network=<OPENSTACK_INTENRAL_NETWORK_NAME>
    (teflo) $ export keypair=<OPENSTACK_KEYPAIR>

You will also need to put you ssh keys in the keys folder and set the permissions to 0600
The name of this folder can be anything, it is a folder to store the ssh keys needed
for provisioning

.. code-block:: bash

    (teflo) $ chmod 0600 ./keys
    (teflo) $ export key_name=<key for creating beaker instances under the keys folder>


Once you have set those environment variables  and ssh keys you can execute the following
command to run teflo.

.. code-block:: none

    (teflo) $ teflo run -t provision -s scenario.yml

You will see teflo provisions two openstack resources with names test_client_a_0 and test_client_a_1
On completion, teflo will create an updated scenario descriptor file
(results.yml). This file will be an exact copy but contains additional
information from provisioning such as ip address, node id, etc.

To cleanup the machine, just execute the following teflo command below.

.. code-block:: none

    (teflo) $ teflo run -t cleanup -s .teflo/.results/results.yml -w .

We pointed teflo to the updated descriptor file. This provides teflo with
the updated information from the provision task.
