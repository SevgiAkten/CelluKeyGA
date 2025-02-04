Installation
============

This section provides detailed instructions for installing `CelluKeyGA` and its dependencies.

Requirements
------------

Before installing `CelluKeyGA`, make sure you have the following installed:

- Python 3.7 or higher
- `pip` package manager

Installing from PyPI
---------------------

The easiest way to install `CelluKeyGA` is via PyPI. You can use `pip` to install it directly from the Python Package Index:

.. code-block:: bash

    pip install CelluKeyGA

Installing from Source
----------------------

To install `CelluKeyGA` from source, follow these steps:

1. Clone the repository from GitHub:

   .. code-block:: bash

       git clone https://github.com/SevgiAkten/CelluKeyGA.git

2. Navigate to the cloned repository directory:

   .. code-block:: bash

       cd CelluKeyGA

3. Install the package using `pip`:

   .. code-block:: bash

       pip install .

Optional Dependencies
---------------------

`CelluKeyGA` has optional dependencies for certain features. To use these features, you may need to install additional packages:

- **Jupyter Notebooks**: If you plan to use Jupyter Notebooks for tutorials or examples, install `jupyter`:

  .. code-block:: bash

      pip install jupyter

- **Matplotlib**: For visualizing optimization results, install `matplotlib`:

  .. code-block:: bash

      pip install matplotlib

Verifying the Installation
--------------------------

To verify that `CelluKeyGA` is installed correctly, you can import it in Python:

.. code-block:: python

    import CelluKeyGA
    print(CelluKeyGA.__version__)

If no errors occur, the installation is successful.

Troubleshooting
---------------

If you encounter any issues during installation, try the following steps:

1. Ensure you are using Python 3.7 or higher by running:

   .. code-block:: bash

       python --version

2. Make sure `pip` is up-to-date:

   .. code-block:: bash

       pip install --upgrade pip

3. If issues persist, refer to the GitHub repository for troubleshooting tips or to submit an issue.

Uninstallation
--------------

To uninstall `CelluKeyGA`, you can use the following command:

.. code-block:: bash

    pip uninstall CelluKeyGA
