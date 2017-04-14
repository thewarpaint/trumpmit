# `git trumpmit`!

## How to

1. Download [trumpmit.py](https://github.com/thewarpaint/trumpmit/blob/master/trumpmit.py)

2. Add the `git` alias:

```sh
$ git config --global alias.trumpmit '!git commit -m "$(./trumpmit.py)"'
```

3. Do the `git add ...` part and then get a great, wonderful, yuge commit message:

```sh
$ git trumpmit

[master abc123d] I inherited a MESS and am in the process of fixing it.
 666 files changed, 43 insertions(+), 1 deletion(-)
 create mode 100644 README.md
 mode change 100644 => 100755 trumpmit.py
```

4. ???

5. PROFIT!
