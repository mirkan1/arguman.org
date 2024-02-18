Traceback (most recent call last):
  File "web/manage.py", line 10, in <module>
    execute_from_command_line(sys.argv)
  File "/usr/local/lib/python3.8/site-packages/django/core/management/__init__.py", line 442, in execute_from_command_line
    utility.execute()
  File "/usr/local/lib/python3.8/site-packages/django/core/management/__init__.py", line 416, in execute
    django.setup()
  File "/usr/local/lib/python3.8/site-packages/django/__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "/usr/local/lib/python3.8/site-packages/django/apps/registry.py", line 116, in populate
    app_config.import_models()
  File "/usr/local/lib/python3.8/site-packages/django/apps/config.py", line 269, in import_models
    self.models_module = import_module(models_module_name)
  File "/usr/local/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 843, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/code/web/profiles/models.py", line 16, in <module>
    from django.utils.translation import ugettext_lazy as _
ImportError: cannot import name 'ugettext_lazy' from 'django.utils.translation' (/usr/local/lib/python3.8/site-packages/django/utils/translation/__init__.py)
bin/rebuild_run.sh: line 4: 1: command not found