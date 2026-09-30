# На доске написано число 2017. Петя и Вася играют в следующую игру: за один ход
# можно вычесть из написанного на доске числа любой его натуральный делитель, кроме него
# самого, и записать результат этого вычитания на доске вместо исходного числа. Проигрывает
# тот, кто не может сделать ход.

class GameState:
    """
    Представляет текущее число на доске и генерирует варианты деления.

    Attributes:
        n (int): Число, записанное на доске.
    """
    def __init__(self, n: int):
        self.n = n

    def get_divisors(self):
        divisors = []
        for i in range(1, self.n):
            if self.n % i == 0:
                divisors.append(i)
        return divisors

    def is_terminal(self):
        return len(self.get_divisors()) == 0

    def get_moves_with_descriptions(self):
        moves = []
        for d in self.get_divisors():
            next_val = self.n - d
            moves.append((GameState(next_val), f'Вычесть делитель {d} (получится {next_val})'))
        return moves

    def get_moves(self):
        return [state for state, _ in self.get_moves_with_descriptions()]

    def __repr__(self):
        return str(self.n)


class HumanPlayer:
    """
    Игрок-человек для консольного взаимодействия в игре с делителями.

    Attributes:
        name (str): Имя игрока.
    """
    def __init__(self, name: str):
        self.name = name

    def make_move(self, state: GameState) -> GameState:
        moves_with_desc = state.get_moves_with_descriptions()
        print('\nДоступные ходы:')
        for idx, (m, desc) in enumerate(moves_with_desc, 1):
            print(f'  {idx}. {desc}')

        while True:
            choice = input(f'Игрок {self.name}, выберите номер хода (1-{len(moves_with_desc)}): ').strip()
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(moves_with_desc):
                    return moves_with_desc[idx - 1][0]
            print('Некорректный ввод. Попробуйте снова.')


class AIPlayer:
    """
    Бот, просчитывающий выигрышную позицию по делителям.

    Attributes:
        name (str): Имя бота.
    """
    def __init__(self, name: str):
        self.name = name

    def _can_win(self, n: int, depth: int = 0, max_depth: int = 6):
        st = GameState(n)

        if st.is_terminal():
            return False

        if depth >= max_depth:
            return False

        for next_st in st.get_moves():
            if not self._can_win(next_st.n, depth + 1, max_depth):
                return True

        return False

    def make_move(self, state: GameState) -> GameState:
        moves = state.get_moves()

        for m in moves:
            if m.is_terminal():
                return m

        for m in moves:
            if not self._can_win(m.n, depth=0, max_depth=6):
                return m

        return moves[0]


class Game:
    """
    Управляет игровым процессом и передачей хода в игре.

    Attributes:
        state (GameState): Текущее числовое состояние игры.
        players (list): Список участников игры.
    """
    def __init__(self, num_players: int):
        self.state = GameState(2017)
        if num_players == 1:
            self.players = [HumanPlayer('Игрок 1'), AIPlayer('Бот')]
        else:
            self.players = [HumanPlayer('Игрок 1'), HumanPlayer('Игрок 2')]

    def run(self):
        print('=== ИГРА С ДЕЛИТЕЛЯМИ (Число 2017) ===')
        print('Вычитаем делители. Проигрывает тот, у кого нет ходов.\n')

        current_idx = 0
        while True:
            current_player = self.players[current_idx]
            print(f'\nТекущее число на доске: {self.state.n}')

            if self.state.is_terminal():
                winner_idx = (current_idx + 1) % 2
                winner_name = self.players[winner_idx].name
                print('\n==========================================')
                print(f'У игрока {current_player.name} нет доступных ходов!')
                print(f'ПОБЕДА! Победил {winner_name}!')
                print('==========================================')
                break

            print(f'Ход делает: {current_player.name}')
            self.state = current_player.make_move(self.state)

            current_idx = (current_idx + 1) % 2


if __name__ == "__main__":
    print('Выберите режим игры:')
    print('1. Человек vs Бот')
    print('2. Человек vs Человек')

    mode = input('Ваш выбор (1 или 2): ').strip()
    num_p = 1 if mode != '2' else 2

    game = Game(num_p)
    game.run()