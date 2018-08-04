import csv
import os

recipient = []
application = []
recipient_title = []
job_position = []
company = []
skills = []
why = []

with open('cover_letter_gen.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        recipient.append(row['Recipient'])
        recipient_title.append(row['Recipient_Title'])
        job_position.append(row['Position'])
        company.append(row['Company'])
        skills.append(row['Skills'])
        why.append(row['Why'])
        application.append(row['Where_did_you_apply'])



skill_string = skills[0]
for i in range(len(skills)):
    if i == 0:
        continue
    if i == len(skills) - 1:
        skill_string = skill_string + ", and " + skills[i]
    else:
        skill_string = skill_string + ", " + skills[i]

message = open('message.txt', 'w+')
dear = "Hi {},".format(recipient[0])
line_one = "I recently applied for the {} position through {}.  I notice that you are a {} at {}. ".format(job_position[0],application[0],recipient_title[0],company[0])
intro = "While I am not sure if you are the right person to contact, here are three reasons why I can provide value to {} and your users:".format(company[0])
point_one = "1. {} are among my strongest technologies and I am confident in my ability to implement them as a software engineer at {} and hit the ground running.".format(skill_string,company[0])
point_two = "2. Having great teamwork, I worked closely with partners in completing daily projects during my time at App Academy, a 1000 hour, 12 week web development course."
point_three = "3.  I pride myself on my work ethic, ability and will."
why_text = "{} interests me because {}.".format(company[0],why[0])
outro = "I know you are a busy person, but I would love the opportunity to have a 10 minute chat on Skype/hangout about the role or other roles the team is recruiting for."
message.write(dear + '\n\n')
message.write(line_one + intro + '\n\n')
message.write(point_one + '\n')
message.write(point_two + '\n')
message.write(point_three + '\n\n')
message.write(why_text + '\n\n')
message.write(outro + '\n')
message.write("Thank you for your time and consideration." + '\n\n')
message.write("Sincerely," + '\n')
message.write("Terrence Tang")
message.close()

# check
# update
os.startfile("message.txt")
