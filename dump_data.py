import os
import json
from django.core.management import call_command
from io import StringIO

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Emporium.settings")

import django
django.setup()


def dump_data(model_name):
    buffer = StringIO()
    call_command('dumpdata', model_name, stdout=buffer)
    json_data = buffer.getvalue()
    file_name = f'fixtures/assortment/{model_name.split(".")[1].lower()}.json'
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(json.loads(json_data), f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        model_name = sys.argv[1]
        dump_data(model_name)
    else:
        print("Please provide the model name as a command line argument.")
