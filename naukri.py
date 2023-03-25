from selenium import webdriver 
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Change this to your browser (Firefox) and the location of your gecko driver
driver = webdriver.Firefox(executable_path="path/to/geckodriver")

# Search for a job on naukri and paste its url here
url = ""
driver.get(url)


#storing all the values here, so that we can output it into a CSV

job_names = []
job_skills = []
work_ex = []
company = []
package = []
location = []
days_posted = []
job_des = []


k = 1

# Number of pages you want to scrape
n = 10

while k<=n:
	time.sleep(2)
	for x in range(1, 21):
		# This will add append all the values to the list we created above

		job_title = driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div/section[2]/div[2]/article["+str(x)+"]/div[1]/div[1]/a").text

		job_names.append(job_title)	

		wex = driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div/section[2]/div[2]/article["+str(x)+"]/div[1]/ul/li[1]/span[1]").text 
		work_ex.append(wex)

		skill = driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div/section[2]/div[2]/article["+str(x)+"]/ul").text
		job_skills.append(skill)

		comp = driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div/section[2]/div[2]/article["+str(x)+"]/div[1]/div[1]/div/a[1]").text
		company.append(comp)

		salary = driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div/section[2]/div[2]/article["+str(x)+"]/div[1]/ul/li[2]/span[1]").text
		package.append(salary)

		city = driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div/section[2]/div[2]/article["+str(x)+"]/div[1]/ul/li[3]/span").text
		location.append(city)

		days_ago  = driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div/section[2]/div[2]/article["+str(x)+"]/div[3]/div[1]/div/span").text
		days_posted.append(days_ago)

		des = driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div/section[2]/div[2]/article["+str(x)+"]/div[2]").text
		job_des.append(des)

	#Goto the next page
	driver.get("https://www.naukri.com/data-analyst-jobs-in-india-"+str(k+1))
	k+=1

# Creating a DataFrame
df = pd.DataFrame({'job_titles': job_names, 'job_skills': job_skills, 'work_ex': work_ex, "job_des": job_des, "location": location, "salary": package, "company": company, "days_posted": days_posted})

# Export the DataFrame to a CSV file
df.to_csv('output.csv', index=False)

#Quit
driver.quit()

