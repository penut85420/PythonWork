import wikipediaapi as wp
from mafan import tradify

def get_summary(page_name):
	zhwp = wp.Wikipedia('zh')
	page = zhwp.page(page_name)

	return tradify(page.summary)

print(get_summary('數學'))
