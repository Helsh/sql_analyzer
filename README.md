# INSTRUCTION FOR CREATING VIEWS
# Please follow steps below to reproduce database environment required to run properly this application

# 1)
# Authors + titles
create view authors_titles_slugs as select authors.name, articles.title, articles.slug from authors join articles on authors.id = articles.author;

# 2)
# Extract name from path so it could be matched with articles slug
create view extracted_paths as select split_part(path, '/', 3) as extracted_name, count(path) as views from log where status = '200 OK' and path != '/' group by path order by views desc;

# 3)
# Extract failed view requests
create view failures_summary as select date(time), count(status) from log where status != '200 OK' group by time;

# 4)
# Count fails view requests
create view counted_failed_requests as select date, count(count) from failures_summary group by date;

# 5)
# All counted view requests
create view all_requests as select date(log.time) as datetime, count(log.status) as counted from log group by datetime;

# 6)
# Percentage of failed requests
 create view failure_percentage as select date, (100.0*(sum(counted_failed_requests.count)/sum(all_requests.counted))) as percentage from counted_failed_requests join all_requests on counted_failed_requests.date = all_requests.datetime group by date order by percentage;

 # HOW TO RUN
 Run main.py file (e.g. python3 main.py).


