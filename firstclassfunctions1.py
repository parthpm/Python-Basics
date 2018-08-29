# functions are first-class in a certain programming language means that they can be passed around and manipulated similarly
# to how you would pass around and manipulate other kinds of objects (like integers or strings). You can assign a function to
#  a variable, pass it as an argument to another function, etc. The distinction is not that individual functions can be
# first class or not,
#but that entire languages may treat functions as first-class objects, or may not.

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1') #i.e print_h1=wrap_text
print(print_h1.__name__)
print(print_h1)

print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')