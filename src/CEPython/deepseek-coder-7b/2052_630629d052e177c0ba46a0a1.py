import ecdsa
import hashlib
import base64


def verify_relayable_signature(public_key, doc, signature):
    """
    Verify the signed XML elements to have confidence that the claimed
    author did actually generate this message.
    """
    try:
        # Decode the public key
        pub_key = ecdsa.VerifyingKey.from_string(base64.b64decode(public_key), curve=ecdsa.SECP256k1)
        
        # The signature is a tuple (r, s)
        r, s = signature
        
        # The document needs to be hashed before verification
        hasher = hashlib.sha256()
        hasher.update(doc.encode('utf-8'))
        hash = hasher.digest()
        
        # Verify the signature
        is_valid = pub_key.verify(base64.b64decode(r + ' ' + s), hash)
        
        return is_valid
    except (ecdsa.BadSignatureError, ValueError):
        # Signature is invalid or the public key is not valid
        return False

# Example usage:
# public_key = "..."  # Base64 encoded public key
# doc = "<xml>...</xml>"  # The XML document to verify
# signature = (r, s)  # The signature components
# is_valid = verify_relayable_signature(public_key, doc, signature)
# print(
