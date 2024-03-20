.. _datasets-building:

###################
 Building datasets
###################

..
   .. figure:: build.png

..
   :alt: Building datasets

..
   :scale: 50%

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
