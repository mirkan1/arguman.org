  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 843, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/code/web/profiles/models.py", line 11, in <module>
    from premises.models import Report, Premise
  File "/code/web/premises/models.py", line 31, in <module>
    from nouns.models import Noun
  File "/code/web/nouns/models.py", line 151, in <module>
    class Keyword(models.Model):
  File "/code/web/nouns/models.py", line 155, in Keyword
    noun = models.ForeignKey(Noun, related_name="keywords")
TypeError: __init__() missing 1 required positional argument: 'on_delete'