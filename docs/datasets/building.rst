.. _datasets-building:

###################
 Building datasets
###################

..
   ************

..
   Principles

..
   ************

..
   .. figure:: build.png

..
   :alt: Building datasets

..
   :scale: 50%

..
   Building datasets

**********
 Concepts
**********

date
   Throughout this document, the term `date` refers to a date and time,
   not just a date. A training dataset is covers a continuous range of
   dates with a given frequency. Missing dates are still part of the
   dataset, but the data are missing and marked as such using NaNs.
   Dates are always in UTC, and refer to date at which the data is
   valid. For accumulations and fluxes, that would be the end of the
   accumulation period.

variable
   A `variable` is meteorological parameter, such as temperature, wind,
   etc. Multilevel parameters are treated as separate variables, one for
   each level. For example, temperature at 850 hPa and temperature at
   500 hPa will be treated as two separate variables (`t_850` and
   `t_500`).

field
   A `field` is a variable at a given date. It is represented by a array
   of values at each grid point.

source
   The `source` is a software component that given a list of dates and
   variables will return the corresponding fields. A example of source
   is ECMWF's MARS archive, a collection of GRIB or NetCDF files, a
   database, etc. See :ref:`dataset-sources` for more information.

filter
   A `filter` is a software component that takes as input the output of
   a source or the output of another filter can modify the fields and/or
   their metadata. For example, typical filters are interpolations,
   renaming of variables, etc. See :ref:`dataset-filters` for more
   information.

************
 Operations
************

In order to build a training dataset, sources and filters are combined
using the following operations:

join
   The join is the process of combining several sources data. Each
   source is expected to provide different variables at the same dates.

pipe
   The pipe is the process of transforming fields using filters. The
   first step of a pipe is typically a source, a join or another pipe.
   The following steps are filters.

concat
   The concatenation is the process of combining different sets of
   operation that handle different dates. This is typically used to
   build a dataset that spans several years, when the several sources
   are involved, each providing a different period.

*****************
 Getting started
*****************

.. literalinclude:: building.yaml
   :language: yaml

****************
 Top-level keys
****************

dadkas;k;level

-  description
-  dataset_status
-  purpose
-  name
-  config_format_version

*******
 Dates
*******

The ``dates`` block specifies the start and end dates of the dataset, as
well as the frequency of the data. The frequency is specified in hours.

*******
 Input
*******

The ``input`` block specifies the input data that will be used to build
the dataset. The ``join`` block specifies the datasets that will be
joined together to form the input data. The ``mars`` block specifies the
MARS datasets that will be used. The ``constants`` block specifies the
constants that will be used.

********
 Output
********

The ``output`` block specifies the output data that will be built. The
``chunking`` block specifies the chunking of the output data. The
``dtype`` block specifies the data type of the output data. The
``flatten_grid`` block specifies whether the output data will be
flattened. The ``order_by`` block specifies the order of the output
data. The ``statistics`` block specifies the statistics that will be
calculated. The ``statistics_end`` block specifies the end date of the
statistics. The ``remapping`` block specifies the remapping of the
output data.
