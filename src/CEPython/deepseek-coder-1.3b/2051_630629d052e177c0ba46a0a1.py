import hashlib
import rsa


def verify_relayable_signature(public_key, doc, signature):
    """
    Verify the signed XML elements to have confidence that the claimed
    author did actually generate this message.
    """
    # First, we need to decode the signature from base64
    signature = rsa.decrypt(base64.b64decode(signature), public_key)

    # Then, we need to create a hash of the document
    hash_doc = hashlib.sha256(doc.encode()).digest()

    # Finally, we can compare the hash of the document with the signature
    return signature == hash_doc
