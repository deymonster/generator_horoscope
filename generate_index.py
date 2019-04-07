# coding: utf-8
from horoscope import generate_prophecies
from datetime import datetime as dt

def generate_page(head, body):
	# page = "<html>" + head + body + "</html>"  old version
	page = f"<html>{head}{body}</html>"
	return page

def generate_head(title):
	# head = "<meta charset='utf-8'>" + "<title>" + title + "</title>" old version
	# return "<head>" + head + "</head>" old version
	head = f"""<head>
	<meta charset='utf-8'>
	<title>{title}</title>
	</head>
	"""
	return head

def generate_body_index(header, paragraphs):
	# body = "<h1>" + header + "</h1>"  old version
	# i = 0
	# while i < len(paragraphs):
		# body = body + "<p>" + paragraphs[i] + "</p>"
		# i = i + 1
	# return "<body>" + body + "</body>"
	body = f"<h1>{header}</h1>"
	for p in paragraphs:
		body = body + f"<p>{p}</p>"
	return f"""<body>
	{body}
	<hr/>
	<a href="about.html">
	О реализации
	</a>
	</body>"""

def generate_body_about(header, times, advices, promises):
	about_t = ""
	about_a = ""
	about_p = ""
	body = f"""<h1>{header}</h1>
				<img src="znak.png"/><p>Параметры генерации: перечень всех использованных списков для генерации</p>"""
	for t in times:
	  	about_t = about_t + f"<li>{t}</li>"  # генерация просто с тегами <li>
	for t in advices:
		about_a = about_a + f"<li>{t}</li>"
	for t in promises:
		about_p = about_p + f"<li>{t}</li>"

	return f"""<body>
	{body}
		<ol>   
			<li>Времена дня
				<ul>{about_t}</ul>   
			</li>
			<li>Глаголы
				<ul>{about_a}</ul>
			</li>
			<li>Дополнения
				<ul>{about_p}</ul>
			</li>
		</ol>
	    <hr/>
			<a href="index.html">
			Назад к гороскопу
			</a>
	</body>"""

def save_page_index(title, header, paragraphs, output="index.html"):
	fp = open(output, "w", encoding='utf-8')
	today = dt.now().date()
	page = generate_page(
		head=generate_head(title),
		body=generate_body_index(header=header, paragraphs=paragraphs)
	)
	print(page, file=fp)
	fp.close()

def save_page_about(title, header, times, advices, promises, output="about.html"):
	fp = open(output, "w", encoding='utf-8')
	today = dt.now().date()
	page = generate_page(
		head=generate_head(title),
		body=generate_body_about(header=header, times=times, advices=advices, promises=promises)
	)
	print(page, file=fp)
	fp.close()


prophecies,times,advices,promises=generate_prophecies()

today = dt.now().date()
save_page_index(
    title="Гороскоп на сегодня",
    header="Что день " + str(today) + " готовит",
    paragraphs=prophecies,
)
save_page_about(
	title="О реализации",
	header="О чем все это",
	times=times,
	advices=advices,
	promises=promises

)