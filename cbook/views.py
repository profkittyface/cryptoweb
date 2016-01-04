from django.http import HttpResponse
from django.shortcuts import render
from .crypto import BlackBox


def index(request):
    return render(request, 'cbook/index.html')


def encrypt_index(request, fingerprint=None):
    if fingerprint:
        bb = BlackBox()
        key = bb.get_key(fingerprint)
    else:
        key = ''
    return render(request, 'cbook/encrypt_index.html', {'key': key})


def encrypt_post(request):
    key = request.POST['key']
    plaintext = request.POST['plaintext']
    bb = BlackBox()
    encrypted_text = bb.encrypt(plaintext, key=key)
    return render(request, 'cbook/encrypt_output.html', {'encrypted_text': encrypted_text})


def decrypt_index(request):
    bb = BlackBox()
    key_list = bb.list_keys()
    return render(request, 'cbook/decrypt_index.html', {'key_list': key_list})


def decrypt_post(request):
    message = request.POST['encrypted_message']
    passphrase = ''
    if request.POST['passphrase']:
        passphrase = request.POST['passphrase']
    bb = BlackBox()
    decrypted_output = bb.decrypt(message, passphrase=passphrase)
    #return HttpResponse(decrypted_output)
    return render(request, 'cbook/decrypt_output.html', {'decrypted_output': decrypted_output})


def address_list_index(request):
    bb = BlackBox()
    key_list = bb.list_keys()
    return render(request, 'cbook/address_list_index.html', {'key_list': key_list})


def address_list_add(request):
    key = request.POST['key']
    bb = BlackBox()
    bb.import_key(key)
    key_list = bb.list_keys()
    return render(request, 'cbook/address_list_index.html', {'key_list': key_list})


def address_list_delete(request, fingerprint=None):
    bb = BlackBox()
    bb.delete_key(fingerprint)
    key_list = bb.list_keys()
    return render(request, 'cbook/address_list_index.html', {'key_list': key_list})

def address_list_encrypt(request):
    return HttpResponse("Not done yet")


def generate_key_index(request):
    return render(request, 'cbook/generate_key_index.html')

def generate_key_post(request):
    email = request.POST['email']
    passphrase = request.POST['passphrase']
    bb = BlackBox()
    bb.generate_key(email, passphrase)
    return render(request, 'cbook/generate_key_output.html')

