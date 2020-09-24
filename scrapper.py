from indeed import extract_indeedpages,extract_indeed_jobs
from save import save_to_file

max_indeed_pages = extract_indeedpages()
indeed_jobs = extract_indeed_jobs(max_indeed_pages)

save_to_file(indeed_jobs)




