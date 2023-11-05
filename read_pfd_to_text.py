from PyPDF2 import PdfReader 
  
# creating a pdf reader object 
reader = PdfReader('resume_ex.pdf') 

def check_keyword(text, keyword):
  for word in text.split():
    if word == keyword:
      return True
  return False
  
# printing number of pages in pdf file 
# print(len(reader.pages)) 
  
# getting a specific page from the pdf file 
page = reader.pages[0] 
  
# extracting text from page 
text = page.extract_text() 
# print(text)

# the keywords to look for in our text
keywords = ["skills", "education", "summary", 'objective', 'certificates  ']
end_keyword = "experience"
result = {}
extracting = False
current_keyword = None

lines = text.split("\n")

for line in lines:
    for keyword in keywords:
        if keyword in line:
            extracting = True
            current_keyword = keyword
    if extracting:
        if end_keyword in line:
            extracting = False
            current_keyword = None
        else:
            if current_keyword not in result:
                result[current_keyword] = []
            result[current_keyword].append(line)

# Convert the results to a dictionary where keys are the keywords and values are the extracted text.
result_dict = {keyword: "\n".join(lines) for keyword, lines in result.items()}

for keyword, extracted_text in result_dict.items(): 
   print(keyword)


# getting data from database for a certain role
import requests

url = "http://localhost:3000/jobs"
response = requests.get(url)

if response.status_code == 200:
  data = response.json() 
else:
  print("Error:", response.status_code)

skillsFromRecruters = data[0]['requirements']['skills']
eduFromRecruters = data[0]['requirements']['education']
print(skillsFromRecruters)
print(eduFromRecruters)

skillScore = 0
educationScore = 0

for keyword, extracted_text in result_dict.items(): 
    print(keyword)
    if 'skill' in keyword:
        for el in skillsFromRecruters: 
            if check_keyword(extracted_text, el):
               skillScore = skillScore + 1
    elif 'summar' in keyword:
        for el in skillsFromRecruters: 
            if check_keyword(extracted_text, el):
               skillScore = skillScore + 1
    elif 'education' in keyword:
       for el in eduFromRecruters:
          if check_keyword(extracted_text, el):
             educationScore = educationScore + 1
