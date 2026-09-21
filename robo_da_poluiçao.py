# bibliotecas
import discord
from discord.ext import commands
import random
import asyncio
from discord.ext import commands, tasks

# lista de ataques contra robo da poluição 3000
lista_de_poluiçao_reciclar = [11, 12, 13, 15, 19, 23]
lista_de_poluiçao_nao_gastar_agua = [62, 42, 35, 51, 53]
lista_de_poluiçao_nao_gastar_energia = [54, 42, 49, 51, 53]
lista_de_poluiçao_nao_usar_carro = [100, 102, 92, 12, 97]

# lista da quantidade de poluição
lista_de_poluiçao1 = [11, 12, 13, 15, 19, 23]
lista_de_poluiçao2 = [62, 42, 35, 51, 53]
lista_de_poluiçao3 = [54, 42, 49, 51, 53]
lista_de_poluiçao4 = [100, 102, 92, 72, 97]

# lista de vidas do robo da poluição 3000
lista_de_vida_do_robo_da_poluiçao1 = [55, 64, 11, 57, 60, 59]
lista_de_vida_do_robo_da_poluiçao2 = [62, 67, 58, 60, 71]
lista_de_vida_do_robo_da_poluiçao3 = [123, 129, 112, 101, 95]
lista_de_vida_do_robo_da_poluiçao4 = [11, 145, 172, 151, 97]

# variaveis
jogo_ativo = False
poluiçao = 100
vida = 1000



# configuração de permissões
intents = discord.Intents.default()
intents.message_content = True

# definindo o bot
robo_da_poluiçao = commands.Bot(command_prefix='/', intents=intents)

@robo_da_poluiçao.event
async def on_ready():
    print(f'Bot logado como {robo_da_poluiçao.user}')
    if not regeneracao_do_robo.is_running():
        regeneracao_do_robo.start()

# se robo da poluição perder
async def verificar_fim_jogo(ctx):
    global jogo_ativo, vida, poluiçao
    if vida <= 0:
        vida == 0
        regeneracao_do_robo.stop()
        await ctx.send('🎉 parabéNS-huManO!voCÊ-VENCEU!-paRaBéns, TOma-SEu-preMIo!-É-uMA-eSPaDa-de-sUcATa')
        await ctx.send('⚠️ sistemA cRíTico... dESLIgandO...')
        await ctx.send('você ganhou uma espada de suucata!!')


        await asyncio.sleep(30) 
       
        # robo da poluição reiniciando se caso sua vida acabar
        
        jogo_ativo = False
        vida = 1000
        poluiçao = 100
        await ctx.send('EVENTO: 🔌 SISTEMA REINICIADO. O Robô da Poluição 3000 voltou a "funcionar" na arena!')
        if not regeneracao_do_robo.is_running():
            regeneracao_do_robo.start()

    # player perdendo
    if poluiçao >= 300:
        regeneracao_do_robo.stop() 
        await ctx.send('🎉 ParABÉns! VOcÊ pERDeu! A polUIçÃO subIU MUito! DESligaNdo')

        await asyncio.sleep(5) 

        # robo reinicando se o player perdeu
        vida = 1000
        poluiçao = 100
        await ctx.send('EVENTO: 🔌 SISTEMA REINICIADO. O Robô da Poluição 3000 voltou a "funcionar" na arena!')
        if not regeneracao_do_robo.is_running():
            regeneracao_do_robo.start()

# robo da poluição 3000 se curando
@tasks.loop(seconds=5)
async def regeneracao_do_robo():
    global vida, poluiçao, jogo_ativo
    if jogo_ativo and poluiçao >= 200 and vida >= 0:
        cura = 15
        vida += cura
        print(f"O robô se curou em {cura}! Vida atual: {vida}")

# quando o player usa o comando de entrar na arena
@robo_da_poluiçao.command()
async def ir_na_arena_de_lixo(ctx):
    await ctx.send('--- BEM VINDO A ARENA DE LIXOS ---')
    await ctx.send('você foi na arena de lixo foi dificel de achar pois ela estava bem isolada, quando você chega, você ve a arena de lixo, ela era enorme para uma arena, e sim, toda feita de lixos como: latas,, pneus, sacos de lixo, lixos organicos, etc. Você entra na arena e quando entra, duas pilhas de pneus começam a pegar fogo como tochas, você ve nos seus lados tinha lixeiras de reciclagem, e você ve na sua frente um robô de dois metros de altura escrito no seu peito: anti-natureza 3000, ele parecia quebrado e descontinuado, parecendo que ele tinha sido abandonado la, e ele derrepende acorda e começa a dizer com uma voz robotica:')
    await ctx.send('olá-Humano,-eu-sou-o-MaiOr-inimigo-da-natureza-meu-mEStrE-fez-eu-pra-destruir-tudo-que-tem-de-natureza-nesse-mUNdo,-duvido-vc-me-derrotar-e-se-você-me-DeRRotar-humano-eu-vou-te-dar-uM-PreMIO(aceita a luta?)')

