
# binja-knife

a cli, `bnk`, for driving a binaryninja server.

it talks to the [`Knife Server`](./server) plugin over rpyc and provides:
- named, stateful sessions
- batteries-included tools (strings, xrefs, IL, tags, common edits)
- arbitrary server-side python execution (`bnk py *`)

## quick start

server:
- in the gui, run `Knife Server/Start server`
- defaults: `127.0.0.1:18812`

client:
```sh
uv run bnk -h
uv run bnk ping
```

multiline python:
```sh
cat <<'PY' | uv run bnk -s demo py exec -
print("hello from binja")
__result__ = 123
PY
```

## install `bnk`

for a global `bnk` command:
```sh
uv tool install -e .
bnk -h
```
