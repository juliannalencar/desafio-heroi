nome_heroi = input('Digite o nome do seu herói: ')
experiencia_heroi = int(input('Digite a quantidade de XP acumulada: '))

if experiencia_heroi <= 1000:
    experiencia_heroi = 'Ferro'
elif experiencia_heroi > 1000 or experiencia_heroi <= 2000:
    experiencia_heroi = 'Bronze'
elif experiencia_heroi > 2000 or experiencia_heroi <= 5000:
    experiencia_heroi = 'Prata'
elif experiencia_heroi > 6000 or experiencia_heroi <= 7000:
    experiencia_heroi = 'Ouro'
elif experiencia_heroi > 7000 or experiencia_heroi <= 8000:
    experiencia_heroi = 'Platina'
elif experiencia_heroi > 8000 or experiencia_heroi <= 9000:
    experiencia_heroi = 'Ascendente'
elif experiencia_heroi > 9000 or experiencia_heroi <= 10000:
    experiencia_heroi = 'Imortal'
else:
    experiencia_heroi = 'Radiante'
    
print(f'O Herói de nome **{nome_heroi}** está no nível de **{experiencia_heroi}**')