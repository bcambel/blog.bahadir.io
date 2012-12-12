import markdown2
import os

base = "".join(open("base.html").readlines())
tail = "".join(open("tail.html").readlines())

for dirname,dirnames,filenames in os.walk('content/'):
	for file in filenames:
		output_file = "%s.html" % file[:-3]
		file_path = "content/%s" % file
		content = "".join(open(file_path).readlines())
		print "{0}{1}{0}".format((20*"-"),output_file)
		gen_content = markdown2.markdown(content)
		with open('posts/%s' % output_file, "w+") as post:
			post.write(base)
			post.write(gen_content.encode('ascii','xmlcharrefreplace'))
			post.write(tail)
			post.flush()

		print file

		print 30 * "="
