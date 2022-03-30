<h2><center><strong>Exploratory Data Analysis & Regression Modeling:</strong></center></h2>
<h3><center><strong>Happiness vs. Mental Health Disorders</strong></center></h3>

<h4><strong>Objective</h4></strong>

<p>The aim of this project is to analyze rates of happiness, 
    as assigned by <a href="https://worldhappiness.report/ed/2021">World Happiness Report</a>, 
    vs rates of mental health disorders provided by <a herf="https://ourworldindata.org/mental-health">Our World in Data: Mental Health</a>.
    We provide a linear regression model of the data, correlating metrics, and graphs for data visualization. The linear regression model strives to determine whether rates of mental health disorders are predictive of happiness.
    In addition, we have provided functionality to review averages as well as customize sort order. </p>

<h4><strong>Conclusion</h4></strong>

<ul>
<li>Rates of mental health disorders are not predictive of happiness scores</li>
<li>Rates of mental health disorders and happiness scores do not significantly vary across years between the period of 2005-2019</li>
<li>Rates of mental health disorders and happiness scores significantly vary between countries</li>
</ul>

<h4><strong>Prerequisites</h4></strong>
<p>Before you begin, please be sure to download the virtual environment provided. Necessary packages can be found within the requirements.txt file, and are listed below:</p>
<ul>
<li>python 3.9</li>
<li>pandas 1.4.1</li>
<li>numpy 1.22.2</li>
<li>skikit-learn 1.0.2</li>
<li>matplotlib 3.5.1</li>
</ul>

<h4><strong>Utilizing Happiness vs Mental Health Disorders</strong></h4>
<p>While utilizing Happiness vs Disorders, you have the ability to select the visualization, averages, and sort order of the data. In addition, metrics related to the evaluation of the model, such as coefficient of determination, mean squared error, mean absolute error, and root mean squared error, will output to the console upon running the script.</p>

<p>-p will select the type of visualization, options include the initial data set (-p Data), the linear regression of happiness vs disorders (-p Regression), happiness by country (-p HappinessByCountry), disorders by country (-p DisordersByCountry), happiness by year (-p HappinessByYear), and disorders by year (-p DisordersByYear)</p>

<p>-m will provide a CSV of average data based on your selection, options include happiness by year (-m HappinessByYear), disorder by year (-m DisorderByYear), happiness by country (-m HappinessByCountry), and disorder by country (-m DisorderByCountry)</p>

<p>-s will provide a CSV of the data sorted by happiness score or disorder prevalence, options include happiness score (-s Happiness) and disorder prevalence (-s MHDisorders)</p>

<p>For example:</p>
<p>python3 main.py -p Regression -m HappinessByYear -s Happiness</p> 

<h4><strong>Contributors</strong></h4>
<p>Katrina Wheeler- katrina.wheeler@du.edu</p>
<p>Nicole Pierick- nicole.pierick@du.edu</p>






