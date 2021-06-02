=====================================
openclean - Reference Data Repository
=====================================

.. image:: https://img.shields.io/badge/License-BSD-green.svg
    :target: https://github.com/VIDA-NYU/openclean-reference-data/blob/master/LICENSE


.. figure:: https://github.com/VIDA-NYU/openclean-reference-data/blob/master/docs/graphics/logo.png
    :align: center
    :alt: openclean Logo


About
=====

This repository contains a collection of reference datasets that can be used for different data cleaning tasks. The repository is part of the `openclean project <https://github.com/VIDA-NYU/openclean-core/>`_. In **openclean** the datasets can easily be downloaded and accessed using the ``openclean.data.refdata.RefStore``.


Datasets
========

The following datasets are currently contained in the repository:

- encyclopaedia_britannica:us_cities: Names of cities in the U.S. together with the name of the state parsed from the `Encyclopaedia Britannica US Cities web site. <https://www.britannica.com/topic/list-of-cities-and-towns-in-the-United-States-2023068>`_
- restcountries.eu: Information about countries in the world available from the `restcountries.eu project <https://restcountries.eu/>`_.
- usps:street_abbrev: Mapping of common street type abbreviations to a standard format parsed from the `C1 Street Suffix Abbreviations web site <https://pe.usps.com/text/pub28/28apc_002.htm>`_.
- usps:secondary_unit_designators: `C2 Secondary Unit Designators <https://pe.usps.com/text/pub28/28apc_003.htm>`_.
- wikipedia:us_states: List of the 50 states in the United States, with their current capital, largest city, the date they ratified the U.S. Constitution or were admitted to the Union, population and area data, and number of representative(s) in the U.S. House of Representatives (`from Wikipedia <https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States>`_).


Parser and Downloader
=====================

This repository also contains a collection of Python scripts that were used to download and parse the different datasets.
