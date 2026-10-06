def verify_relayable_signature(public_key, doc, signature):
    from lxml import etree
    from cryptography.exceptions import InvalidSignature
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import padding
    """
    Verify the signed XML elements to ensure the claimed author generated the message.
    """
    try:
        # Parse the XML document
        root = etree.fromstring(doc)
        
        # Canonicalize the XML using exclusive canonicalization (assumed method)
        canonicalized_doc = etree.tostring(root, method="c14n", exclusive=True)
        
        # Verify the signature using the public key
        public_key.verify(
            signature,
            canonicalized_doc,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except (etree.XMLSyntaxError, InvalidSignature, ValueError, TypeError):
        return False
