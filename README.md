# dpa-digitalwires-to-newsmlG2
This project provides a method for transforming entries from the dpa-digitalwires format into an
approximate [NewsML-G2](https://iptc.org/std/NewsML-G2/2.34/specification/NewsML-G2-2.34-specification.html) article format. We tried to closely emulating the NewsML-G2 standard while acknowledging inherent limitations.

This converter creates an **approximation** of the NewsML-G2 format because some information needed for a precise transformation may not be available in the dpa-digitalwires source data. Despite these limitations, the tool provides a practical solution for enhancing interoperability and workflow efficiency.

## Getting started

```
pipenv install "git+https://github.com/dpa-newslab/dpa-digitalwires-to-newsmlg2.git
```

This setup was tested with:

* =Python3.12

Install requirements by calling:

```
pip install -r requirements.txt
```

```python
import newsmlg2
import json

with open("path/to/digitalwires.json") as f:
    dw = json.load(f)
    g2_messages = newsmlg2.convert_to_g2(dw)
```

## Tests

```
pip install -r requirements-test.txt
pytest -s tests
```

## Limitations
- no wordcount
- item class, is derived from `article_html` and `associations`
- linkbox is missing a rank therefore order in links cannot be ensured
- there is always only one headline

## License

Copyright 2025 dpa-IT Services GmbH

Apache License, Version 2.0 - see `LICENSE` for details.