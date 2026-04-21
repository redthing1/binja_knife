from __future__ import annotations

import threading

# Serialize short shared Binary Ninja operations. Do not hold this around
# arbitrary user code, or one sleeping session will stall unrelated sessions.
BN_LOCK = threading.RLock()

# root globals are shared across connections; protect them explicitly
ROOT_LOCK = threading.RLock()
