import re
import urllib.request
import html

def report (identifier):

    ### Find type of identifier.

    normal = re.compile(r"^([\w\-]+ ?)+$") # e.g. Teresa Sullivan
    inverted = re.compile(r"^([\w\-]+), (\w+)$") # e.g. Sullivan, Teresa
    number = re.compile(r"^(\d{9})$") # e.g. 161048349
    hyphenated = re.compile(r"^([\w\-]+)$") # e.g. teresa-sullivan

    if (normal.match(identifier)):
        # e.g. Teresa Sullivan
        result = identifier.split()
        lookup = "-".join(result)
        lookup = lookup.lower()
    elif (inverted.match(identifier)):
        # e.g. Sullivan, Teresa
        result = inverted.match(identifier)
        lookup = result.group(2).lower() + "-" + result.group(1).lower()
    elif (number.match(identifier)):
        # e.g. 161048349
        lookup = identifier
    elif (hyphenated.match(identifier)):
        # e.g. teresa-sullivan
        lookup = identifier

    ### Retrieve HTML.

    url = "http://cs1110.cs.virginia.edu/files/uva2016/" + lookup
    try:
        conn = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        return None, 0, 0
    else:
        data = conn.read().decode("utf-8")

        ### Parse HTML.
        titleE = re.compile(r"\<span.*id=\"personjob\"\>([^<]+)\<\/span\>")
        compensationE = re.compile(r"<h2.*id=\"paytotal\">\$([\d,]+)<\/h2>")
        rankE = re.compile(r"<tr><td>University of Virginia rank<\/td><td>([\d,]+) of 7,927<\/td><\/tr>")

        result = titleE.findall(data)
        title = html.unescape(result[0])

        result = compensationE.findall(data)
        compensation = float(result[0].replace(",", ""))

        if (rankE.findall(data)):
            rank = int(rankE.findall(data)[0].replace(",", ""))
        else:
            rank = 0

        return title, compensation, rank

print(report(input()))
