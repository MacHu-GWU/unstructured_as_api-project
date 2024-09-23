
.. .. image:: https://readthedocs.org/projects/unstructured-as-api/badge/?version=latest
    :target: https://unstructured-as-api.readthedocs.io/en/latest/
    :alt: Documentation Status

.. .. image:: https://github.com/MacHu-GWU/unstructured_as_api-project/actions/workflows/main.yml/badge.svg
    :target: https://github.com/MacHu-GWU/unstructured_as_api-project/actions?query=workflow:CI

.. .. image:: https://codecov.io/gh/MacHu-GWU/unstructured_as_api-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/unstructured_as_api-project

.. .. image:: https://img.shields.io/pypi/v/unstructured-as-api.svg
    :target: https://pypi.python.org/pypi/unstructured-as-api

.. .. image:: https://img.shields.io/pypi/l/unstructured-as-api.svg
    :target: https://pypi.python.org/pypi/unstructured-as-api

.. .. image:: https://img.shields.io/pypi/pyversions/unstructured-as-api.svg
    :target: https://pypi.python.org/pypi/unstructured-as-api

.. image:: https://img.shields.io/badge/Release_History!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/unstructured_as_api-project/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/unstructured_as_api-project

------

.. .. image:: https://img.shields.io/badge/Link-Document-blue.svg
    :target: https://unstructured-as-api.readthedocs.io/en/latest/

.. .. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://unstructured-as-api.readthedocs.io/en/latest/py-modindex.html

.. .. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/unstructured_as_api-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/unstructured_as_api-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/unstructured_as_api-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/unstructured-as-api#files


Welcome to ``unstructured_as_api`` Documentation
==============================================================================


Introduction
------------------------------------------------------------------------------
unstructured_as_api is a project that transforms the open-source unstructured data processing library, Unstructured, into a scalable and accessible API service. This project aims to simplify the process of working with unstructured data by eliminating installation complexities and resource provisioning concerns.


Project Overview
------------------------------------------------------------------------------
The unstructured_as_api project provides a FastAPI-based service that exposes the capabilities of the Unstructured library through simple API endpoints. It allows users to process unstructured data, particularly focusing on PDF partitioning in this implementation, without the need to install or manage the Unstructured library directly.


Key Features
------------------------------------------------------------------------------
- Easy-to-use API: Simple REST API endpoints for processing unstructured data.
- Scalable Architecture: Automatically scales to handle varying workloads.
- Synchronous and Asynchronous Processing: Supports both immediate processing for small payloads and background processing for larger files.
- S3 Integration: Allows processing of documents stored in Amazon S3 buckets.
- Job Management: Provides job IDs and status checks for asynchronous processing.


API Endpoints
------------------------------------------------------------------------------
- ``/part_pdf/`` (POST): Synchronous endpoint for partitioning small PDF documents.
- ``/start_part_pdf/`` (POST): Asynchronous endpoint for starting the partitioning of large PDF documents.
- ``/get_part_pdf/`` (POST): Retrieves the results of an asynchronous partitioning job.


Usage Examples
------------------------------------------------------------------------------
- `Fast API entry point <https://github.com/MacHu-GWU/unstructured_as_api-project/blob/main/main.py>`_
- `Usage example (notebook) <https://github.com/MacHu-GWU/unstructured_as_api-project/blob/main/docs/source/01-Example-Usage/index.ipynb>`_


.. _install:

Install
------------------------------------------------------------------------------

``unstructured_as_api`` is released on PyPI, so all you need is to:

.. code-block:: console

    $ pip install unstructured-as-api

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade unstructured-as-api
