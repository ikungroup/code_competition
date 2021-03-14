# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import optuna
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
def objective(trial):
    x = trial.suggest_uniform('x', -10, 10)
    return (x - 2) ** 2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    sample = np.random.binomial(n=1, p=0.9, size=1)[0]
    a=2



    study = optuna.create_study()
    study.optimize(objective, n_trials=100)

    study.best_params  # E.g. {'x': 2.002108042}



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
