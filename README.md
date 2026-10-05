# gauntlet-automations-demo (lab scaffold)

Tiny Python repo for the Gauntlet Oct 6 Automations + model-picker demo.
Push to a PRIVATE repo: github.com/rabiya-cursor/gauntlet-automations-demo

- `main` has a small pricing module, tests, and one intentional lint issue (unused import) + one latent bug.
- `feat/bulk-discount` adds a bulk-discount tier with an off-by-one bug and no test. Open this as the live PR.

## Demo environment check

Python 3.10+ is required. From the repo root:

```bash
pip install -r requirements-dev.txt
ruff check .
pytest -q
```

`ruff check .` is expected to report the unused import in `src/utils.py`. `pytest -q` should pass.
