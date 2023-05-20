# Toolchain

## VSCode

Add "Acme Cross Assembler (C64)" extension

## vim

[vim-acme](https://github.com/leissa/vim-acme)

Symlinks:

```bash
# Create if required
mkdir ~/.vim/ftdetect
mkdir ~/.vim/syntax
```

From the directory where you git cloned the plugin:

```bash
ln -s `pwd`/vim-acme/ftdetect/acme.vim ~/.vim/ftdetect/.
ln -s `pwd`/vim-acme/syntax/acme.vim ~/.vim/syntax/.
```
