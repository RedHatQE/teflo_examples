Run Tests
=========

First compile the Sample class.

.. code-block:: bash

    $ javac Sample.java

Next compile the SampleTest class.

.. code-block:: bash

    $ javac SampleTest.java

Compile the UnitTestRunner class.

.. code-block:: bash

    $ javac UnitTestRunner.java

Lastly compile the Custom Execution Listener class.

.. code-block:: bash

    $ javac CustomExecutionListener.java

Now that both files have been successfully compiled. Lets run the tests.

.. code-block:: bash

    # replace junit-4.10.jar with your jar file and include path
    $ java -cp :junit-4.10.jar UnitTestRunner SampleTest
