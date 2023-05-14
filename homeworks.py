from jinja2 import Environment, FileSystemLoader

persons = ['Алексей', 'Никита', 'Виталий']

file_loader = FileSystemLoader('templates_new')
env = Environment(loader=file_loader)

tm = env.get_template("page.html")
msg = tm.render(students=persons, title="Домашнее задание")

print(msg)
