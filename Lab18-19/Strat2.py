# На доске записаны два числа: 2014 и 2015. Петя и Вася ходят по очереди. За один ход можно
# — либо уменьшить одно из чисел на его ненулевую цифру или на ненулевую цифру другого числа;
# — либо разделить одно из чисел пополам, если оно чётное.
# Выигрывает тот, кто первым напишет однозначное число.

class GameState:
    """
    Представляет текущее состояние игры с двумя числами (a, b).

    Attributes:
        a (int): Первое число на доске.
        b (int): Второе число на доске.
    """
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def is_terminal(self):
        return (1 <= self.a <= 9) or (1 <= self.b <= 9)

    def get_digits(self):
        digits = []
        for num in (self.a, self.b):
            for ch in str(num):
                d = int(ch)
                if d != 0 and d not in digits:
                    digits.append(d)
        return digits

    def get_moves_with_descriptions(self):
        moves = []
        digits = self.get_digits()

        for d in digits:
            if self.a - d > 0:
                moves.append((GameState(self.a - d, self.b), f'Уменьшить {self.a} на цифру {d}'))

        if self.a % 2 == 0 and self.a > 0:
            moves.append((GameState(self.a // 2, self.b), f'Разделить {self.a} пополам'))

        for d in digits:
            if self.b - d > 0:
                moves.append((GameState(self.a, self.b - d), f'Уменьшить {self.b} на цифру {d}'))

        if self.b % 2 == 0 and self.b > 0:
            moves.append((GameState(self.a, self.b // 2), f'Разделить {self.b} пополам'))

        unique_moves = []
        seen = []
        for state, desc in moves:
            key = (state.a, state.b)
            if key not in seen:
                seen.append(key)
                unique_moves.append((state, desc))

        return unique_moves

    def get_moves(self):
        return [state for state, _ in self.get_moves_with_descriptions()]

    def __repr__(self):
        return f'({self.a}, {self.b})'


class HumanPlayer:
    """
    Игрок, совершающий ход через консольный ввод.

    Attributes:
        name (str): Имя или обозначение игрока.
    """
    def __init__(self, name: str):
        self.name = name

    def make_move(self, state: GameState):
        moves_with_desc = state.get_moves_with_descriptions()
        print('\nДоступные ходы:')
        for idx, (m, desc) in enumerate(moves_with_desc, 1):
            print(f'  {idx}. {desc} -> {m}')

        while True:
            choice = input(f'Игрок {self.name}, выберите номер хода (1-{len(moves_with_desc)}): ').strip()
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(moves_with_desc):
                    return moves_with_desc[idx - 1][0]
            print('Некорректный ввод. Попробуйте снова.')


class AIPlayer:
    """
    Бот, выбирающий выигрышный ход.

    Attributes:
        name (str): Имя бота.
    """
    def __init__(self, name: str):
        self.name = name

    def _can_win(self, a: int, b: int, depth: int = 0, max_depth: int = 5):
        st = GameState(a, b)

        if st.is_terminal():
            return True

        if depth >= max_depth:
            return False

        for next_st in st.get_moves():
            if next_st.is_terminal():
                return True
            if not self._can_win(next_st.a, next_st.b, depth + 1, max_depth):
                return True

        return False

    def make_move(self, state: GameState) -> GameState:
        moves = state.get_moves()

        for m in moves:
            if m.is_terminal():
                return m

        for m in moves:
            if not self._can_win(m.a, m.b, depth=0, max_depth=5):
                return m

        return moves[0]

class Game:
    """
    Управляет игровым процессом и очередностью ходов в игре.

    Attributes:
        state (GameState): Текущее состояние игровых чисел на доске.
        players (list): Список из двух участников игры.
    """
    def __init__(self, num_players: int):
        self.state = GameState(2014, 2015)
        if num_players == 1:
            self.players = [HumanPlayer('Игрок 1'), AIPlayer('Бот')]
        else:
            self.players = [HumanPlayer('Игрок 1'), HumanPlayer('Игрок 2')]

    def run(self):
        print('=== ИГРА С ЧИСЛАМИ (2014, 2015) ===')
        print('Выигрывает тот, кто первым получит хотя бы одно однозначное число (1..9).\n')

        current_idx = 0
        while not self.state.is_terminal():
            current_player = self.players[current_idx]
            print(f'\nТекущие числа на доске: {self.state}')
            print(f'Ход делает: {current_player.name}')

            self.state = current_player.make_move(self.state)

            if self.state.is_terminal():
                print('\n==========================================')
                print(f'ПОБЕДА! {current_player.name} получил число {self.state}!')
                print('==========================================')
                break

            current_idx = (current_idx + 1) % 2


if __name__ == "__main__":
    print('Выберите режим игры:')
    print('1. Человек vs Бот')
    print('2. Человек vs Человек')

    mode = input('Ваш выбор (1 или 2): ').strip()
    num_p = 1 if mode != '2' else 2

    game = Game(num_p)
    game.run()