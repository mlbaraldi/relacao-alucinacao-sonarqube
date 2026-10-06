import xmlsec


def verify_relayable_signature(public_key, doc, signature):
    """
    Verify the signed XML elements to have confidence that the claimed
    author did actually generate this message.
    """
    # Create a template for the signature context
    template = xmlsec.template.create(
        doc,
        xmlsec.Transform.EXCL_C14N,
        xmlsec.Transform.RSA_SHA1,
    )

    # Load the public key
    key = xmlsec.Key.from_file(public_key, xmlsec.KeyFormat.PEM)

    # Create a digital signature context (dsig_ctx)
    dsig_ctx = xmlsec.DSigCtx(key)

    # Verify the signature
    try:
        dsig_ctx.verify(template)
        print("Signature is valid.")
    except xmlsec.DSigError:
        print("Signature is invalid.")
