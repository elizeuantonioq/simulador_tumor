import sympy as sp

print('/////////////////////////////////////////')
print("/// Simulador de Crescimento de Tumor ///")
print('/////////////////////////////////////////')

print("\nInforme os dados do modelo de crescimento do tumor:")

crescimento_acelerado = float(input("Crescimento acelerado do tumor (cm) (coeficiente t²): "))
crescimento_linear = float(input("Crescimento linear do tumor (cm) (coeficiente t): "))
tamanho_inicial = float(input("Tamanho inicial do tumor (cm): "))

tamanho_critico = 10

# Incógnita
tempo = sp.symbols('tempo')

# Equação polinomial
equacao = sp.Eq(
    crescimento_acelerado * tempo**2 +
    crescimento_linear * tempo +
    tamanho_inicial,
    tamanho_critico
)

# Resolver equação
resultado = sp.solve(equacao, tempo)

print("\n--- Resultado ---")
print("O tumor atingirá o tamanho crítico no tempo de (meses):")

for valor in resultado:
    if valor.is_real and valor >= 0:
        print(f"{valor:.1f}")

