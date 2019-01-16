====================
django-template-uuid
====================

.. image:: https://travis-ci.org/mpasternak/django-template-uuid.svg
   :target: https://travis-ci.org/mpasternak/django-template-uuid


Assign an unique ID to every Django page rendered.

Usage
-----

1. Add ``template_uuid`` to ``INSTALLED_APPS``

2. Use in template like:

::

   <body>

     {% load template_uuid %}
     {% uuid4 my_unique_id %}

     My unique ID is: {{ my_unique_id }}.

   </body>
