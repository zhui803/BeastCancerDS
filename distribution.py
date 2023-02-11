import matplotlib.pyplot as plt
import scipy.stats as stats

def dist_info(df, column):
    mean = df[[column]].mean().item()
    std = df[[column]].std().item()

    print(column)
    print("Mean: " + str(mean))
    print("Std: " + str(std))
    print("")

    return mean, std

def dist_plot(df, column, mean, std, lower, upper):

    pdf = stats.norm.pdf(df[column].sort_values(), mean, std)

    plt.plot(df[column].sort_values(), pdf)
    plt.xlim([lower,upper])  
    plt.xlabel(column, size=12)    
    plt.ylabel("Frequency", size=12)                
    plt.grid(True, alpha=0.3, linestyle="--")
    plt.show()

def add_norm(df, column, new_column):

    df[new_column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
    
    return df
