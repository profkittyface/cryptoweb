# cryptoweb

Cryptoweb is a small django application that provides a web interface for basic GPG messaging.

It supports maintaining private keys on your server as well as an address book for the public keys of your contacts.

This app is designed to be run locally but can be set up to run on a public network, just please enable SSL as the passphrase is posted in the web request.

To run locally, install the following packages:

<pre>
pip install django
pip install gnupg
apt-get install gnupg
</pre>


* OSX/Windows users will have to install GPGTools
<a>https://gpgtools.org/</a>

 and run ./manage.py runserver
