import streamlit as st
st.sidebar.title(" Aluguel de Carros")
st.sidebar.image("carro.png" , width=150)


st.sidebar.write("Escolha o carro ideal pra você!")

carros = ["Chevrolet Onix Plus" , "Volkswagen Polo" , "Fiat Cronos" , "Peugeot 2008" , "Hyundai HB20"]

opcao = st.sidebar.selectbox("Escolha o carro que foi alugado" , carros)




st.title(" JP-Aluguel de carros")

st.image(f"{opcao}.png")
st.markdown(f"## Você alugou o modelo {opcao}")
st.markdown("---")


dias = st.text_input(f"Por quantos dias o {opcao} foi alugado?")
km = st.text_input(f"Quantos km você rodou com o {opcao} ?")


if opcao == "Chevrolet Onix Plus":
    diaria = 450

elif opcao == "Volkswagen Polo":
    diaria = 500

elif opcao == "Fiat Cronos":
    diaria = 300

elif opcao == "Peugeot 2008":
    diaria = 250

elif opcao == "Hyundai HB20s":
    diaria = 120

### CAUCULAR

if st.button("calcular"):
    dias = int(dias)
    km = float(km)
    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km

    st.warning(f"Você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a pagar é R$ {aluguel_total:.2f}")