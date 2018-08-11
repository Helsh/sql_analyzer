# INSTRUCTION FOR CREATING VIEWS
# Please follow steps below to reproduce database environment required to run properly this application

1)
# Authors + titles
create view authors_titles_slugs as select authors.name, articles.title, articles.slug from authors join articles on authors.id = articles.author;

2)
# Extract name from path so it could be matched with articles slug
create view extracted_paths as select split_part(path, '/', 3) as extracted_name, count(path) as views from log where status = '200 OK' and path != '/' group by path order by views desc;