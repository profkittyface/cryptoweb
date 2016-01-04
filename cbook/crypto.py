import gnupg
import re
from django.conf import settings




class BlackBox():
    gpghome = getattr(settings, "GPGHOME", None)

    def __init__(self):
        self.gpg = gnupg.GPG(homedir=self.gpghome, ignore_homedir_permissions=True)

    def generate_key(self, email, passphrase=None):
        input_data = self.gpg.gen_key_input(
            name_email=email,
            key_type='RSA',
            passphrase=passphrase)
        key = self.gpg.gen_key(input_data)
        return key.fingerprint

    def import_key(self, key):
        import_result = self.gpg.import_keys(key)
        if not import_result.fingerprints:
            raise Exception("Unable to import key.")
        # .fingerprints returns a unicode, needs to be string
        return str(import_result.fingerprints[0])

    def encrypt(self, message, fingerprint=None, key=None ):
        if key:
            fingerprint = self.import_key(key)
        unencrypted_string = message
        encrypted_data = self.gpg.encrypt(unencrypted_string, fingerprint)
        encrypted_string = encrypted_data.data
        return encrypted_string

    def decrypt(self, message, passphrase=None, fingerprint=None):
        result = self.gpg.decrypt(message=message, passphrase=passphrase)
        if result.data is '':
            raise Exception("Unable to decrypt message")
        return result.data

    def list_keys(self):
        key_list = []
        for key_dict in self.gpg.list_keys():
            key_list.append(key_dict)
        return key_list

    def get_key(self, fingerprint):
        return self.gpg.export_keys(fingerprint)

    def delete_key(self, fingerprint):
        result = self.gpg.delete_keys(fingerprint)
        if result.data is '':
            raise Exception("Unable to delete key")
            print result.problem_reason
        else:
            return True

