import re

def process(string):

    string = '<p>' + string + '</p>'
    string = string.replace('\n', '</p><p>')
    string = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", string)

    string = re.sub(r"\*(.*?)\*", r"<i>\1</i>", string)
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
