import xml.etree.ElementTree as ET
from xml.dom import minidom


def verify_relayable_signature(public_key, doc, signature):
    # Parse the XML document
    root = ET.fromstring(doc)

    # Get the signature element
    signature_element = root.find(".//Signature")

    # Get the signed info element
    signed_info_element = signature_element.find(".//SignedInfo")

    # Get the canonicalization method
    canonicalization_method = signed_info_element.get("CanonicalizationMethod")

    # Get the signature method
    signature_method = signature_element.get("SignatureMethod")

    # Get the reference element
    reference_element = signed_info_element.find(".//Reference")

    # Get the digest method
    digest_method = reference_element.get("DigestMethod")

    # Get the digest value
    digest_value = reference_element.get("DigestValue")

    # Get the key info element
    key_info_element = signature_element.find(".//KeyInfo")

    # Get the public key
    public_key_element = key_info_element.find(".//PublicKey")
    public_key = public_key_element.text

    # Verify the signature
    signature_verified = False
    if signature_method == "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256":
        signature_verified = rsa.verify(digest_value, signature, public_key)
    elif signature_method == "http://www.w3.org/2001/04/xmldsig-more#rsa-sha1":
        signature_verified = rsa.verify(digest_value, signature, public_key)
    else:
        raise ValueError("Unsupported signature method")

    # Return the result
    return signature
