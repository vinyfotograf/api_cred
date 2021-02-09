<h1>Welcome to Cred_API<h1>

<h3>Here is a sample of project created with flask api</h3>

<p>O aplicativo recebe uma entrada em json e realiza as validações necessárias para aprovação de uma transação</p>

<ul>
    <li>When the value of installmets exceeds 30% of income: compromised-income</li>
    <li>When the score is lower than 200: low-score</li>
    <li>When the istallments value is lower than 6: minimum-installments</li>
    <li>When happens two transactions in the same 2 minutes: doubled-transactions</li>
</ul>

<p>To store the transaction, <a href="https://flask-caching.readthedocs.io/en/latest/" >Flask-Cahing<a> was used</p>

<p>This project uses <a href="https://pypi.org/project/virtualenv/">virtualenv</a> for virtual environment management.</p>

`\venv\Scripts\activate`

<p>Running</p>

`cd cred_api\run.py`

<h2>For the application test, the </a href="https://www.postman.com/downloads/"> Postman</a> was used</h2>

<h4>Location API:</h4>
<p>GET - getTransaction</p> http://127.0.0.1:5000/transaction


<a href="https://flask.palletsprojects.com/en/1.1.x/" >Learn More abaout Flask Project<a/>




