class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Name cannot be deleted")

    def articles(self):
        return [article for article in Article.all_articles if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        Article.all_articles.append(article)
        return article

    def topic_areas(self):
        magazines = self.magazines()
        if not magazines:
            return None
        return list(set([magazine.category for magazine in magazines]))


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return [article for article in Article.all_articles if article.magazine == self]

    def contributors(self):
        authors = set()
        for article in self.articles():
            authors.add(article.author)
        return list(authors)

    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]

    def contributing_authors(self):
        authors = self.contributors()
        if not authors:
            return None
        return [author for author in authors if len([article for article in author.articles() if article.magazine == self]) > 2]

    @classmethod
    def top_publisher(cls):
        if not cls.all_magazines:
            return None
        return max(cls.all_magazines, key=lambda magazine: len(magazine.articles()))


class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all_articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = value

    @title.deleter
    def title(self):
        raise AttributeError("Title cannot be deleted")