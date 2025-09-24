from langchain_core.tools import tool

@tool
def judgement(query:str):
    '''
    Use this tool to retrieve or summarize Indian court judgments.

    Includes:
    - Supreme Court judgments
    - High Court judgments
    - Tribunal decisions (if applicable)
    - Any Court Judgements

    Trigger this tool whenever the user asks about:
    - Specific case laws or citations
    - Landmark judgments
    - Legal precedents in India
    - Court rulings related to a topic

    Example Queries:
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
    pass

@tool
def act(query:str):
    '''
     Use this tool to provide details about Indian Acts and their sections.

    Includes:
    - Central Acts (e.g., IPC, Companies Act, IT Act, GST Act)
    - State-specific Acts
    - Explanations of legal sections

    Trigger this tool whenever the user asks about:
    - Explanation or meaning of an Act
    - Specific sections of Indian law
    - Compliance or requirements under an Act

    Example Queries:
    Q. Suit can withdraw at any time as per the order 23 rule 1
    Q. when the prima facie the provisions of sc/st (poa) not applicable, the petition for anticipatory bail maintainable
    Q. What are the primary elements that need to be established to prove action under act of defense?
    Q. What is the recent amendment in section 11 arbitration?
    Q. What are the legal remedies available to an individual for violation of Right to Privacy?
    Q. The suit is file for adverse possession.Limitation for the  filing of the suit  If any case law please send it
    Q. When there is no doctor certificate attached to the WILL, the said WILL is not legal and valid.
    Q. Before the completion of the loan bank without recall the loan can not demand the outstanding amount. The bank only demand the overdue amount

    '''
    pass

@tool
def order(query:str):
    '''
      Use this tool to fetch or explain Indian government or court orders.

    Includes:
    - Notifications, circulars, and government orders
    - Court-issued interim or final orders
    - Regulatory authority orders (RBI, SEBI, etc.)

    Trigger this tool whenever the user asks about:
    - Official government notifications
    - Court orders (not judgments)
    - Administrative or regulatory directions

    Example Queries:
    Q. Under what circumstances can a party be added to a suit under Order 1 Rule 10 CPC?
    Q. What is the effect of non-joinder of claims under Order 2 Rule 2 CPC?
    Q. What are the modes of service of summons under Order 5 CPC?
    Q. What is the difference between material facts and evidence as per Order 6 Rule 2 CPC?
    Q. When can a plaint be rejected under Order 7 Rule 11 CPC?
    Q. What is the time limit for filing a written statement under Order 8 Rule 1 CPC?
    Q. What remedies are available when the defendant does not appear under Order 9 CPC?
    Q. What is the evidentiary value of admissions under Order 12 Rule 6 CPC?
    Q. Differentiate between issues of law and issues of fact under Order 14 CPC.
    Q. Under what circumstances can adjournments be granted under Order 17 CPC?
    Q. What are the modes of execution of decrees under Order 21 CPC?
    Q. What is the effect of the death of a party during a suit under Order 22 CPC?
    Q. What is the difference between withdrawal of suit with and without permission under Order 23 CPC?
    Q. What are the grounds for granting a temporary injunction under Order 39 CPC?
    Q. What powers does an appellate court have under Order 41 Rule 33 CPC?

    '''
    pass