from jinja2 import Template

t = Template("Hello {{ name }}!")
print(t.render(name="World"))

t = Template("Numbers: {% for n in range(1, 10) %}{{n}} " "{% endfor %}")
print(t.render())