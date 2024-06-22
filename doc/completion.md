# Toolchain

## VSCode

Add "Acme Cross Assembler (C64)" extension

## vim

See [vim-acme](https://github.com/leissa/vim-acme)

At a glance:

- Clone the plugin repository
- Create a symlink in your vim configuration directory to the plugin's file detection file
- Same for the syntax highlighting file.

In short:

```bash
# Create config directories if required
$ mkdir ~/.vim/ftdetect
$ mkdir ~/.vim/syntax

# From the directory where you git cloned the plugin
$ cd path_to_plugin_repo
$ ln -s `pwd`/vim-acme/ftdetect/acme.vim ~/.vim/ftdetect/.
$ ln -s `pwd`/vim-acme/syntax/acme.vim ~/.vim/syntax/.
```

## novim

Similar to vim, but with different paths:

```bash
# Create config directories if required
$ mkdir ~/.config/nvim/ftdetect
$ mkdir ~/.config/nvim/syntax

# From the directory where you git cloned the plugin
$ cd path_to_plugin_repo
$ ln -s `pwd`/vim-acme/ftdetect/acme.vim ~/.config/nvim/ftdetect/.
$ ln -s `pwd`/vim-acme/syntax/acme.vim ~/.config/nvim//syntax/.
```

See [new-filetype](https://neovim.io/doc/user/filetype.html#new-filetype) and [syntax](https://neovim.io/doc/user/syntax.html) documentation for more information.
