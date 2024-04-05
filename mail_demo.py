import os
import smtplib 
from email.message import EmailMessage
import imghdr
# EMAIL_ADDRESS=os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD=os.environ.get('EMAIL_PASS')
EMAIL_ADDRESS="gjkkunwar07@gmail.com"
EMAIL_PASSWORD="slgr nstm wrwv rsxb"
# print(EMAIL_ADDRESS, EMAIL_PASSWORD)


contacts=['pudasainirohan0@gmail.com','gjkkunwar07@gmail.com']

msg=EmailMessage()
# msg['Subject']='Grab dinner this weekend ?'
msg['Subject']='Check out Bronx as a puppy ?'
msg['From']=EMAIL_ADDRESS
# msg['To']=contacts     ==>another way in the python documentation look at here 
msg['To']=','.join(contacts)        #in the python documentation this one is here right     join chai 2 or more then contact ma data pathaune vayepaxi chai use garne hai ta
msg.set_content('How about dinner at 6p this saturday ?')

msg.add_alternative(
    '''\
        <!DOCTYPE html>
        <html>
        <body>
        <h1 style="color:SlateGray;">This is an HTML Email </h1>
        </body>
        </html>
        
        
        </html>
    
    
    ''',subtype='html'
)

# multiple email send garna :


# multiple images
files=['g1.jpeg','g2.jpeg','ganesh.jpeg']

# Adding attachements
for file in files:
    with open(file,'rb') as f:
        file_data=f.read()
        file_type=imghdr.what(f.name)     # image ko context ma matra yo garinxa aru file "resume.pdf" haru ma chai yesko use garedaina hai ta
        print(file_type)
        file_name=f.name
         
    msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)    #main_type image bahek aru ma image vanera lekhinna for example((((main_type='application ,,,subtype='octet-stream' lekhinxa hai ta ))))


with smtplib.SMTP_SSL('smtp.gmail.com',465 ) as smtp:          
# with smtplib.SMTP('smtp.gmail.com',587 ) as smtp:        #smtp changes garera mathi ko chalaune ho ssl      
# with smtplib.SMTP('localhost',1025) as smtp:             #local machine ma chai email haru send garne check garna lai ho hai ta   <--> python3 -m smtpd -c DebuggingServer -n localhost:1025  <---> yo termunal ma run garna lai ho hai ta 
    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo() 
    
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    
    smtp.send_message(msg)
    
    # subject='Grab dinner this weekend ?'
    # body='How about dinner at 6pm this saturday !'
    
    # msg=f'Subject:{subject}\n\n{body}'
    
    # smtp.sendmail(EMAIL_ADDRESS,'gjkkunwar07@gmail.com',msg)
    
    
    
    
    
     
    
