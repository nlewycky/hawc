Health Assessment Workspace Collaborative
=========================================

.. image:: https://zenodo.org/badge/25273569.svg
   :target: https://zenodo.org/badge/latestdoi/25273569

The Health Assessment Workspace Collaborative (HAWC) is a website designed to
capture key data and analyses performed in conducting human-health assessment
of chemicals and other environmental exposures in-order to establish hazard
identification and potentially derive quantitative levels of concern.

For more information, please see the `documentation <http://hawc.readthedocs.org/>`_.


# Squashing migrations

The brute-force method; required for django 2.0 migration

.. code-block:: bash

    # delete old migrations
    rm animal/migrations/00*
    rm assessment/migrations/00*
    rm bmd/migrations/00*
    rm epi/migrations/00*
    rm epimeta/migrations/00*
    rm invitro/migrations/0*
    rm lit/migrations/0*
    rm mgmt/migrations/0*
    rm myuser/migrations/0*
    rm riskofbias/migrations/0*
    rm study/migrations/0*
    rm summary/migrations/0*

    # delete from db
    psql -c 'delete from django_migrations;'

    # fake new migrations and migrate
    python manage.py makemigrations
    python manage.py migrate --fake
