# Cohen Kappa Score
Cohen Kappa Score - Unofficial Python Implementation using matrix multiplication

The kappa score is used to compare more accurate performance on nominal and ordinal scales. I inspired by [데이터마이닝에서 Cohen의 kappa를 이용한 분류정확도 측정](https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO201306735655420&dbt=NART). More information about the formula can be found [here](https://en.wikipedia.org/wiki/Cohen%27s_kappa). 

# Equation
#### Kappa Score
$$ K = {{P_o-P_e}\over{1-P_e}} $$

#### weightd Kappa Score

$$ linear \ w_{ij} = 1 - {|i-j|\over{R-1}}$$

$$ quadratic \ w_{ij} = 1 - {(i-j)^2\over{(R-1)^2}}$$

$$ weighted \ kappa \ score= {{\Sigma_{i=1}^{I}\Sigma_{j=1}^{J}{w_{ij}P_{ij}}-\Sigma_{i=1}^{I}\Sigma_{j=1}^{J}w_{ij}P_{i.}P_{.j}}\over{1-\Sigma_{i=1}^{I}\Sigma_{j=1}^{J}{w_{ij}P_{i.}P_{.j}}}}$$
