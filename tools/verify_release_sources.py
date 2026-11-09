"""Fail closed if the workflow is building different source files."""
from pathlib import Path
import hashlib
import json

expected = json.loads(Path('release-sources.json').read_text(encoding='utf-8'))
for name, digest in expected.items():
    actual = hashlib.sha256(Path(name).read_bytes()).hexdigest()
    if actual != digest:
        raise SystemExit(f'Release source mismatch: {name}')
source = Path('lib/main.dart').read_text(encoding='utf-8')
assert '是否扣计划剩余额度' in source
assert '是否抵扣代管余额' in source
assert '记一笔支出 · 0.2.3' in source
print('Verified 0.2.3 expense controls and all release source hashes.')
