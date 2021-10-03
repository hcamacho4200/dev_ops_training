# dev_opts_training
A application to help via example of how to leverage CI/CD

# Geting Started
- Move to a Test or Development Directory
<pre>
hcamacho@hcamacho-mn1 config % cd ~/test
</pre>

- Clone the repo
<pre>
hcamacho@hcamacho-mn1 test % git clone https://github.com/hcamacho4200/dev_ops_training.git
Cloning into 'dev_ops_training'...
remote: Enumerating objects: 67, done.
remote: Counting objects: 100% (67/67), done.
remote: Compressing objects: 100% (45/45), done.
</pre>

- Enter the project directory
<pre>hcamacho@hcamacho-mn1 test % cd dev_ops_training</pre>

- Create a Virtual Environment for Python and Activate
<pre>
hcamacho@hcamacho-mn1 dev_ops_training % python3 -m venv venv
hcamacho@hcamacho-mn1 dev_ops_training % . ./venv/bin/activate
</pre>

- Install Requirements
<pre>
(venv) hcamacho@hcamacho-mn1 dev_ops_training % pip install -r requirements.txt
</pre>

- Run the application
<pre>
(venv) hcamacho@hcamacho-mn1 dev_ops_training % cd src
(venv) hcamacho@hcamacho-mn1 src % python main.py
</pre>

Browse to http://127.0.0.1:5000/api/v1/
