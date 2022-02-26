const supportsHyperlinks = require('supports-hyperlinks');

if (supportsHyperlinks.stdout) {
	print("true")
}

if (supportsHyperlinks.stderr) {
	print("false)
}
