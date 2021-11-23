# Deploy-Models
✔ Deploy the trained and validated models after creating Flask file and the template folder having index.html files
# Deploy-Models
🏡 House Price Prediction deployed url : https://housepricebrokers.herokuapp.com/
✔ Create <Project Name> folder in Virtual Studio Code IDE
✔Inside that folder create 'train.py' file
✔Create new environment eg deployment 
✔Navigate to Deployment environment using 'conda activate deployment' in vs code terminal. cd project folder. 
✔Inside the file -First Train the model and save the high accuracy model as a pickle file or Joblib file
✔Run by specifying 'python train.py'  
✔Once the above code is run then we can notice that the pickle file getting generated inside the same folder where the .py file is present
✔Create Load_pkl.py file 
✔Inside Load_pkl.py file--Import all the necessary Libraries and Load the saved file and do predictions by giving new test data
✔Create Flask.py file(Flask is a framework that is used to create web page using Python (This is nothing but app.py)
✔Create templates folder under the same project folder that you are working (The name 'templates' is fixed- do not change the 'name of the folder' for any project)
✔Inside the templates folder Create 'index.html' file 
✔Now run the Flask file.
✔We can notice 'http:.....' getting created in the debug area.
✔Click on that link...Our web page gets displayed.
  
✔We need to create 'Form.html'file inside templates folder.
✔When we run the flask file,it generates eg.http://127.0.0.1:5000**/** ,our '/' on the web page looks for '/' function in the flask file--which returns render_template(form.html) file and whatever the code action is in the form.html file that gets displayed on web browser,so that the user can input the datas and click on submit button
✔Once Submit button is pressed on web page,then it will look for the 'action' that is specified in the Form.html file eg.action={{url_for('predict')}}
✔The web page(Client) looks for the '/predict' function in the Flask file.    
✔Once the submit is done,the connection goes to the Backend Flask Server where the predict function would be present and the inputs would be given as an array to the model for prediction.
✔The communication between Web page(Client) and the Flask server(Server) is made by HTTP Protocol.
✔HTTP works as a request-response protocol between client and the server
✔Like we can perform CRUD( C-Create, R-Retrieve, U-Update, D-Delete) Operations on the Database, here in HTTP protocol we have GET(Retrieve), POST(Create), PUT(Update), Delete(Delete) operations.
✔  
  
✔Create a 'Procfile' ('P' should be capital) under the project folder having 'web: gunicorn app:app'typed inside it-----This is required for deploying in Heroku.
✔web:(Heroku knows that it is a web application) gunicorn(It is the web server at the backend--for flask file we need to put gunicorn only), :app(name given to Flask file(app=Flask(__name__) in our case)--as we have selected python as our language while creating account with Heroku,it will look for .py file only.   
  
✔Create requirements file using 'pip freeze > requirements.txt'--notice this file getting created under the same location 
✔If someone wants to run our code then they need to install the required packages using ' pip install -r requirements.txt' under deployment environment  
  
✔*How to push the files present in the local folder to github
✔Open the folder in local system eg.c:/Deployment
✔Right click and select ' Git Bash Here'
✔type 
✔ls -al in the bash terminal(lists all the files present in that folder)
✔git init (Initializes the local project folder and creates .git folder in that project folder eg.c:/Deployment
✔ls -al (Now we can see the .git folder)
✔git remote add origin https://github.com/nrsumithra/House_Price.git (specify where do we want to add the project folder)
✔git status (displays all the files present inside the local project folder(red color if the files are not included, to be committed action)
✔git add 'HOUSE PRICE/' (adds the folder to the -to be commited action)
✔git status (Now all the files turn green-meaning that they are added successfully- to be commited action)  
✔git commit -m "Deploy-Models" (This name gets displayed in description of the files(beside filename) in Github)  
✔git push origin master (Now the files can be viewed in the github under House_Price repository)  
