###################
 Building datasets
###################

************
 Principles
************

.. figure:: build.png
   :alt: Building datasets
   :scale: 50%

   Building datasets

Concepts
========

Source
------

The source is the data that will be used to build the dataset. The
source

Sources are:

-  mars
-  opendap
-  constants
-  grib
-  netcdf

Join
----

The join is the process of combining the source data to form the input

Pipe
----

The pipe is the process of transforming the input data to form the
output

Filter
------

The filter is the process of selecting the output data from the input

Getting started
===============

.. code:: yaml

   description: Boundary condition for MetNO's LAM model rotated
   # dataset_status: experimental
   # purpose: aifs
   name: aifs-ea-an-oper-0001-mars-n320-2020-2023-6h-v2-metno-bc-rotated
   # config_format_version: 2


   dates:
     start: 2020-02-05 00:00:00
     end: 2023-12-31 18:00:00
     frequency: 6h

   build:
     group_by: monthly

   input:
     join:
       - mars:
           class: ea
           param: [10u, 10v, 2d, 2t, msl, skt, sp, tcw, lsm, sdor, slor, z]
           levtype: sfc

       - mars:
           class: ea
           param: [r, t, u, v, w, z]
           levtype: pl
           level: [50, 100, 150, 200, 250, 300, 400, 500, 700, 850, 925, 1000]

       - constants:
           template: ${input.join.0.mars}
           param:
           - cos_latitude
           - cos_longitude
           - sin_latitude
           - sin_longitude
           - cos_julian_day
           - cos_local_time
           - sin_julian_day
           - sin_local_time
           - insolation

   output:
     # chunking: {dates: 1, ensembles: 1}
     # dtype: float32
     # flatten_grid: True
     order_by:
       - valid_datetime
       - param_level
       - number
     statistics: param_level
     # statistics_end: 2022
     remapping:
       param_level: "{param}_{levelist}"

Top-level keys
==============

dadkas;k;level

-  description
-  dataset_status
-  purpose
-  name
-  config_format_version

Dates
=====

The ``dates`` block specifies the start and end dates of the dataset, as
well as the frequency of the data. The frequency is specified in hours.

Input
=====

The ``input`` block specifies the input data that will be used to build
the dataset. The ``join`` block specifies the datasets that will be
joined together to form the input data. The ``mars`` block specifies the
MARS datasets that will be used. The ``constants`` block specifies the
constants that will be used.

Output
======

The ``output`` block specifies the output data that will be built. The
``chunking`` block specifies the chunking of the output data. The
``dtype`` block specifies the data type of the output data. The
``flatten_grid`` block specifies whether the output data will be
flattened. The ``order_by`` block specifies the order of the output
data. The ``statistics`` block specifies the statistics that will be
calculated. The ``statistics_end`` block specifies the end date of the
statistics. The ``remapping`` block specifies the remapping of the
output data.
