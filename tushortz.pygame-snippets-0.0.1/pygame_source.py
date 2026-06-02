# Import necessary packages
import re, os, shutil
from urllib.request import urlopen


_url = "https://docs.python.org/3.5/py-modindex.html"
_link = str(urlopen(_url).read())

modules = re.findall(r'<a href=".*?"><code class="xref">([\w\s\d\_\-\\.]+)', _link)
lnbegin = "{\n"; lnend = "}"

dirname = "snippets"
filename = "pygame"
extension = "json"

# Recreate on every program run
if os.path.exists(dirname): shutil.rmtree(dirname)
if not os.path.exists(dirname): os.makedirs(dirname)

def replaced(text):
	TEXT = (text.replace("&gt;", ">").replace("&lt;", "<").replace("&#8217;", "'").replace("\\n", " ")
		.replace("\\t", "").replace("\\r", "").replace("&nbsp;", " ").replace("\'", "'")
		.replace("&quot;", "\"").replace("\\;", "").replace("\\'", "'").replace("&lt;", "<")
		.replace("&gt;", ">").replace("&trade;", "(TM)").replace("&#8212;", "--").replace("&#8220;", "\"")
		.replace("&#8221;", "\"").replace("\n", " ").replace("\t", "").replace("\r", "").replace("&#8217;", "'")
		.replace("\\", "").replace("\"", "\\\"")
	)
	return TEXT

def change(text):
	head = text.split("(")[0]
	body = text.split("(")[1:]
	body = "".join(body).split(")")[0]

	body = body.split(",")

	result = ""
	for x in body:
		ind = body.index(x) + 1
		if len(body) > 1:
			if body.index(x) != len(body) - 1:
				x = "${%s:%s}, " % (ind, replaced(x.strip()))
			else:
				x = "${%s:%s}" % (ind, replaced(x.strip()))
		else:
			x = ""

		result += x
	result = head + "(" + result + ")"
	return (result)

def make(link):
	alls = []
	text = urlopen(link).read().decode("utf-8")
	A = re.findall(r'<div class="line"><span class="signature">(.*?) -&gt; .*?</div>', text)
	pattern = re.compile(r'\\x[\w\d]\d|<.*?>')
	A = sorted(set(A))

	for x in A:
		x = pattern.sub("", x)
		if x.endswith(")"):
			x = change(x)

		alls.append(x)
	return alls

url = "http://www.pygame.org/docs/ref/%s.html"
head = ["BufferProxy", "cdrom", "Color", "cursors", "display", "draw", "event", "examples", "font", "freetype", "gfxdraw", "image", "joystick", "key", "locals", "mixer", "music", "mouse", "Overlay", "PixelArray", "Rect", "scrap", "sndarray", "sprite", "Surface", "surfarray", "tests", "time", "transform"]

ln1 = "{\n\t\"scope\": \"source.python\",\n\t\"completions\":\n\t[\n"
ln2 = "\t\t{\"trigger\": \"%s\\tpygame(%s) \", \"contents\": \"pygame.%s.%s\"},\n"
ln3 = "\t]\n}"

# Substitution template for completion
template ="""	"'%s' from the python's '%s' module": {
		"description": "'%s' from the pygame's '%s' module",
		"prefix": "%s",
		"body": ["%s"]},
"""

modules = ["BufferProxy", "cdrom", "Color", "cursors", "display", "draw", "event", "examples", "font", "freetype", "gfxdraw", "image", "joystick", "key", "locals", "mixer", "music", "mouse", "Overlay", "PixelArray", "Rect", "scrap", "sndarray", "sprite", "Surface", "surfarray", "tests", "time", "transform"]

with open("%s/%s.%s" % (dirname, filename, extension), "w") as obj:
	obj.write(lnbegin)
	link = "http://www.pygame.org/docs/ref/%s.html"
	for module in modules:
		try:
			obj.write("// %s\n" % module)
			for content in make(link % module.lower()):
				methods = content.split("(")[0]
				completion = "pygame.%s.%s" % (module, content)
				obj.write(template % (methods, module, methods, module, methods, completion))
		except: pass
		print("%s completed" % module)
	obj.write(lnend)
print("Operation finished")