import imaplib
import email
from email.header import decode_header

def decode_maybe(s, enc=None):
    if isinstance(s, bytes):
        return s.decode(enc or "utf-8", errors="replace")
    return s

def decode_mime_header(value):
    parts = decode_header(value or "")
    return "".join(decode_maybe(t, enc) for t, enc in parts)

def read(em, p, n, box="INBOX", HOST="imap.gmail.com"):
    imap = imaplib.IMAP4_SSL(HOST, 993)
    imap.login(em, p)
    imap.select(box)

    typ, data = imap.search(None, "ALL")
    if (typ != "OK"):
        raise RuntimeError("Search failed")

    ids = data[0].split()
    for msg_id in ids[-n:]:
        typ, msg_data = imap.fetch(msg_id, "(RFC822.HEADER)")
        if typ != "OK":
            continue
        raw = msg_data[0][1]
        msg = email.message_from_bytes(raw)

        subject = decode_mime_header(msg.get("Subject"))
        from_ = decode_mime_header(msg.get("From"))
        date_ = msg.get("Date")
        print(f"{date_} {from_}: {subject}")

    imap.logout()

