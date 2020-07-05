# Online compiler for C and Python

# Setup
	1. git clone https://github.com/Pirate2606/compiler.git
	2. Create a virtual environment:
		1. sudo apt install virtualenv
		2. virtualenv -p python3 <name without brackets>
		3. source <name without brackets>/bin/activate
		
	3. Get OAuth credentials from Google:
		1. Visit the Google Developers Console at https://console.developers.google.com and create a new project. 
		2. In the "APIs & Services" section, click on "Credentials", and then click the "Create Credentials" button. Select "OAuth client ID" from the 
		   dropdown menu. 
		3. Click "Configure Consent screen" and select external. Fill the "Application Name" in the form and click "save".
		4. Repeat step 2. Select"Web Application" in the Application type field and fill the name of the app. 
		5. Once you’ve done that, you’ll see two new fields: "Authorized JavaScript origins" and "Authorized redirect URIs". Set the authorized redirect URI
		   to http://127.0.0.1:5000/login/google/authorized, and click "Create". Google will give you a client ID and client secret.
		6. Paste the client ID and client secret in the compiler/config.py file inside inverted commas.
	
	3. cd compiler/
	4. pip install -r requirements.txt
	5. flask createdb
	6. python3 app.py
	7. run local server - http://127.0.0.1:5000/
