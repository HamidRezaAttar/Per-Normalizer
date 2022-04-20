# Per-Normalizer
Persian text cleaner with additional features on Parsivar package.


# How to use

## Pre Requirements
```bash
pip install parsivar
```

```bash
git clone https://github.com/HamidRezaAttar/Per-Normalizer
cd /content/Per-Normalizer
```

## Normalizer

```python
from per_normalizer import Normalizer

module = Normalizer()

text = " INPUT TEXT "

output = module._normalize_text(text)
```
