import re

def ber(string):

    string = '<p>' + string + '</p>'
    string = string.replace('\n', '</p><p>')
    string = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", string)

    string = re.sub(r"\*(.*?)\*", r"<em>\1</em>", string)
    supers = re.findall(r"(?<=\^)(.*?)($|[ ])", string)
    if supers:
        replacers = [x[0] for x in supers]
        for r in replacers:
            replaced = r.replace("^", "<sup>")
            replaced += "</sup>"*(len(replacers)-1)
            string = string.replace(r, replaced)
    string = re.sub(r"~~(.*?)~~", r"<del>\1</del>", string)
    string = re.sub(r"\[(.*?)\]\((.*?)\)", r"<a href='\2'>\1</a>", string)
    string = re.sub(r"`(.*?)`", r"<code>\1</code>", string)
    string = re.sub(r"(?m)    (.*)(?=($|[\n]))", r"<pre><code>\1</code></pre>", string)

    return string
