#!/usr/bin/env python
import os
import sys
import subprocess


def create_spatialite_db():
    if not os.path.isfile("db.sqlite3"):
        subprocess.call(['spatialite', 'db.sqlite3', 'SELECT InitSpatialMetaData();'])


if __name__ == "__main__":
    create_spatialite_db()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TheAuditTrail.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
