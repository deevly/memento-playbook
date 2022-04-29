import boto3
import base64

kms = boto3.client('kms')

def kms_decrypt(ciphertext, key):
    return kms.decrypt(EncryptionAlgorithm='RSAES_OAEP_SHA_256',KeyId=key,CiphertextBlob=bytes(base64.b64decode(ciphertext))).get('Plaintext').decode('utf-8')

def kms_encrypt(plaintext, key):
    return base64.b64encode(kms.encrypt(EncryptionAlgorithm='RSAES_OAEP_SHA_256',KeyId=key,Plaintext=plaintext).get('CiphertextBlob'))

class FilterModule(object): 
    def filters(self):
        return { 'kms_encrypt': kms_encrypt, 'kms_decrypt': kms_decrypt } 
