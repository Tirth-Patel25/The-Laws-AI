from langchain_core.tools import tool

@tool
def judgementType(question: str):
    '''
    This tool is used to answer the question which are related to judgement related for example: 
    
    Q. Is there any judgment showing how much period needs to expire for an asset to become npa under sarfaesi act
    Q. Provide Supreme court judgments discussing the rights of daughters in a coparcenary property.
    Q. First applicant (loan borrower) obtained a loan but the bank didnt get a life insurance policy assigned to bank. Please send citation for the same.
    Q. Under Maharashtra Tenancy and Agricultural Lands Act, 1948 Relating to  Sec. 70 B
    Q. Please share the case law of Supreme Court Promoter & Builder can not sell common terrace and parking space
    Q. Witness came in the witnesses box one time and given half evidence but thereafter didnot come   whether the evidence discard or not
    Q. Between the two wills notary has been same and witness is differed then its must be call the notary for evidence
    Q. Provide Supreme court judgments discussing the rights of daughters in a coparcenary property.
    Q. I need judgements. Estoppel under SARFASI Act for issuing second notice after withdrawal of proceedings under first notice
    Q. Judgement revision against interlocutory order of rejection of handwriting expert as defence witness
    Q. Provide me the latest judgments of Gujarat Hight court on Land Grabing

    
    '''

@tool
def actType(question: str):
    '''
    This tool is used to answer the question which are related to judgement related for example: 
    
    Q. Suit can withdraw at any time as per the order 23 rule 1
    Q. when the prima facie the provisions of sc/st (poa) not applicable, the petition for anticipatory bail maintainable
    Q. What are the primary elements that need to be established to prove action under act of defense?
    Q. What is the recent amendment in section 11 arbitration?
    Q. What are the legal remedies available to an individual for violation of Right to Privacy?
    Q. The suit is file for adverse possession.Limitation for the  filing of the suit  If any case law please send it
    Q. When there is no doctor certificate attached to the WILL, the said WILL is not legal and valid.
    Q. Before the completion of the loan bank without recall the loan can not demand the outstanding amount. The bank only demand the overdue amount

    '''

@tool
def orderType(question: str):
    '''
    This tool is used to answer the question which are related to judgement related for example: 
    
    Q. Suit can withdraw at any time as per the order 23 rule 1
    Q. when the prima facie the provisions of sc/st (poa) not applicable, the petition for anticipatory bail maintainable
    Q. What are the primary elements that need to be established to prove action under act of defense?
    Q. What is the recent amendment in section 11 arbitration?
    Q. What are the legal remedies available to an individual for violation of Right to Privacy?
    Q. The suit is file for adverse possession.Limitation for the  filing of the suit  If any case law please send it
    Q. When there is no doctor certificate attached to the WILL, the said WILL is not legal and valid.
    Q. Before the completion of the loan bank without recall the loan can not demand the outstanding amount. The bank only demand the overdue amount

    '''