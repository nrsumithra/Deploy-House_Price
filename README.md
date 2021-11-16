# Deploy-Models
✔ Deploy the trained and validated models after creating Flask file and the template folder having index.html files
# Deploy-Models
✔ Create <Project Name> folder in Virtual Studio Code IDE
✔Inside that folder create 'train.py' file
✔Inside the file -First Train the model and save the high accuracy model as a pickle file or Joblib file
✔Once the above code is run then we can notice that the pickle file getting generated inside the same folder where the .py file is present
✔Create Load_pkl.py file 
✔Inside Load_pkl.py file--Import all the necessary Libraries and Load the saved file and do predictions by giving new test data
✔Create Flask.py file(Flask is a framework that is used to create web page using Python
✔Create templates folder under the same project folder that you are working (The name 'templates' is fixed- do not change the 'name of the folder' for any project)
✔Inside the templates folder Create 'index.html' file 
✔Now run the Flask file.
✔We can notice 'http:.....' getting created in the debug area.
✔Click on that link...Our web page gets displayed.

  
  
  
  
✔*How to push the files present in the local folder to github
✔Open the folder in local system eg.c:/Deployment
✔Right click and select ' Git Bash Here'
✔type 
✔ls -al in the bash terminal(lists all the files present in that folder)
✔git init (Initializes the local project folder and creates .git folder in that project folder eg.c:/Deployment
✔ls -al (Now we can see the .git folder)
✔git remote add origin https://github.com/nrsumithra/Deploy-Models.git (specify where do we want to add the project folder)
✔git status (displays all the files present inside the local project folder(red color if the files are not included, to be committed action)
✔git add 'HOUSE PRICE/' (adds the folder to the -to be commited action)
✔git status (Now all the files turn green-meaning that they are added successfully- to be commited action)  
✔git commit -m "Deploy-Models" (The respository in which the files will be added in Github)  
✔git push origin master (Now the files can be viewed in the github under Deploy-Models repository)  
