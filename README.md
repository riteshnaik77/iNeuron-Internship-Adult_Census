# iNeuron-Internship-Adult_Census_Income_Prediction

Here is our webapp 
<li><a href="https://ineuron-salary-pred.herokuapp.com/" rel="nofollow">income_prediction_website</a></li>

<li> [Also here](http://yantra-learning.com/income) </li>

<article class="markdown-body entry-content container-lg" itemprop="text" style=""><h1 dir="auto" style=""><a id="user-content-adult-census-income" class="anchor" aria-hidden="true" href="#adult-census-income" style=""><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true" style=""><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z" style=""></path></svg></a>Adult-Census-Income</h1>
<h2 dir="auto" style=""><a id="user-content-project-description" class="anchor" aria-hidden="true" href="#project-description"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Project Description</h2>
<p dir="auto" style="">In this project we analyze a U.S. census data taken from the <a href="https://archive.ics.uci.edu/ml/datasets/Census+Income" rel="nofollow">UCI Machine Learning Repository</a>. The goal of this project is to profile people in the above dataset based on available demographic attributes.</p>
<ol dir="auto">
<li style="">Construct a model that accurately predicts whether an individual makes more than $50,000.</li>
<li style="">What are the key factors contributing to high vs. low income?</li>
<li>Are there any significant gaps in these Census attributes by gender or race?</li>


</ol>
<h3 dir="auto"><a id="user-content-install" class="anchor" aria-hidden="true" href="#install"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Install</h3>
<p dir="auto">This project requires <a href="https://www.python.org/downloads/release/python-364/" rel="nofollow"><strong>Python 3.x</strong></a> and the following Python libraries installed:</p>
<ul dir="auto">
<li><a href="http://www.numpy.org/" rel="nofollow">NumPy</a></li>
<li><a href="http://pandas.pydata.org" rel="nofollow">Pandas</a></li>
<li><a href="http://matplotlib.org/" rel="nofollow">matplotlib</a></li>
<li><a href="http://scikit-learn.org/stable/" rel="nofollow">scikit-learn</a></li>
</ul>

<p dir="auto">You will also need to have software installed to run and execute an <a href="http://ipython.org/notebook.html" rel="nofollow">iPython Notebook</a></p>
<p dir="auto">It's highly recommended to install <a href="https://www.continuum.io/downloads" rel="nofollow">Anaconda</a>, a pre-packaged Python distribution that contains all of the necessary libraries and software for this project.</p>

<h3 dir="auto"><a id="user-content-code" class="anchor" aria-hidden="true" href="#code"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path>

</svg></a>Code</h3>
<p dir="auto">The main code for this project is located in the <code>Adult income prediction.ipynb</code> notebook file. </p>


<h3 dir="auto"><a id="user-content-data" class="anchor" aria-hidden="true" href="#data"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path>


</svg></a>Data</h3>
<ul dir="auto">
<li><code>adult.csv</code></li>
This dataset consist of 32561 rows & 15 Columns </li>
</ul>
<p dir="auto"><strong>Features</strong></p>
<ul dir="auto">
<li><code>age</code>: continuous.</li>
<li><code>workclass</code>: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.</li>
<li><code>fnlwgt</code>: final weight, continuous.</li>
<li><code>education</code>: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.</li>
<li><code>education-num</code>:  continuous.</li>
<li><code>marital-status</code>: Represents the responding unit’s role in the family. Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.</li>
<li><code>occupation</code>: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.</li>
<li><code>relationship</code>: Represents the responding unit’s role in the family. Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.</li>
<li><code>race</code>: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.</li>
<li><code>sex</code>: Female, Male.</li>
<li><code>capital-gain</code>: income from investment sources, apart from wages/salary, continuous.</li>
<li><code>capital-loss</code>: losses from investment sources, apart from wages/salary, continuous.</li>
<li><code>hours-per-week</code>: continuous.</li>
<li><code>native-country</code>: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&amp;Tobago, Peru, Hong, Holand-Netherlands.</li>
</ul>
<p dir="auto"><strong>Target</strong></p>
<ul dir="auto">
<li><code>income</code>: Income Class (&lt;=50K, &gt;50K)</li>

</ul>
</article>
