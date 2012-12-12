import markdown2
import os
from jinja2 import *



cur_dir = os.path.dirname(os.path.realpath(__file__))
env = Environment(loader=FileSystemLoader(os.path.join(cur_dir,"templates")))



class Article:
	title = ''
	slug = ''
	def __init__(self,title,slug):
		self.title=title
		self.slug = slug

def render_plain():
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

def render_jinja():
	articles = []
	article_jinja_tmpl = env.get_template("article_detail.html")

	for dirname,dirnames,filenames in os.walk('content/'):
		for file in filenames:
			title = slug = file[:-3]
			title = title.replace("-"," ")
			articles.append(Article(title=title,slug=slug))

		for article in articles:
			article_path = "content/%s.md" % article.slug
			content = "".join(open(article_path).readlines())
			gen_content = markdown2.markdown(content)
			content = gen_content.encode('ascii','xmlcharrefreplace')

			with open('posts/%s.html'%article.slug,"w+") as article:
				article.write( article_jinja_tmpl.render(content=content,articles=articles) )
				article.flush()

	index_jinja_tmpl = env.get_template('index.html')
	index = 'html/index.html'

	with open(index,"w+") as index:
		index.write(index_jinja_tmpl.render(articles=articles))
		index.flush()

if __name__ == "__main__":
	render_jinja()