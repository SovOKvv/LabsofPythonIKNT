# Пятачок и Винни-Пух решили съесть квадратную шоколадку 7 × 7. Они поочерёдно по
# клеточкам выедают из неё кусочки: Пятачок — 1 × 1, Винни-Пух — 2 × 1 или 1 × 2 (кусочки
# можно выедать не обязательно с краю). Первый ход делает Пятачок. Если перед ходом Винни-
# Пуха в шоколадке не осталось ни одного кусочка 2 × 1 или 1 × 2, то вся оставшаяся шоколадка
# достаётся Пятачку. Выигрывает тот кто больше съест.

class GameState:
    """
    Представляет состояние шоколадной доски 7x7 и текущий счёт участников.

    Attributes:
        board (list[list[int]]): Двумерный массив 7x7, где 0 — целая клетка, 1 — съеденная.
        pig_score (int): Количество клеток, съеденных Пятачком.
        pooh_score (int): Количество клеток, съеденных Винни-Пухом.
    """
    def __init__(self, board=None, pig_score: int = 0, pooh_score: int = 0):
        if board is None:
            self.board = [[0] * 7 for _ in range(7)]
        else:
            self.board = [row[:] for row in board]

        self.pig_score = pig_score
        self.pooh_score = pooh_score

    def get_pig_moves(self):
        moves = []
        for r in range(7):
            for c in range(7):
                if self.board[r][c] == 0:
                    new_board = [row[:] for row in self.board]
                    new_board[r][c] = 1
                    moves.append((
                        GameState(new_board, self.pig_score + 1, self.pooh_score),
                        f'Пятачок съел клетку ({r + 1}, {c + 1})'
                    ))
        return moves

    def get_pooh_moves(self):
        moves = []
        for r in range(7):
            for c in range(7):
                if c + 1 < 7 and self.board[r][c] == 0 and self.board[r][c + 1] == 0:
                    new_board = [row[:] for row in self.board]
                    new_board[r][c] = 1
                    new_board[r][c + 1] = 1
                    moves.append((
                        GameState(new_board, self.pig_score, self.pooh_score + 2),
                        f'Винни съел 1x2 на ({r + 1}, {c + 1}) и ({r + 1}, {c + 2})'
                    ))
                if r + 1 < 7 and self.board[r][0 if c < 0 else c] == 0 and self.board[r + 1][c] == 0:
                    new_board = [row[:] for row in self.board]
                    new_board[r][c] = 1
                    new_board[r + 1][c] = 1
                    moves.append((
                        GameState(new_board, self.pig_score, self.pooh_score + 2),
                        f'Винни съел 2x1 на ({r + 1}, {c + 1}) и ({r + 2}, {c + 1})'
                    ))
        return moves

    def count_remaining_cells(self):
        return sum(row.count(0) for row in self.board)

    def display_board(self):
        print('   1 2 3 4 5 6 7')
        for idx, row in enumerate(self.board):
            line = ' '.join('.' if cell == 0 else 'X' for cell in row)
            print(f'{idx + 1}  {line}')

    def __repr__(self):
        return f'Пятачок: {self.pig_score}, Винни: {self.pooh_score}'


class HumanPlayer:
    """
    Игрок с выбором роли для ввода.

    Attributes:
        name (str): Имя игрока.
        is_pig (bool): Флаг роли; True, если играет за Пятачка, иначе за Винни.
    """
    def __init__(self, name: str, is_pig: bool):
        self.name = name
        self.is_pig = is_pig

    def make_move(self, state: GameState):
        moves_with_desc = state.get_pig_moves() if self.is_pig else state.get_pooh_moves()

        print('\nДоступные ходы (первые 15 вариантов):')
        for idx, (m, desc) in enumerate(moves_with_desc[:15], 1):
            print(f'  {idx}. {desc}')
        if len(moves_with_desc) > 15:
            print(f'  ... и еще {len(moves_with_desc) - 15} вариантов.')

        while True:
            choice = input(f'{self.name}, выберите номер хода (1-{len(moves_with_desc)}): ').strip()
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(moves_with_desc):
                    return moves_with_desc[idx - 1][0]
            print('Некорректный ввод. Попробуйте снова.')


class AIPlayer:
    """
    Бот, использующий метод максимального сохранения ходов.

    Attributes:
        name (str): Имя бота.
    """
    def __init__(self, name: str):
        self.name = name

    def make_move(self, state: GameState):
        moves_with_desc = state.get_pooh_moves()

        best_move = moves_with_desc[0][0]
        max_future_pooh = -1

        for m, _ in moves_with_desc:
            pooh_options = len(m.get_pooh_moves())
            if pooh_options > max_future_pooh:
                max_future_pooh = pooh_options
                best_move = m

        return best_move


class Game:
    """
    Управляет игровым циклом, подсчётом очков и завершением игры.

    Attributes:
        state (GameState): Текущее состояние поля шоколадки и счёта.
        players (list): Список из двух игроков.
    """
    def __init__(self, mode: str):
        self.state = GameState()
        if mode == '1':
            self.players = [HumanPlayer('Пятачок (Вы)', is_pig=True), AIPlayer('Винни-Пух (ИИ)')]
        else:
            self.players = [HumanPlayer('Пятачок (Игрок 1)', is_pig=True),
                            HumanPlayer('Винни-Пух (Игрок 2)', is_pig=False)]

    def run(self):
        print('=== ИГРА: ПЯТАЧОК И ВИННИ-ПУХ ДЕЛЯТ ШОКОЛАДКУ 7x7 ===')
        print('Пятачок съедает 1x1, Винни-Пух съедает 2x1 или 1x2.')
        print('Если у Винни нет ходов 2x1/1x2, вся оставшаяся шоколадка достается Пятачку!\n')

        current_idx = 0

        while True:
            current_player = self.players[current_idx]
            print('\n-------------------------------------------')
            self.state.display_board()
            print(f'Счёт -> {self.state}')

            if current_idx == 0:
                if self.state.count_remaining_cells() == 0:
                    break
            else:
                pooh_moves = self.state.get_pooh_moves()
                if len(pooh_moves) == 0:
                    rem = self.state.count_remaining_cells()
                    print('\n==========================================')
                    print(f'У Винни-Пуха нет ходов 2x1 или 1x2!')
                    print(f'Пятачок забирает оставшиеся {rem} клеток шоколадки!')
                    self.state.pig_score += rem
                    break

            print(f'Ход делает: {current_player.name}')
            self.state = current_player.make_move(self.state)
            current_idx = (current_idx + 1) % 2

        print('\n================ ИТОГИ ИГРЫ ================')
        print(f'Финальный счёт:')
        print(f'  Пятачок: {self.state.pig_score} клеток')
        print(f'  Винни-Пух: {self.state.pooh_score} клеток')

        if self.state.pig_score > self.state.pooh_score:
            print('ПОБЕДИЛ ПЯТАЧОК!')
        elif self.state.pooh_score > self.state.pig_score:
            print('ПОБЕДИЛ ВИННИ-ПУХ!')
        else:
            print('НИЧЬЯ!')
        print('============================================')


if __name__ == "__main__":
    print('Выберите режим игры:')
    print('1. Человек (Пятачок) vs Бот (Винни-Пух)')
    print('2. Человек vs Человек')

    choice = input('Ваш выбор (1 или 2): ').strip()
    game = Game(choice)
    game.run()