#### INSTRUCTION FOR CREATING VIEWS ####
#Please follow steps below to reproduce database environment required to run properly this application

1)
#Create view for paths and views
#This sql is extracting part of article name from its path
create view articles_paths as select split_part(path, '/', 3), count(path) as views from log where status = '200 OK' and path != '/' group by path order by views desc limit 3;

2)
#Create view with splited names and views
#This sql is replacing "-" with spaces so we could match it with article name
create view top_articles as select replace(split_part, '-', ' ') as short_name, views from articles_paths;