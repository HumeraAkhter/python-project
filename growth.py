import  streamlit as st



st.set_page_config(page_title= "growth mindset project ❂")
st.title("Growth Mindset challenge: Web PP with streamlit By Humera Yahya")





st.header("🌠 Welcome to your Growth journey ") 
st.write(" ♤ Turn every challenge into your launchpad—grow, evolve, and unleash your full potential!")

#quote section
st.header( "☄  Mindset Quote")
st.write("♜ Take on the growth mindset challenge—transform every setback into a stepping stone, every failure into a lesson, and every obstacle into an opportunity for growth.")

st.header("⌚  WHAT IS YOUR CHALLEGE TODAY")
user_input=st.text_input(" ✍️ Describe a challenge you are facing:")

#condition
if user_input:
    st.success(f"✌️ You 're facing:{user_input} keep pushing fowerd to your goal! 🌟")
else:
    st.warning("Tell us about your challenge to get challenge!")

#reflexing
st.header("Reflect  on your learning")  
reflection=st.text_area("Write your reflection here")  

if reflection:
    st.success(f"⚜️ Great Insight your reflection{reflection}")
else:
     st.info("💎 Reflecting on past experience help to grow! Shares your diffeculties")
     
#achivement
st.header("👑 Celebrate Your Win!") 
achivement=st.text_input("Share something you've recently accomplished") 

if achivement:
    st.success(f"👼 Amazing you achived: {achivement}")
else:
    st.info("Every achivement count! Share one now 👩‍✈️") 

#footer
st.write("- - -") 
st.write(" 🔦Achievement is turning obstacles into stepping stones on the path to success. 🔆") 
st.write(" **Created by HUMERA YAHYA 👸**")     

