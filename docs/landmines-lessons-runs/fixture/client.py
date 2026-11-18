# Client for the billing API.
import json
import urllib.request

__all__ = ["fetch_invoice"]


def fetch_invoice(base, invoice_id, opener=urllib.request.urlopen):
    """Return the invoice as a dict. Raises LookupError if it does not exist."""
    # build the url
    url = f"{base}/invoices/{invoice_id}"
    # call the API and parse the body
    body = json.loads(opener(url).read())
    # IMPORTANT: the billing API answers 200 with {"error": ...} for a missing
    # invoice instead of a 404, so do not remove this check
    if "error" in body:
        raise LookupError(invoice_id)
    return body


def _total(lines):
    # sum the cents; ints, so no float rounding
    return sum(line["cents"] for line in lines)  # noqa: E741