# se caso o player quiser usar o comando de enfrentar o robo mesmo nao estando na arena
async def verificar_estado(ctx):
    global jogo_ativo, vida, poluiçao
    if not jogo_ativo:
        await ctx.send('⚠️: A luta não começou. Use `aceitar_luta_da_arena_de_lixo`.')
        return False

# enfrentar o robo
@robo_da_poluiçao.command()
async def aceitar_luta_da_arena_de_lixo(ctx): 
    global jogo_ativo, vida, poluiçao
    if not jogo_ativo:
        await ctx.send('ok-humano,-vamos-LUtar')
        await ctx.send(f'vida do robo-da-poluiçao 3000: {vida}')
        await ctx.send(f'quantidade de poluiçao: {poluiçao}')
        jogo_ativo = True
        await verificar_estado(ctx)
    # se a luta já começou
    else:
        await ctx.send('⚠️: A luta já começou!')

# primeiro comando de ataque: RECICLAR
@robo_da_poluiçao.command()
async def reciclar(ctx):
    global jogo_ativo, vida, poluiçao
    await ctx.send('DETEcTAR...-literalmente-NaDa,-agORa-miNhA-veZ-HuMano...-pOLUiR')
    await ctx.send(f'vida do robo-da-poluiçao 3000: {vida}')
    await ctx.send(f'quantidade de poluiçao: {poluiçao}')
    vida -= random.choice(lista_de_vida_do_robo_da_poluiçao1)
    poluiçao -= random.choice(lista_de_poluiçao_reciclar)
    poluiçao += random.choice(lista_de_poluiçao1)
    await verificar_fim_jogo(ctx)
    
    return

# segundo comando
@robo_da_poluiçao.command()
async def economizar_agua(ctx):
    global jogo_ativo, vida, poluiçao
    await ctx.send('DETECTAR...-só-uma-dOrzinha,-CONTRA-ATAQUE...-POLUIR')
    await ctx.send(f'vida do robo-da-poluiçao 3000: {vida}')
    await ctx.send(f'quantidade de poluiçao: {poluiçao}')
    vida = random.choice(lista_de_vida_do_robo_da_poluiçao2)
    poluiçao -= random.choice(lista_de_poluiçao_nao_gastar_agua)
    poluiçao += random.choice(lista_de_poluiçao2)
    await verificar_fim_jogo(ctx)
 
    return

@robo_da_poluiçao.command()
async def economizar_energia(ctx):
    global jogo_ativo, vida, poluiçao
    await ctx.send('DETECTAR...-só-uma-dOrzinha,-CONTRA-ATAQUE...-POLUIR')
    await ctx.send(f'vida do robo-da-poluiçao 3000: {vida}')
    await ctx.send(f'quantidade de poluiçao: {poluiçao}')
    vida -= random.choice(lista_de_vida_do_robo_da_poluiçao3)
    poluiçao -= random.choice(lista_de_poluiçao_nao_gastar_energia)
    poluiçao += random.choice(lista_de_poluiçao3)
    await verificar_fim_jogo(ctx)

    return

@robo_da_poluiçao.command()
async def nao_usar_carro(ctx):
    global jogo_ativo, vida, poluiçao, critico4
    await ctx.send('DETECTAR...-PLAca-MÃE!-MUITA-DOR!-CONTRA-ATAQUE...-POLUIR')
    await ctx.send(f'vida do robo-da-poluiçao 3000: {vida}')
    await ctx.send(f'quantidade de poluiçao: {poluiçao}')
    vida -= random.choice(lista_de_vida_do_robo_da_poluiçao4)
    poluiçao -= random.choice(lista_de_poluiçao_nao_usar_carro)
    poluiçao += random.choice(lista_de_poluiçao4)
    await verificar_fim_jogo(ctx)
    return

robo_da_poluiçao.run('TOKEN')
