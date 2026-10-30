import datetime
import calendar



meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

dia  = ["segunda-feira", "terça feira", "quarta feira", "quinta feira", "sexta feira"]


#  21/12/2021 ( colocar padrão americano ano/mes/dia)
data = datetime.date(2024, 12, 21)

print(data)

hoje = datetime.date.today()

print(hoje)

# formatar a data funçao Brasil
print(hoje.strftime("%d/%m/%Y"))



hoje = datetime.date.today()
print(hoje)
print(hoje.strftime("%d/%m/%Y"))
print(f"São Paulo, {dia[hoje.weekday()]}, {hoje.day} de {meses[hoje.month -1]} de {hoje.year}")

# saber se o ano é bissexto
print(f"2027 é Bissexto: {calendar.isleap(2027)}")

# para saber o ultimo dia do ano 
print(f"É o ultimo dia do mês? {calendar.monthrange(2026,10)[1]}")

