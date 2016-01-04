#!/usr/bin/python
import gnupg
gpg = gnupg.GPG(homedir='/home/ahunt/gpghome', verbose=True, ignore_homedir_permissions=True)
input = gpg.gen_key_input(key_type='RSA', key_length=1024, passphrase='secret')
keyresult = gpg.gen_key(input)
