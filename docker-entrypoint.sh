#### FILE START
#!/bin/bash

if [ -z "$PORT" ]
then
    #echo "\$PORT is empty"
    PORT=8000
fi

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput
