# README: Interactive SIR Model for Rumor Spreading

This project provides an interactive tool to simulate the **SIR model** for rumor spreading model from the article [Zhao et al., 2013](https://www.sciencedirect.com/science/article/pii/S037843711200934X)  , which divides a population into three categories: **Ignorants (I)**, **Spreaders (S)**, and **Stiflers (R)**. This model helps analyze how a rumor propagates, spreads, and eventually ceases within a community, based on specific parameters that influence the interaction rates and dynamics of rumor transmission.

## Model Overview

The SIR model for rumor spreading assumes:
- **Ignorants (I)**: Individuals who have not yet heard the rumor.
- **Spreaders (S)**: Individuals actively spreading the rumor.
- **Stiflers (R)**: Individuals who have heard the rumor but are no longer spreading it.

The dynamics of these groups are governed by the following differential equations:


![equation]https://latex.codecogs.com/svg.image?\begin{cases}\frac{dI}{dt}=-\bar{k}I&space;S,\\\frac{dS}{dt}=\lambda\bar{k}I&space;S-\bar{k}S(\gamma&space;S&plus;\eta&space;R)-\delta&space;S,\\\frac{dR}{dt}=(1-\lambda)\bar{k}I&space;S&plus;\bar{k}S(\gamma&space;S&plus;\eta&space;R)&plus;\delta&space;S,\end{cases}


<!-- \[ -->
<!-- \begin{cases} -->
<!--     \frac{dI}{dt} = -\bar{k} I S, \\ -->
<!--     \frac{dS}{dt} = \lambda \bar{k} I S - \bar{k} S (\gamma S + \eta R) - \delta S, \\  -->
<!--     \frac{dR}{dt} = (1 - \lambda) \bar{k} I S + \bar{k} S (\gamma S + \eta R) + \delta S, -->
<!-- \end{cases} -->
<!-- \] -->

where \( I + S + R = 1 \).

### Parameters

- **\( \bar{k} \)**: Average number of contacts per individual.
- **\( \lambda \)**: Transmission rate of the rumor from spreaders to ignorants.
- **\( \eta \)**: Removal rate due to stiflers' influence.
- **\( \gamma \)**: Removal rate due to ignorant influence.
- **\( \delta \)**: Spontaneous removal rate of spreaders.

### Assumptions

- The total population remains constant.
- Each individual in the population belongs to only one group at a time.
- Interaction rates and removal influences are homogeneously applied across the population.

## Features

- **Interactive Graph**: Visualize how the rumor spreads over time through the interactive graph, with sliders to adjust parameters and observe the impact on rumor dynamics.
- **Real-time Simulation**: Adjust parameters such as \( \lambda \), \( \eta \), \( \gamma \), \( \delta \), and \( \bar{k} \) to see how they affect the percentages of ignorants, spreaders, and stiflers in real time.
- **Dynamic Behavior**: Study the behavior of each population group over time to identify critical points in the rumor's spread and stifling process.

## Usage

1. **Install Required Libraries**: Make sure you have the necessary dependencies installed to run this program (e.g., Matplotlib for visualization, or any interactive graph library your program uses).
2. **Run the Program**: Execute the script to launch the interactive simulation.
3. **Adjust Parameters**: Use the sliders to change \( \lambda \), \( \eta \), \( \gamma \), \( \delta \), and \( \bar{k} \), observing how these changes affect the dynamics of the rumor.
4. **Analyze Results**: Review how different parameter values influence the spread and eventual suppression of the rumor.

## Example Scenarios

Try experimenting with various scenarios:
- **High Transmission Rate (\( \lambda \))**: Observe the rapid initial spread among ignorants.
- **Increased Stifler Influence (\( \eta \))**: Watch how stiflers quickly diminish the number of spreaders.
- **Higher Spontaneous Removal (\( \delta \))**: See how spreaders lose interest on their own, independent of other factors.

## Contributing

Contributions to improve this tool are welcome. You can suggest improvements, fix bugs, or enhance features through pull requests.

## License

This project is licensed under the MIT License.

## Acknowledgments

This model is inspired by epidemiological SIR models but adapted to represent rumor spreading rather than disease transmission. The parameters and equations have been tailored to simulate social dynamics, providing insights into rumor spread control and suppression in communities.

To reference the article in your README, you can add a section called **References** at the end. Here’s how you might format it:


## References

- Zhao, L., Cui, H., Qiu, X., Wang, X., & Wang, J. (2013). **SIR rumor spreading model in the new media age**. *Physica A: Statistical Mechanics and its Applications*, 392(4), 995-1003. doi: [10.1016/j.physa.2012.09.030](https://doi.org/10.1016/j.physa.2012.09.030). Available at [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S037843711200934X).

