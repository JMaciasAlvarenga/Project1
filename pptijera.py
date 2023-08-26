import random
import streamlit as st
#import os
#clear = lambda: os.system('cls')
#clear()
#Con esto limpia el terminal

st.title("My First Program in Streamlit")



list_game = ['Piedra','Papel','Tijera']
choose_player1 = st.selectbox("Select one Option :", list_game)


# El player 2 va ser la computadora e ingresa la opcion de forma random
choose_player2 = list_game [random.randint(0,2)]

st.write(" Option slected by player  😎: ", choose_player1)
st.write(" Option slected by computer 💻: ", choose_player2)

if choose_player1 in list_game:
   
   if choose_player2 == choose_player1:
       st.header("Empate!! 😒  Piensa mejor la proxima vez! 🤔")
   elif choose_player1 == "Piedra":
        if choose_player2 == "Tijera":
             st.header("Ganaste!! 😃")
        else:
             st.header("Perdiste!! 😢 Mejor Suerte en la proxima!")
   elif choose_player1 == "Papel":
        if choose_player2 == "Piedra":
             st.header("Ganaste!! 😃")
        else:
             st.header("Perdiste!! 😢Mejor Suerte en la proxima!")
   elif choose_player1 == "Tijera":
        if choose_player2 == "Papel":
             st.header("Ganaste!! 😃")
        else:
             st.header("Perdiste!! 😢 Mejor Suerte en la proxima!")
else:
    st.header("Escoger una opcion valida : Piedra o Papel o Tijera")