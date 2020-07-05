# Online compiler for C and Python

# Setup
	1. git clone https://github.com/Pirate2606/compiler.git
	2. Create a virtual environment:
		1. sudo apt install virtualenv
		2. virtualenv -p python3 <name without brackets>
		3. source <name without brackets>/bin/activate
	3. Get OAuth credentials from Google:
		1. Visit the Google Developers Console at https://console.developers.google.com and create a new project. In the "APIs & auth" section, click on "Credentials", and then click the "Create a new Client ID" button. Select "Web Application" for the application type, and click the "Configure consent screen" button. Put in your application information, and click Save. Once you’ve done that, you’ll see two new fields: "Authorized JavaScript origins" and "Authorized redirect URIs". Set the authorized redirect URI to http://localhost:5000/login/google/authorized, and click "Create Client ID". Google will give you a client ID and client secret.
		2. Paste the client ID and client secret in the `config.py` file inside inverted commas.
	
	3. cd compiler/
	4. pip install -r requirements.txt
	5. flask createdb
	6. python3 app.py
	7. run local server - http://127.0.0.1:5000/
