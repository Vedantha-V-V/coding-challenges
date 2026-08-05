STYLE = {
    "body":"font-family:monospace; color:#333; line-height:1.6; max-width:700px; margin:0 auto; padding:24px;",
    "h1":"color:#1e293b; font-size:30px; font-weight:700; border-bottom:1px solid #e2e8f0; padding-bottom:12px; margin-bottom:16px;",
    "h2":"color:#1e293b; font-size:28px; font-weight:700; margin-top:32px; margin-bottom:12px;",
    "h3":"color:#1e293b; font-size:24px; font-weight:700; margin-top:32px; margin-bottom:12px;",
    "h4":"color:#1e293b; font-size:22px; font-weight:700; margin-top:32px; margin-bottom:12px;",
    "h5":"color:#1e293b; font-size:20px; font-weight:700; margin-top:32px; margin-bottom:12px;",
    "h6":"color:#1e293b; font-size:18px; font-weight:700; margin-top:32px; margin-bottom:12px;",
    "p":"color:#475569; font-size:15px;",
    "ul":"padding-left:20px;",
    "li":"color:#475569; margin-bottom:6px;",
    "pre":"background:#2d2d2d; color:#e2e8f0; border-radius:8px; padding:16px 20px; overflow-x:auto; margin:16px 0;",
    "backquote":"border-left: 3px solid #cbd5e1; margin: 0; padding-left:8px; color: #64748b; font-size: 15px;"
}

def parse_heading(header):
    if header.startswith('# '):
        return f'<h1 style="{STYLE['h1']}">{parse_sentence(header[2:])}</h1>'
    elif header.startswith("## "):
        return f'<h2 style="{STYLE['h2']}">{parse_sentence(header[3:])}</h1>'
    elif header.startswith("### "):
        return f'<h3 style="{STYLE['h3']}">{parse_sentence(header[4:])}</h3>'


def parse_sentence(line):
    words = line.split(" ")
    for i in range(len(words)):
        word = words[i]
        if word.startswith("**") and word.endswith("**"):
            word = word.replace("**","")
            words[i] = f"<b>{word}</b>" 
        elif word.startswith("*") and word.endswith("*"):
            word = word.replace("*","")
            words[i] = f"<i>{word}</i>"
        elif word.startswith("["):
            tag,url = tuple(word.split("("))
            tag = tag.replace("[",'<link href="URL">')
            tag = tag.replace("]","</link>")
            url = url.replace(")","")
            tag = tag.replace("URL",url)
            words[i] = tag
    ln = " ".join(words)
    return ln     

def parse(lines):
    i = 0
    htmlbody = []
    while i < len(lines):
        line = lines[i]
        if line.startswith("#"):
            htmlbody.append(parse_heading(line))
        elif line.startswith("- "):
            htmlbody.append(f'<ul style={STYLE["ul"]}>')
            while i < len(lines) and lines[i].startswith("- "):
                ln = lines[i].replace("- ","")
                htmlbody.append(f"</li>{parse_sentence(ln)}</li><br>")
                i+=1
            htmlbody.append("</ul>")
            continue            
        elif line.startswith("```"):
            i+=1
            code = [f'<pre style="{STYLE["pre"]}">']
            while i< len(lines) and not lines[i].startswith("```"):
                code.append(lines[i])
                i+=1
            code.append("</pre>")
            htmlbody.append("\n".join(code))
        elif line.startswith("> "):
            htmlbody.append(f'<backquote style="{STYLE["backquote"]}">{parse_sentence(line[2:])}</backquote>')
        elif line == "\n" or len(line)==0:
            i+=1
            continue
        else:
            htmlbody.append(f"<p>{parse_sentence(line)}</p>")
        i+=1
    return "\n".join(htmlbody)

def main():
    print("Markdown Parser")

if __name__ == "__main__":
    main()