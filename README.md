# Abhikalpan-Hackathon

Setting up this project on your local machine is really easy.

## Installation instructions:

* Download and install python 3.6 and git
* Clone using `$ git clone https://github.com/Sanji515/Abhikalpan-Hackathon.git && cd Abhikalpan-Hackathon`

### Run

* Install virtualenv
    - on Ubuntu: `$ sudo apt install python-virtualenv`
    - on Windows: `$ pip install virtualenv`
    
* Create a virtual environment
    - on Ubuntu: `$ virtualenv venv -p python3.6`
    - on Windows: `$ virtualenv venv`
    
* Activate the environment:
    - on Ubuntu: `$ source venv/bin/activate`
    - on Windows: `$ ./venv/Scripts/activate`
    
* Install the requirements: `$ pip install -r requirements.txt`
* Make migrations `$ python manage.py makemigrations`
* Migrate the changes to the database `$ python manage.py migrate`
* Run the server `$ python manage.py runserver`

That's it. Open web browser and hit the url http://127.0.0.1:8000

## Steps for training model:

### 1. Prerequisites:
  - IBM Cloud account: If you do not have an IBM Cloud account, you can create an account [Click Here](https://cloud.ibm.com/) .
  - Watson Knowledge Studio account: User must have a WKS account. If you do not have an account, you can create a free account [click Here](https://www.ibm.com/account/us-en/signup/register.html?a=IBMWatsonKnowledgeStudio). Make a note of the login URL since it is unique to every login id
  - Basic knowledge of building models in WKS: The user must possess basic knowledge of building model in WKS in order to build a custom model. Check getting started documentation [Click Here](https://cloud.ibm.com/docs/services/knowledge-studio/tutorials-create-project.html#wks_tutintro)
  
### 2. Create NLU service instance:
  - Step1: [Click here](https://cloud.ibm.com/catalog/services/natural-language-understanding) to create NLU service and enter the service name
  ![](Watson_knowlege_Studio/Screenshots/Screenshot%20from%202019-03-02%2023-05-57.png)
  - Step2: Once you click on Create NLU service instance should get created. 
  ![](Watson_knowlege_Studio/Screenshots/Screenshot%20from%202019-03-02%2023-07-55.png)
  
### 3. Training Your Model:
  - Click Create Workspace in Watson Knowledge Studio
  ![](Watson_knowlege_Studio/Screenshots/Screenshot%20from%202019-03-02%2022-28-26.png)
  - In the Create Workspace pop up window, enter the name of the new project. Click Create
  ![](Watson_knowlege_Studio/Screenshots/Screenshot%20from%202019-03-02%2023-02-44.png)
  - Click on the workspace you created and on Entity Type Click on Upload and add json file Abhikalpan-Hackathon/Watson_knowlege_Studio/Entities/types-de2a5c20-3cc6-11e9-9a38-235c4e7dcc32.json
  ![](Watson_knowlege_Studio/Screenshots/Screenshot%20from%202019-03-02%2023-02-54.png)
  - On Documents Click Upload and select Abhikalpan-Hackathon/Watson_knowlege_Studio/dataset/corpus-de2a5c20-3cc6-11e9-9a38-235c4e7dcc32.zip
  ![](Watson_knowlege_Studio/Screenshots/Screenshot%20from%202019-03-02%2023-03-08.png)
  - Click on Annotation Task under Machine Learning model and click on task available
  ![](Watson_knowlege_Studio/Screenshots/Screenshot%20from%202019-03-02%2023-04-29.png)
  - Click on Task which is in Not Complete and make each task Complete
  ![](Watson_knowlege_Studio/Screenshots/Screenshot%20from%202019-03-02%2023-04-34.png)
  - Click on Versions under Machine learning model and create new version and deploy it to Natural Language Understanding services
  ![](Watson_knowlege_Studio/Screenshots/Screenshot%20from%202019-03-02%2023-05-08.png)
  - Click on Performance under Machine learning model and click on Train and Evaluate button which will train the model against the annotations
  ![](Watson_knowlege_Studio/Screenshots/Screenshot%20from%202019-03-02%2023-04-47.png)

### 4. Analyze Results:
  - Run the Abhikalpan-Hackathon/try.py and enter any piece of secret text and the function will analyze the text
![](Watson_knowlege_Studio/Screenshots/Screenshot%20from%202019-03-02%2023-07-11.png)
