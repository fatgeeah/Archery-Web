from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title = "Archery Web",layout= "wide")


def load_lottieurl(url):       
 r = requests.get(url)
 if r.status_code !=200:
    return None
 return r.json()

 # LOAD ASSETS
img_Archer = Image.open("images/Archer.png")
img_Archery = Image.open("images/Archery.png")

 # Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

    local_css("style/style.css")       


#LOAD ASSETS
lottie_coding =load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_rtceylyu.json")  


#HEADER SECTION 
with st.container():
      st.title("Welcome to PreArcher :wave:")
      st.subheader("A Professional Archer ")
      st.write(
        """
        Using this website as a guide to becoming a professional archer will ensure that you are able to understand and engage more in the arts of the sport archery:
        - This will increase your ability to concentate and apadt to new surroundings.
        - This will secure a possibilitiy of creating a career out of this sport.
        - This will allow better knowledge before engaging which will benefit your health.""")

      st.write ("[Learn more about archery>](https://archery360.com/archery-101/)")

# WHAT THE SITE IS ABOUT
with st.container():
     st.write("---")
     left_column, right_colum = st.columns(2)
     with left_column:
      st.header("What is Archery all about and Why you should enagage with it")
      st.write(
        """
        This website will explain the basic whilst the youtube chanel I have provided will explain everything in depth:
       - Archery is the sport, practice, or skill of using a bow to shoot arrows.
       - Archery has the ability to eases arthritis pain for some people through consistent practice and muscle memory.
       - The primary benefit of archery is that it improves hand-eye coordination.
       - All body components are used when practicing, especially arms, hands, chest, and shoulders. 
       - Tension on the muscle is maintained for many seconds before the string is been released. 
       - Repetitive activity results into muscle development therefore building up strength.""")

      st.write("[YouTube Chanel(Archery) >](https://www.youtube.com/watch?v=5_c6K_DYpRU)")

with right_colum :
    st_lottie(lottie_coding, height=300, key= "Archery")

# Past Competitions
with st.container():
    st.write("---")
    st.header("What to know about Archery Events")
    st.write(
                """
               Archery Events:
               - An archery event often depends on the type of archery you are taking part in. Generally, though, the closer you get to the middle of the target, the more highly you’ll be scored. In most cases, an arrow can be worth between one to ten points. As a general rule, you’ll be scored across rounds. These rounds will be further broken down into ends.
               - There are MANY types of Archery Events such as :
                  - Target Archery
                  - Field Archery
                  - 3D Archery
                  - Flight Archery
                  - Indoor Archery
                  - Para Archery
                  - Ski Archery
                  - Run Archery
                """
            )
    st.markdown("[To find more about Types of Archery>](https://archerygb.org/about/types-of-archery)")
    
   
    image_column, text_column = st.columns((1, 2 ))
    with image_column:
     st.image(img_Archer)
              
    with text_column:
        st.header("Benefits of Archery Competiotions")
        st.write(
                """
                Archery is very beneficial because of what it has to offer such as:
                - Improves focus as archers are not only some physical strength, but also mental fitness, and archers develop their focus, flexibility, and attention skills.
                - Archery is relatively inexpensive: it can be a cheap sport if you just want to play for fun ;however, if you want to compete, then the price can increase, and requires a lot of your time as well as dedication.
                - Improves patience: as archery is particularly useful for youngsters as it teaches them the benefits of patience; Significant levels of practice are required to reach a decent standard and that level is not reached without patience and dedication.
                - Improves self-confidence : archery provides great satisfaction in combining both mental and physical attributes to good effect ; Whatever the results at the target, every archer is able to draw satisfaction to a lesser or greater extent, from having won a personal mental battle. 
                - Teaches the importance of safety: the sport can be extremely dangerous if people are reckless ; Archery teaches everyone to be responsible for one another and also for the equipment they are using there is clearly no place for reckless behaviour.
                - Archers develop skills and abilities like ; mental strength, aerobic endurance, balance and coordination, reaction time, motivation & self confidence, skill/technique, agility, flexibility, strength and power.
                - Archery is meant to be for everyone which teaches a person other benefits like teamwork ; Furthermore, it is a good way to socialize. A person needs to have adequate socialization levels in order to sustain a healthy mental life.
                - Archery is a great sport for building confidence quickly as the feeling of shooting a bow and accomplishing your goal , whether it's drilling a bull's eye or executing a great shot, helps you build self-esteem and enjoy a sense of accomplishment.
                - Archery also demands correct posture to hit the bull's eye ; Hence, regular practise of archery improves overall physical posture, improves low back pains, improves the alignment of your back and strengthens shoulders.
                - Archery can be considered as a Meditative Practice as it is a form of active meditation, providing a positive impact on a person's mood and helping to ease anxiety and depression ; with some archers noting that it can be just as calming as yoga as it balances the body and mind.
                - The effects of Archery has been cited as improved sleep, reduced stress levels, and sharpened mental faculties like memory and problem-solving ; participating in archery, especially in an outdoor setting with other people, can positively influence mental health.
                 """

            )
        st.markdown("[Watch the video of reward ceremony.](https://www.youtube.com/watch?v=RPocPEQ4Ick)")
 
with st.container():
    image_column, text_column = st.columns((1, 2 ))
    with image_column:
          st.image(img_Archery)

    with text_column:
            st.header("Live perfomance of an Archery event")
            st.write("Watch live performance of archery events or competitions that will blow your mind and make you see how archery can become when you practices and set your mind towards it.")
            st.write(
                """
                Someone known as  Paulo Coelho once said that :
                "I am a very good archer. I use archery as my way of meditation. I cannot sit down and just meditate in the classical sense. I am very active. So, I use archery. I have my bow, my arrow and I use this tension and relaxation in the second after throwing the arrow. And it is my way to meditate and this is the only thing that clears my mind. When I do archery, I am totally there with my bow, my target, my arrow, and I don’t think, I am communion with the universe.
            """
            )

            st.markdown("[Watch the video of a live Archery Event.](https://www.youtube.com/watch?v=ilA-uusMHis)")
       
           

# CONTACT
st.write("---")
st.header("Contact to find out more information")
contact_form ="""
<form action="https://formsubmit.co/fatgeeahminkis@gmail.com" method="POST">
     <input type = "hidden" name = "_captcha" value = "false">
     <input type="text" name="name" placeholder ="Your name" required>
     <input type="email" name= "email" placeholder ="Your email" required>
     <textarea name = "messages" placeholder = "Your message here " required></textarea>
     <button type="submit">Send</button>
</form> 
"""
left_column , right_colum = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html= True)
    with right_colum:
        st.empty()