# README: Interactive SIR Model for Rumor Spreading

This program is an interactive tool to simulate the **SIR model** for rumor spreading model from the article [Zhao et al., 2013](https://www.sciencedirect.com/science/article/pii/S037843711200934X).

## Model Overview

The SIR model for rumor spreading assumes:
- **Ignorants (I)**: Individuals who have not yet heard the rumor.
- **Spreaders (S)**: Individuals actively spreading the rumor.
- **Stiflers (R)**: Individuals who have heard the rumor but are no longer spreading it.

The model is given by

$$
\begin{cases}
    \frac{dI}{dt} = -\bar{k} I S, \\
    \frac{dS}{dt} = \lambda \bar{k} I S - \bar{k} S (\gamma S + \eta R) - \delta S, \\ 
    \frac{dR}{dt} = (1 - \lambda) \bar{k} I S + \bar{k} S (\gamma S + \eta R) + \delta S,
\end{cases}
$$

notice that $ I + S + R = 1 $.

### Parameters

- $\bar{k}$: Average number of contacts per individual.
- $\lambda$: Transmission rate of the rumor from spreaders to ignorants.
- $\eta $: Removal rate due to stiflers' influence.
- $\gamma $: Removal rate due to ignorant influence.
- $\delta $: Spontaneous removal rate of spreaders.


## Usage

- As long as you have python together with its numpy, scipy and the matplotlib libraries installed, this program runs just like any other.


## License

This project is licensed under the MIT License.


## References

- Zhao, L., Cui, H., Qiu, X., Wang, X., & Wang, J. (2013). **SIR rumor spreading model in the new media age**. *Physica A: Statistical Mechanics and its Applications*, 392(4), 995-1003. doi: [10.1016/j.physa.2012.09.030](https://doi.org/10.1016/j.physa.2012.09.030). Available at [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S037843711200934X).

