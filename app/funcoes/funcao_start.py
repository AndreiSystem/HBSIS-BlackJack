from app.classes.cartas import Cartas
from app.funcoes.funcao_continuar import continuar

class BlackJack:
    def __init__(self):
        self.pt = 0
        self.cartas = Cartas()

    def jogo_start(self):

        continuar_resp = True

        print('Começou!')

        while continuar_resp:
            self.cartas.embaralhar()

            carta_retirada = self.cartas.retirar_carta()
            self.cartas.salvar_cartas(carta_retirada)


            self.cartas.retornar_cartas_salvas()

            try:
                self.pt += int(carta_retirada)
                print(f'Pontuação: \033[1;32m{self.pt}\033[m')
            except:
                if carta_retirada == 'A':
                    if self.pt > 0:
                        self.pt += 1
                    else:
                        self.pt += 11
                elif carta_retirada == 'J':
                    self.pt += 10
                elif carta_retirada == 'Q':
                    self.pt += 10
                else:
                    self.pt += 10
                print(f'Pontuação: \033[1;32m{self.pt}\033[m')

            continuar_resp = continuar()

            if len(self.cartas.get_cartas()) == 0:
                print('\033[1;33mOpa as cartas acabaram! Fim de jogo.\033[m')
                print('Jogo Finalizado!')
                break
            elif self.pt >= 21:
                print('\033[1;33mOpa você passou dos 21 pontos! Fim de jogo.\033[m')
                print('Jogo Finalizado!')
                break
            else:
                continue









