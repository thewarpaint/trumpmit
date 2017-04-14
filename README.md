# `git trumpmit`!

Make Git Commit Messages Great Again!

## How to

1. Download [trumpmit.py](https://github.com/thewarpaint/trumpmit/blob/master/trumpmit.py), place it
   somewhere in your `$PATH` list and run `$ chmod +x` on it.

2. Add the `git` alias:

```sh
$ git config --global alias.trumpmit '!git commit -m "$(trumpmit.py)"'
```

3. Add your files with `git add ...` and then get a great, wonderful, yuge commit message:

```sh
$ git trumpmit

[master abc123d] I inherited a MESS and am in the process of fixing it.
 666 files changed, 1776 insertions(+), 43 deletions(-)
 create mode 100644 README.md
 mode change 100644 => 100755 trumpmit.py
```

4. ???

5. PROFIT!

## Wanna try before you buy?

[Use the simulator!](https://thewarpaint.github.io/trumpmit/)
