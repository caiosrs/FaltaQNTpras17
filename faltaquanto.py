from datetime import datetime, timedelta
from win10toast import ToastNotifier

hora_atual = datetime.now().time()

hora_alvo = datetime.strptime("17:00:00", "%H:%M:%S").time()

# Calcula a diferença entre a hora alvo e a hora atual
diferenca = datetime.combine(datetime.today(), hora_alvo) - datetime.combine(datetime.today(), hora_atual)

# Extrai horas e minutos da diferença
horas, segundos = divmod(diferenca.seconds, 3600)
minutos = segundos // 60

# Formata
tempo_restante = f"{horas} horas e {minutos} minutos"

toast = ToastNotifier()
toast.show_toast("Contagem Regressiva", f"Faltam {tempo_restante} para as 17 horas.", duration=10)

#RESULTADO
print(f"Faltam {tempo_restante} para as 17 horas.")