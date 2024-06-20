import streamlit as st
from docxtpl import DocxTemplate
import io
from sip_utils import *

# function to format document
def render_docx(data):
    doc = DocxTemplate(report_dict['SIP Report'])
    doc.render(data)
    return doc

# set page configuration
st.set_page_config(
    page_title="Sample Report Generator",
    layout="wide")

# initialize variables in session state
if 'Context' not in st.session_state:
	st.session_state['Context'] = {'Title_of_Report' : '[Report Title]',
	'Faculty_Advisor': '[Faculty Advisor]',
	'Org_Advisor' : '[Organization Advisor]',
    'Org_Name' : '[Organization Name]',
    'Date' : 'July 2024',
    'Student_Name' : "[Student Name]",
    'Student_Number' : '[Student Number]',
    'Year' : report_year_ug,
    'Program' : '[Program]',
	'Student' : 'undergraduate'}

st.markdown("Enter your information here for the SIP Report Template:")

# which report

st.session_state['Context']['Title_of_Report'] = st.text_input(Title_of_Report['Question'], key='report_name',placeholder=Title_of_Report['placeholder'])

st.session_state['Context']['Student_Name'] = st.text_input(Student_Name['Question'], key='student_name',placeholder=Student_Name['placeholder'])

st.session_state['Context']['Student_Number'] = st.text_input(Student_Number['Question'], key='student_no',placeholder=Student_Number['placeholder'])

st.session_state['Context']['Program'] = st.selectbox(Program['Question'], Program['options'], index=None,placeholder=Program['placeholder'])

#st.session_state['Context']['Date'] = st.text_input(Date['Question'], key='date',placeholder=Date['placeholder'])

st.session_state['Context']['Faculty_Advisor'] = st.text_input(Faculty_Advisor['Question'], key='faculty',placeholder=Faculty_Advisor['placeholder'])

st.session_state['Context']['Org_Advisor'] = st.text_input(Org_Advisor['Question'], key='org_adv',placeholder=Org_Advisor['placeholder'])

st.session_state['Context']['Org_Name'] = st.text_input(Org_Name['Question'], key='org_name',placeholder=Org_Name['placeholder'])


if st.button("Submit Form"):
	if st.session_state['Context']['Title_of_Report']:
		if st.session_state['Context']['Student_Name']:
			if st.session_state['Context']['Student_Number']:
				if st.session_state['Context']['Program']:
					# change year based on the program
					if st.session_state['Context']['Program'] == 'UG':
						st.session_state['Context']['Year'] = report_year_ug
						st.session_state['Context']['Student'] = 'undergraduate'
					if st.session_state['Context']['Program'] == 'PG':
						st.session_state['Context']['Year'] = report_year_pg
						st.session_state['Context']['Student'] = 'postgraduate'
					if st.session_state['Context']['Year']:
						if st.session_state['Context']['Date']:
							if st.session_state['Context']['Faculty_Advisor']:
								if st.session_state['Context']['Org_Advisor']:
									if st.session_state['Context']['Org_Name']:
										doc = render_docx(st.session_state['Context'])
										bio = io.BytesIO()
										doc.save(bio)

										st.download_button(label="Download Template Report",
											data=bio.getvalue(),
											file_name='Student_name_SIP.docx',
											mime='docx')

st.markdown("*if you do not get a button to download the template after submitting the form, please check if you have filled information in all the above mentioned fields.")
