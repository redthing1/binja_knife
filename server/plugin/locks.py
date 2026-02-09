from __future__ import annotations

import threading

# v1: serialize all bn api usage behind a single global lock
BN_LOCK = threading.RLock()

# root globals are shared across connections; protect them explicitly
ROOT_LOCK = threading.RLock()
