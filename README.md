radosgw-rest-admin
==================

Radosgw admin tool using the radosgw admin rest interface.

First steps:
============

In order to use ceph radosgw admin interface it's needed to create a user
with the correct privileges. e.g.:

    radosgw-admin user create --uid admin --display-name admin
    radosgw-admin caps add --uid=admin --caps="users=*" 
    radosgw-admin caps add --uid=admin --caps="buckets=*"
    radosgw-admin caps add --uid=admin --caps="metadata=*"
    radosgw-admin caps add --uid=admin --caps="usage=*"

With this use it should be possible to use the rest interface:

    export S3_ACCESS_KEY_ID=2A52ZT4GFI548MCGZ3G4
    export S3_HOSTNAME=radosgw1
    export S3_SECRET_ACCESS_KEY=Z08zn58H4l29zzXRXGJyzjUOsWeB7ugtYfmKh0MB
    
    radosgw_rest_admin.py user-list --uid admin
