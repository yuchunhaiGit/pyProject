# __author__ = 'yuchunhai'
# 虽然本书全部用 BeautifulSoup（也是 Python 里最受欢迎的 HTML 解析库之一），但它并不
# 是你唯一的选择。如果 BeautifulSoup 不能满足你的需求，你可以看看其他的库。
# • lxml
# 这个库（http://lxml.de/）可以用来解析 HTML 和 XML 文档，以非常底层的实现而闻名
# 于世，大部分源代码是用 C 语言写的。虽然学习它需要花一些时间（其实学习曲线越
# 陡峭，表明你可以越快地学会它），但它在处理绝大多数 HTML 文档时速度都非常快。
# • HTML parser
# 这是 Python 自带的解析库（https://docs.python.org/3/library/html.parser.html）。因为它不
# 用安装（只要装了 Python 就有），所以可以很方便地使用。