# AcrPred: A hybrid optimization with enumerated machine learning algorithm to predict Anti-CRISPR proteins
## Abstract
CRISPR-Cas, as a tool for gene editing, has received extensive attention in recent years. Anti-CRISPR (Acr) proteins can inactivate the CRISPR-Cas defense system during interference phase, and can be used as a potential tool for the regulation of gene editing. In-depth study of Anti-CRISPR proteins is of great significance for the implementation of gene editing. In this study, we developed a high-accuracy prediction model based on two-step model fusion strategy, called AcrPred, which could produce an AUC of 0.952 with independent dataset validation. To further validate the proposed model, we compared with published tools and correctly identified 9 of 10 new Acr proteins, indicating the strong generalization ability of our model. Finally, for the convenience of related wet-experimental researchers, a user-friendly web-server AcrPred (Anti-CRISPR proteins Prediction) was established at http://lin-group.cn/server/AcrPred, by which users can easily identify potential Anti-CRISPR proteins.

## Requires
Python3 (tested 3.5.4)

## Usage
python predict_main.py

## citation
Dao FY, Liu ML, Su W, Lv H, Zhang ZY, Lin H, Liu L. AcrPred: A hybrid optimization with enumerated machine learning algorithm to predict Anti-CRISPR proteins. Int J Biol Macromol. 2023 Feb 15;228:706-714. doi: 10.1016/j.ijbiomac.2022.12.250. Epub 2022 Dec 28. PMID: 36584777.
