from flask import Flask, render_template, request, redirect, url_for
import subprocess, os
from subprocess import PIPE

app = Flask(__name__)


@app.route('/')
def Compiler():
	check = ''
	language = ''
	return render_template('home.html',
	                        check = check,
							data = [{'language':'C'}, {'language':'Python'}]
	)


@app.route('/submit', methods = ['GET','POST'])
def submit():
	if request.method == 'POST':

		code = request.form['code']
		inp = request.form['input']
		chk = request.form.get('check')
		lan = request.form.get('comp_select')

		if  not chk == '1':
			inp = ""
			check = ''
		else:
			check = 'checked'

		output = complier_output(code, inp, chk, lan)
	return render_template('home.html',
	                        code = code,
							input = inp,
							output = output,
							check = check,
							data = [{'language':'C'}, {'language':'Python'}]
    )


def createFile(code, lan):
	if lan == "Python":
		extension = ".py"
	else:
		extension = ".c"

	fileName = "try" + extension

	if not os.path.exists(fileName):
		os.open(fileName, os.O_CREAT)

	fd = os.open(fileName, os.O_WRONLY)

	os.truncate(fd, 0)
	fileadd = str.encode(code)
	os.write(fd, fileadd)
	os.close(fd)


def complier_output(code, inp, chk, lan):

	if lan == 'Python':

		createFile(code, lan)

		process = subprocess.Popen(['python3', 'try.py'], stdout = PIPE, stdin = PIPE, stderr = PIPE)

		#communicate() returns a tuple (stdoutdata, stderrdata)
		output = process.communicate(input = inp.encode())[0]
		error = process.communicate(input = inp.encode())[1]
		check = process.returncode
		if check == 0:
			return output.decode("utf-8")
		else:
			return error.decode("utf-8")
	else:

		createFile(code, lan)
		process = subprocess.run(['gcc','-o','out','try.c'], stderr = PIPE,)
		check = process.returncode

		if check == 0:
			if chk == '1':
				run = subprocess.run(["./out"], input = inp.encode(), stdout = PIPE)
			else:
				run = subprocess.run(["./out"], stdout = PIPE)
			return run.stdout.decode("utf-8")
		else:
			return process.stderr.decode("utf-8")


if __name__ == '__main__':
	app.run(debug = True)
