import numpy as np
import pandas as pd

def main():
    date_rng = pd.date_range(start='11/12/2023', end='12/12/2023', freq='s')
    df = pd.DataFrame(date_rng, columns=['timestamp'])

    np.random.seed(42)
    df['value'] = np.random.randint(0, 100, size=(len(date_rng)))
    df = df.sample(frac=0.5, random_state=42).sort_values(by=['timestamp'])
    df.to_csv('data.csv', index=False)
    return


if __name__ == "__main__":
    main()
