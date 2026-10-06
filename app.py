import streamlit as st
import pandas as pd

# Give our app a super cool title!
st.title("🌟 My Awesome Pokemon Power Predictor!")

# Read your CSV file (The data you just opened!)
df = pd.read_csv("PokemonData.csv")

# Show a sneak peek of the data on the screen
st.write("### Here are the Pokemon hiding in your data:")
st.dataframe(df.head())

# Create a dropdown menu so you can pick a Pokemon
pokemon_name = st.selectbox("Pick a Pokemon to check its power!", df['Name'])

# Find the exact Pokemon you picked
my_pokemon = df[df['Name'] == pokemon_name]

st.write(f"### You chose {pokemon_name}!")
st.table(my_pokemon[['HP', 'Attack', 'Defense', 'Speed']])

# Make a simple "Prediction" based on their attack score!
attack_power = int(my_pokemon['Attack'].iloc[0])

if attack_power >= 100:
    st.success("🔥 PREDICTION: This Pokemon is a super-strong fighter! It will win easily!")
elif attack_power >= 60:
    st.info("⚔️ PREDICTION: This Pokemon is a great fighter. Good for your team!")
else:
    st.warning("🛡️ PREDICTION: This Pokemon is a little weak right now. It needs more training!")