#!/bin/bash
source ~/messages/.venv/bin/activate
echo "venv activated"
cd ~/messages/msgs_is
echo "entered to core folder"
python manage.py clearsessions
echo "sessions are cleared"
